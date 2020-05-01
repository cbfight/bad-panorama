from skimage import io
from matplotlib import pyplot as plt
from tkinter import filedialog
from tkinter import *
import cv2
import math
import statistics
import numpy as np
import os

#get home
home = os.path.expanduser("~")
savepath = os.path.join(home,'Desktop')
#stitcher
stitcher = cv2.createStitcher()

#file dialogue
root = Tk()
root.filenames = filedialog.askopenfilenames(initialdir="/",title="select images")
root.destroy()

fins = root.tk.splitlist(root.filenames) #list of files

plotDims = math.ceil(math.sqrt(len(fins))) #get grid dimensions

#show single images
fig, ax = plt.subplots()
i = 1
for image in fins:
    fig.add_subplot(plotDims,plotDims,i)
    ax.axis('off')
    plt.axis('off')
    io.imshow(image)
    i+=1
plt.show()

#stitch
stitchQueue = []
for image in fins:
    needs_stitch=cv2.imread(image)
    stitchQueue.append(needs_stitch)

status, stitched = stitcher.stitch(stitchQueue)
stitched = cv2.cvtColor(stitched, cv2.COLOR_BGR2RGB)
stitchednp = np.array(stitched)

#crop
rows_w_image = []
cols_w_image = []
flat_image = np.add(stitchednp[:,:,0],stitchednp[:,:,1],stitchednp[:,:,2])
row_counter = 0
col_counter = 0
for row in flat_image:
    if statistics.mean(row) > 5:
        rows_w_image.append(row_counter)
    row_counter += 1

for col in np.transpose(flat_image):
    if statistics.mean(col) > 5:
        cols_w_image.append(col_counter)
    col_counter += 1

left_boundary = rows_w_image[0]
right_boundary = rows_w_image[-1]
top_boundary = cols_w_image[0]
bottom_boundary = cols_w_image[-1]

cropped = stitched[left_boundary:right_boundary,top_boundary:bottom_boundary,:]

io.imshow(cropped)
plt.axis('off')
plt.savefig(str(savepath+'/test.png'),bbox_inches='tight', dpi=1200)
plt.show()







