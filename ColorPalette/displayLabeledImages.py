#! /usr/bin/env python3
from PIL import Image, ImageTk
import glob, os
import numpy as np
import pandas as pd
import sys
import string

import tkinter as tk
from tkinter import simpledialog

img_list = sorted(glob.glob("../LabeledImages/*gt.png"))
palette = np.loadtxt("LabelColorMapping.csv",skiprows=1,delimiter=';',usecols=(1,2,3)).astype(int)
palette = palette.ravel()
palette = list(palette)


def main():
    img_index = 0
    displayAll(img_index)
    return

def displayAll(img_index):
    global img_list
    img = Image.open(img_list[img_index])
    checkPalette(img.getpalette())
    return

def checkPalette(img_palette):
    global palette
    if (np.array_equal(img_palette,palette)):
        return True
    else:
        return False
    
    
    # # compare color palette of img and of csv_file
    # # if not equal img_changed = img; img_changed.putpalette of csv_file; display both images; ask if it should be changed; quit
    # # check if all three images are available
    # # ttk.tree
    # # get unique color indices of img
    # # create small image boxes with colors
    # # create tkinter labels out of images
    # # create tkinter labels out of corresponding labels from csv_file
    # # pack all right
    # # create tkinter label out of img
    # # pack left
    
    # if key == n next image
    # # image_index = (image_index+1)%(len(list of images)-1)
    # # displayAll(image_index)
    # if key == p previous image
    # # image_index = (image_index-1)%(len(list of images)-1)
    # # displayAll(image_index)
    # if key == c color image
    # # 
    # if key == s scribble image
    # if key == d depth image
    # if key == g gt image
    # if key == q quit
    # if key == x exchange color
    
    
    
    
    #     global img_list
    #     global csv_file
    #     global color_index
    
    #     colormap = np.loadtxt("LabelColorMapping.csv",skiprows=1,delimiter=';',usecols=(1,2,3))
    #     colormap = colormap.astype(int)
    
    #     csv_file = pd.read_csv("LabelColorMapping.csv",delimiter=";")
    #     labels = csv_file['Label']
    
    #     color_index = rows[0]
    #     color = colormap[color_index]
    
    #     img_list = findImages(color_index, color)
    
    #     if (len(img_list) == 0):
    #         print("No image with this color: " + str(color))
    #         label = "NoImg"
    #         csv_file.set_value(color_index,'Label',label)
    #         csv_file.to_csv("LabelColorMapping.csv", sep=';',index=False)
    #         sys.exit()
    
    #     global img_number
    
    #     img = Image.open(img_list[img_number])
    #     color_img = Image.new('RGB',(60,60),tuple(color))
    
    #     global root
    #     root = tkinter.Tk()
    
    #     photo_color = ImageTk.PhotoImage(color_img)
    #     photo_img = ImageTk.PhotoImage(img)
    
    #     w1 = tkinter.Label(root, image=photo_color).pack()
    #     explanation = color
    #     w2 = tkinter.Label(root, 
    #                padx = 10, 
    #                text=explanation).pack()
    #     global w3
    #     w3 = tkinter.Label(root, image=photo_img)
    #     w3.pack()
    #     root.bind_all('<Key>', key)
    #     root.mainloop()
    
    # def key(event):
    #     global root
    #     root.unbind_all('<Key>')
    #     if event.char in ('n', 'p', 'c'):
    #         global img_number
    #         global img_list
    
    #         if event.char == 'n':
    #             img_number = img_number+1
    #             img_number = img_number % (len(img_list)-1)
    #         elif event.char == 'p':
    #             img_number = img_number-1
    #             img_number = img_number % (len(img_list)-1)
    #         img_path = img_list[img_number]
    
    #         if event.char == 'c':
    #             img_path = str.replace(img_path, 'gt', 'image')
    
    
    #         img = Image.open(img_path)
    #         photo_img = ImageTk.PhotoImage(img)
    #         global w3
    #         w3.configure(image=photo_img)
    #         w3.image = photo_img
    #     if event.char == 'l':
    #         label = simpledialog.askstring('Input', 'Label Name')
    #         global csv_file
    #         global color_index
    #         # add label input to labels
    #         csv_file.set_value(color_index,'Label',label)
    #         csv_file.to_csv("LabelColorMapping.csv", sep=';',index=False)
    #         root.quit()
    #     root.bind_all('<Key>', key)
    
    # def findImages(color_index, color):
    #     out = []
    #     for infile in sorted(glob.glob("../LabeledImages/*gt.png")):
    #         img = Image.open(infile)
    #         img_indexed_colors = np.array(img)
    
    #         palette = img.getpalette()
    #         palette = np.array(palette).reshape(len(palette)/3, 3)
    
    #         color_index2 = np.where(np.all(palette==color, axis=1))[0][0]
    
    #         if color_index2 != color_index:
    #             print("Different color indices. Original:" + str(color_index) + " - Image: " + str(color_index))
    #         color_index = color_index2
    
    
    #         if (color_index in img_indexed_colors[:,:]):
    #             out.append(infile)
    #     return out

if __name__ == "__main__":
    main()
