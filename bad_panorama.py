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
stitcher = cv2.createStitcher(cv2.Stitcher_SCANS)

#file dialogue bg-correction
root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/",title="select background image")
root.destroy()
background = io.imread(root.filename)

#file dialogue inputs
root = Tk()
root.filenames = filedialog.askopenfilenames(initialdir="/",title="select stitch images")
root.destroy()


fins = root.tk.splitlist(root.filenames) #list of files

plotDims = math.ceil(math.sqrt(len(fins))) #get grid dimensions


background_average_r = np.average(background[:,:,0])
background_average_g = np.average(background[:,:,1])
background_average_b = np.average(background[:,:,2])


#show cropped single images and make stitch
fig, ax = plt.subplots()
i = 1
stitchQueue = []
for im in fins:
    image = cv2.imread(im)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    h, w = image.shape[:2]
    bg_thresh = 0.1
    # Make mask of black pixels - mask is True where image is black
    mBlack = (image[:, :, 0:3] < [background_average_r*bg_thresh,background_average_g*bg_thresh,background_average_b*bg_thresh]).all(2)
    # Make all pixels matched by mask into transparent ones
    image[mBlack] = (background_average_r,background_average_g,background_average_b)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    fig.add_subplot(plotDims,plotDims,i)
    ax.axis('off')
    plt.axis('off')
    io.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    i+=1
    stitchQueue.append(image)
plt.show()

    

status, stitched = stitcher.stitch(stitchQueue)
stitched = cv2.cvtColor(stitched, cv2.COLOR_BGR2RGB)
stitchednp = np.array(cv2.cvtColor(stitched,cv2.COLOR_BGR2GRAY),dtype='uint8')




#cropped = stitched[left_boundary:right_boundary,top_boundary:bottom_boundary,:]


io.imshow(stitched)
plt.axis('off')
plt.savefig(str(savepath+'/test.png'),bbox_inches='tight', dpi=1200)
plt.show()







