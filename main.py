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
path = None

os.chdir(r'C:\Users\Gary\Desktop\New folder')  # os.chdir -> change current dir
WorkingDir = os.getcwd()  # os.getcwd() -> get current working dir


def GetImageList():
    # get image files from working dir and put images in list and list box
    for index, f in enumerate(os.listdir(), start=1):
        f_name, f_ext = os.path.splitext(f)
        if f_ext in ImageExtList:
            ImageList.append(f)
            root.imageListbox.insert(index, f_name + f_ext)


def GetImagePath(ImageName):
    Path = WorkingDir + '\\' + ImageName
    return Path


def ImageLoader(Path):
    originalImage = Image.open(Path)

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


def changeImg(Path):
    # keep ref to image cause of garbage collection
    photo = ImageLoader(Path)
    root.panel['image'] = photo
    root.panel.image = photo


def on_click_listbox(event):
    ImageChanged()


def ImageChanged():
    try:
        Selection = root.imageListbox.curselection()
        if Selection != root.imageSelection:
            newPath = GetImagePath(str(root.imageListbox.get(root.imageListbox.curselection())))
            changeImg(newPath)
            root.imageSelection = Selection
            print("item changed")
        else:
            print("asdf")
    except TclError:
        print("select item")


def MoveImage():
    print("move")
    OldImgPath = GetImagePath(str(root.imageListbox.get(root.imageListbox.curselection())))
    NewImgPath = os.path.join(WorkingDir, root.folderButton['text'])
    shutil.move(OldImgPath, NewImgPath)


def CreateNewFolder(FolderName):
    # Path
    NewFolderPath = os.path.join(WorkingDir, FolderName)

    # Create the directory
    # 'Nikhil'
    try:
        os.makedirs(NewFolderPath, exist_ok=True)
        print("Directory '%s' created successfully" % FolderName)
    except OSError as error:
        print("Directory '%s' can not be created" % FolderName)


def AddButton():

    if root.folderName.get() not in folderButtonList:
        folderButtonList.append(root.folderName.get())
        root.folderButton = Button(root.frame2, text=root.folderName.get(), command=MoveImage)
        root.folderButton.pack(side="bottom", fill="both", expand="yes")
        CreateNewFolder(root.folderName.get())


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

        # create widgets in frame1
        root.WorkingDir = tk.Entry(root.frame1, text="Working Directory")
        root.WorkingDir.pack(side="top", fill="both", expand="yes")
        root.sb1 = Scrollbar(root.frame1)
        root.sb1.pack(side="right", fill="both", expand="yes")
        root.imageListbox = Listbox(root.frame1, yscrollcommand=root.sb1.set)
        root.imageListbox.pack(side="bottom", fill="both", expand="yes")
        root.imageSelection = None
        root.sb1.config(command=root.imageListbox.yview)

        # create widgets in frame 2
        root.folderName = tk.Entry(root.frame2, text="add folder")
        root.folderName.pack(side="top", fill="both", expand="yes")
        root.folderButton = Button(root.frame2, text="+", command=AddButton)
        root.folderButton.pack(side="bottom", fill="both", expand="yes")


if __name__ == '__main__':
    root = tk.Tk()

    width = root.winfo_screenwidth() - 100
    height = root.winfo_screenheight() - 100

    folderButtonList = []

    app = ImageOrganizer(root)
    GetImageList()

    while TRUE:
        # use left mouse click on a list item to display selection
        root.imageListbox.bind('<ButtonRelease-1>', on_click_listbox)
        root.mainloop()
