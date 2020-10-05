# I want to write a desktop application that displays images in an directory and
# moves the image into an new folder with a click of a button.
# This is to organize folders with hundreds of images

# print(f'Hi, {name}')

# Libraries -> Tkinter, PIL, os, sys, glob, shutil

import os, sys, shutil

import tkinter as tk

from PIL import ImageTk, Image

ImageList = []  # empty Image list
ImageExtList = [".jpg", ".jpeg", ".bmp", ".gif", "png"]
path = ""

os.chdir(r'C:\Users\Gary\Desktop\New folder')  # os.chdir -> change current dir
WorkingDir = os.getcwd()  # os.getcwd() -> get current working dir


def GetImageList(Path):
    # get image files from working dir and put images in list
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext in ImageExtList:
            ImageList.append(f)

    Path = WorkingDir + '\\' + ImageList[10]

    return Path


def ImageLoader():
    originalImage = Image.open(path)

    img_w = originalImage.size[0]
    img_h = originalImage.size[1]

    delta_h = (height / 2 - 3) - img_h
    delta_w = (width / 2 - 3) - img_w

    resize_h = img_h
    resize_w = img_w

    # resize logic
    if (delta_h <= 0 and delta_w > 0) or (delta_h <= 0 and 0 > delta_w > delta_h):
        # too tall
        resize_h = height
        resize_w = height / img_h * img_w

    elif (delta_h > 0 and delta_w <= 0) or (0 > delta_h > delta_w and delta_w <= 0):
        # too wide
        resize_h = width / img_w * img_h
        resize_w = width

    resizeImage = originalImage.resize((int(resize_w), int(resize_h)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resizeImage)

    return img


# create root app and window size
class ImageOrganizer(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title("Image Organizer")
        # root.overrideredirect(True)              #fullscreen
        self.parent.geometry(f'{width}x{height}')

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        """width=width / 2, height=height / 2 - 4,"""
        frame1 = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)
        frame2 = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)
        frame_img = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=1, column=0, sticky="nsew")
        frame_img.grid(row=0, column=1, rowspan=2, sticky="nsew")

        Img = ImageLoader()

        panel = tk.Label(frame_img, image=Img, text="IMAGE")
        panel.pack(side="bottom", fill="both", expand="yes")


"""
def test():
"""

if __name__ == '__main__':
    root = tk.Tk()

    width = root.winfo_screenwidth() - 100
    height = root.winfo_screenheight() - 100

    path = GetImageList(path)

    # test()

    ImageOrganizer(root)

    root.mainloop()
