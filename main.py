# I want to write a desktop application that displays images in an directory and
# moves the image into an new folder with a click of a button.
# This is to organize folders with hundreds of images

# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Libraries -> Tkinter, PIL, os, sys, glob, shutil

import os, sys, shutil

from tkinter import *
from PIL import ImageTk, Image

ImageList = []  # empty Image list
os.chdir(r'C:\Users\Gary\Desktop\New folder')  # os.chdir -> change current dir
WorkingDir = os.getcwd()  # os.getcwd() -> get current working dir


def GetImageList():
    # get image files from working dir and put images in list
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext in (".jpg", ".jpeg", ".bmp", ".gif", "png"):
            ImageList.append(f)


def test():
    # Display image on screen with in Tkinter

    path = WorkingDir + '\\' + ImageList[10]

    # create root app and window size
    root = Tk()
    width = root.winfo_screenwidth()-100
    height = root.winfo_screenheight()-100
    # root.overrideredirect(True)              #fullscreen
    root.geometry(f'{width}x{height}')

    # resize image
    # originalImage = Image.open(path)
    # reWidth = int(originalImage.size[0]/width*originalImage.size[0])
    # reHeight = int(originalImage.size[1]/height*originalImage.size[1])
    # new_width = root.width
    # new_height = root.height
    # resizeImage = originalImage.resize(width, height)
    originalImage = Image.open(path)
    resizeImage = originalImage.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resizeImage)

    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()


if __name__ == '__main__':
    GetImageList()
    test()
