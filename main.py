# I want to write a desktop application that displays images in an directory and
# moves the image into an new folder with a click of a button.
# This is to organize folders with hundreds of images

# print(f'Hi, {name}')

# Libraries -> Tkinter, PIL, os, sys, glob, shutil

import os, sys, shutil
from tkinter import *
import tkinter as tk

from PIL import ImageTk, Image

ImageList = []  # empty Image list
ImageExtList = [".jpg", ".jpeg", ".bmp", ".gif", "png"]
path = ""

os.chdir(r'C:\Users\Gary\Desktop\New folder')  # os.chdir -> change current dir
WorkingDir = os.getcwd()  # os.getcwd() -> get current working dir


def GetImageList(Path):
    # get image files from working dir and put images in list and list box
    for index, f in enumerate(os.listdir(), start = 1):
        f_name, f_ext = os.path.splitext(f)
        if f_ext in ImageExtList:
            ImageList.append(f)
            root.imageListbox.insert(index, f_name)

    Path = WorkingDir + '\\' + ImageList[5]

    return Path


def ImageLoader():
    originalImage = Image.open(path)

    img_w = originalImage.size[0]
    img_h = originalImage.size[1]

    # root.update()

    delta_h = root.frame_img['height'] - img_h
    delta_w = root.frame_img['width'] - img_w

    resize_h = img_h
    resize_w = img_w

    # resize logic
    if (delta_h <= 0 and delta_w > 0) or (delta_h <= 0 and 0 > delta_w > delta_h):
        # too tall
        resize_h = root.frame_img['height']
        resize_w = root.frame_img['height'] / img_h * img_w

    elif (delta_h > 0 and delta_w <= 0) or (0 > delta_h > delta_w and delta_w <= 0):
        # too wide
        resize_h = root.frame_img['width'] / img_w * img_h
        resize_w = root.frame_img['width']

    resizeImage = originalImage.resize((int(resize_w), int(resize_h)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resizeImage)

    return img


def changeImg():
    # keep ref to image cause of garbage collection
    photo = ImageLoader()
    root.panel['image'] = photo
    root.panel.image = photo


class ImageOrganizer(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Image Organizer")
        self.parent.geometry(f'{width}x{height}')
        '''
        # root.overrideredirect(True)              #fullscreen
        # root.rowconfigure(0, weight=1)
        # root.rowconfigure(1, weight=1)
        # root.columnconfigure(0, weight=1)
        # root.columnconfigure(1, weight=1)
        # fixed frame
        # root.frame1.grid_propagate(0)
        # root.frame2.grid_propagate(0)
        # root.frame_img.grid_propagate(0)
        # width=width / 2, height=height / 2,
        '''
        # create and place frames
        root.frame1 = tk.Frame(root, width=width / 2, height=height / 2, relief=tk.RIDGE, borderwidth=2)
        root.frame2 = tk.Frame(root, width=width / 2, height=height / 2, relief=tk.RIDGE, borderwidth=2)
        root.frame_img = tk.Frame(root, width=width / 2, height=height, relief=tk.RIDGE, borderwidth=2)
        root.frame1.grid(row=0, column=0, sticky="nsew")
        root.frame2.grid(row=1, column=0, sticky="nsew")
        root.frame_img.grid(row=0, column=1, rowspan=2, sticky="nsew")

        # create image panel in image frame
        root.panel = tk.Label(root.frame_img, text="IMAGE")
        root.panel.pack(side="bottom", fill="both", expand="yes")

        # create listbox in frame1
        root.imageListbox = Listbox(root.frame1)
        root.imageListbox.pack(side="bottom", fill="both", expand="yes")


"""
def test():
"""

if __name__ == '__main__':
    root = tk.Tk()

    width = root.winfo_screenwidth() - 100
    height = root.winfo_screenheight() - 100

    app = ImageOrganizer(root)
    path = GetImageList(path)
    changeImg()

    root.mainloop()
