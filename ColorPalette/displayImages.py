from PIL import Image, ImageTk
import glob, os
import numpy as np
import pandas as pd
import sys
import string

import tkinter
from tkinter import simpledialog

img_number = 0
img_list = []

def main():
    colormap = np.loadtxt("LabelColorMapping.csv",skiprows=1,delimiter=';',usecols=(1,2,3))
    colormap = colormap.astype(int)
    
    global csv_file
    csv_file = pd.read_csv("LabelColorMapping.csv",delimiter=";")
    labels = csv_file['Label']
    
    rows = np.where(np.array(pd.isnull(labels)))[0]
    
    print(str(len(rows)) + " unlabeled pixels found.")
    
    if len(rows) == 0:
        print("Nothing to do.")
        sys.exit()
    
    global color_index
    color_index = rows[0]
    color = colormap[color_index]
    
    global img_list
    img_list = findImages(color_index)
    
    if (len(img_list) == 0):
        print("No image with this color.")
        sys.exit()
    
    global img_number
    
    img = Image.open(img_list[img_number])
    color_img = Image.new('RGB',(60,60),tuple(color))
    
    # color_img.show()
    global root
    root = tkinter.Tk()
    
    photo_color = ImageTk.PhotoImage(color_img)
    photo_img = ImageTk.PhotoImage(img)
    
    # logo = PhotoImage(file="../images/python_logo_small.gif")
    w1 = tkinter.Label(root, image=photo_color).pack()
    explanation = """Find label name of this color:"""
    w2 = tkinter.Label(root, 
               padx = 10, 
               text=explanation).pack()
    global w3
    w3 = tkinter.Label(root, image=photo_img)
    w3.pack()
    root.bind_all('<Key>', key)
    root.mainloop()

def key(event):
    global root
    root.unbind_all('<Key>')
    if event.char in ('n', 'p', 'c'):
        global img_number
        global img_list
        
        if event.char == 'n':
            img_number = img_number+1
        elif event.char == 'p':
            img_number = img_number-1
        
        img_path = img_list[img_number]
        
        if event.char == 'c':
            img_path = string.replace(img_path, 'gt', 'image')
        
        img_number = img_number % (len(img_list)-1)
        img = Image.open(img_list[img_number])
        photo_img = ImageTk.PhotoImage(img)
        global w3
        w3.configure(image=photo_img)
        w3.image = photo_img
    if event.char == 'l':
        label = simpledialog.askstring('Input', 'Label Name')
        global csv_file
        global color_index
        # add label input to labels
        csv_file.set_value(color_index,'Label',label)
        csv_file.to_csv("LabelColorMapping.csv", sep=';',index=False)
        root.quit()
    root.bind_all('<Key>', key)


def findImages(color_index):
    out = []
    for infile in sorted(glob.glob("../LabeledImages/*gt.png")):
        img = Image.open(infile)
        img_colors = np.array(img)
        
        
        if (color_index in img_colors[:,:]):
            out.append(infile)
    return out

if __name__ == "__main__":
    main()
