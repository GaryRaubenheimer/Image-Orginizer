# I want to write a desktop application that displays images in an directory and
# moves the image into an new folder with a click of a button.
# This is to organize folders with hundreds of images

# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Libraries -> Tkinter, PIL, os, sys, glob, shutil

import os

ImageList = []                                              # empty Image list
os.chdir(r'C:\Users\Gary\Desktop\New folder')               # os.chdir -> change current dir
WorkingDir = os.getcwd()                                    # os.getcwd() -> get current working dir

def GetImageList():
    # get image files from working dir and put images in list
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext in (".jpg", ".jpeg", ".bmp", ".gif", "png"):
            ImageList.append(f)


def test():
   # Display image on screen with in Tkinter
    

if __name__ == '__main__':
    test()
