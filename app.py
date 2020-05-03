import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


foo = Image.open("/Users/wesleywong/Desktop/test small.jpg")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.fuckgarbagecollect = []

        self.pack()

        self.quit_button()
        finzzzzz = self.load_ims_button()
        self.load_bg_button()
        self.sel_stitch_button()
        self.stitch_ims_button()
        self.im_serve(finzzzzz)

    
        
    def fin(self,multiple):
        if multiple==True:
            multi = filedialog.askopenfilenames()
            multi = list(multi) #list of files
            return multi
        else:
            single = filedialog.askopenfilename()
            return single

    def load_ims_button(self):
        self.load_ims = tk.Button(self)
        self.load_ims["text"] = "Select\nImages"
        finzzz = self.load_ims["command"] = self.fin(multiple=True)
        self.load_ims.pack()
        return finzzz

    def load_bg_button(self):
        self.load_bg = tk.Button(self)
        self.load_bg["text"] = "Select\BG"
        self.load_bg["command"] = self.say_hi
        self.load_bg.pack()

    def sel_stitch_button(self):
        self.sel_stitch = tk.Button(self)
        self.sel_stitch["text"] = "Select\nSet"
        self.sel_stitch["command"] = self.say_hi
        self.sel_stitch.pack()

    def stitch_ims_button(self):
        self.stitch_ims = tk.Button(self)
        self.stitch_ims["text"] = "Stitch\nSet"
        self.stitch_ims["command"] = self.say_hi
        self.stitch_ims.pack()

    def quit_button(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack()

    def say_hi(self):
        print("hi there, everyone!")

    def im_serve(self,inputs):
        for i in range(len(inputs)):
            temp1 = Image.open(inputs[i])
            temp1 = temp1.resize((150, 150), resample=Image.LANCZOS)
            self.fuckgarbagecollect.append(ImageTk.PhotoImage(temp1))
        
        for i in range(0,len(self.fuckgarbagecollect)):
            j = tk.Label(self.master, image=self.fuckgarbagecollect[i])
            j.pack()
    

root = tk.Tk()
app = Application(master=root)
app.mainloop()


