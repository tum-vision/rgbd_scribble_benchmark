#! /usr/bin/env python3
from PIL import Image, ImageTk
import glob, os
import numpy as np
import pandas as pd
import sys
import string
import pathlib

import matplotlib.colors as colors

import tkinter as tk

from tkinter import simpledialog

img_list = sorted(glob.glob("../LabeledImages/*gt.png"))
palette = np.loadtxt("LabelColorMapping.csv",skiprows=1,delimiter=';',usecols=(1,2,3)).astype(int)
palette = palette.ravel()
palette = list(palette)
csv_file = pd.read_csv("LabelColorMapping.csv",delimiter=";")
labels = csv_file['Label']
img_index = 0
list_ids = []

def main():
    global root
    root = tk.Tk()
    displayAll()
    return

def displayAll():
    global img_index
    global img_list
    global palette
    global root
    global photo_img
    global label_img
    global list_ids
    global w_canvas
    
    gt_path = img_list[img_index]
    img=Image.open(gt_path)
    root.wm_title(gt_path)
    # if (not checkPalette(img.getpalette())):
    #     photo_img1 = ImageTk.PhotoImage(img)
    #     img.putpalette(palette)
    #     photo_img2 = ImageTk.PhotoImage(img)
    #     w1 = tk.Label(root, image=photo_img1).pack()
    #     w2 = tk.Label(root, image=photo_img2).pack()
    #     if (tk.messagebox.askyesno("Palette", "Replace palette?")):
    #         img.save(gt_path)
    #         return
    #     root.mainloop()
    #     root.quit()
    #     exit()
    
    img_path = str.replace(gt_path, 'gt', 'image')
    if (not pathlib.Path(img_path).is_file()):
        tk.messagebox.showwarning("Missing","File missing: " + img_path)
    depth_path = str.replace(gt_path, 'gt', 'depth')
    if (not pathlib.Path(depth_path).is_file()):
        tk.messagebox.showwarning("Missing","File missing: " + depth_path)
    scribble_path = str.replace(img_path, 'depth', 'scribble')
    if (not pathlib.Path(scribble_path).is_file()):
        tk.messagebox.showwarning("Missing","File missing: " + scribble_path)
    
    
    
    photo_img = ImageTk.PhotoImage(img)
    label_img = tk.Label(root, image=photo_img)
    label_img.pack(side=tk.LEFT)
    # list_rects = []
    w_canvas = tk.Canvas(root, width=400, height=480)
    w_canvas.pack(side=tk.LEFT)
    
    displayLabels(img)
    
    root.bind_all('<Key>', key)
    root.mainloop()
    
    return

def rgb_to_hex(rgb_tuple):
    return colors.rgb2hex([1.0*x/255 for x in rgb_tuple])

def checkPalette(img_palette):
    global palette
    if (np.array_equal(img_palette,palette)):
        return True
    else:
        return False

def displayLabels(img):
    img_indexed_colors = np.unique(np.array(img))
    row = 10
    for color_index in img_indexed_colors:        
        w_canvas.create_rectangle(10, row, 30, row+20, fill=rgb_to_hex(palette[(color_index*3):(color_index*3+3)]))
        w_canvas.create_text(40, row+10, anchor=tk.W, font="Helvetica", text=str(color_index) + ' ' + labels[color_index])
        row += 30


def key(event):
    global root
    global img_list
    global img_index
    global photo_img
    global label_img
    global list_ids
    global w_canvas
    
    root.unbind_all('<Key>')
    
    
    img_path = img_list[img_index]
    if event.char in ('n', 'p'):
        if event.char == 'n':
            img_index = img_index+1
        elif event.char == 'p':
            img_index = img_index-1
        
        img_index = img_index % (len(img_list)-1)
        # display gt image
        # change canvas
        root.wm_title(img_path)
        img_path = img_list[img_index]
        img = Image.open(img_path)
        photo_img = ImageTk.PhotoImage(img)
        label_img.configure(image=photo_img)
        label_img.image = photo_img
        # checkPalette
        
        w_canvas.delete('all')
        
        displayLabels(img)
    if event.char in ('c','d','g'):
        if event.char == 'c':
            img_path = str.replace(img_path, 'gt', 'image')
        if event.char == 'd':
            img_path = str.replace(img_path, 'gt', 'depth')
        root.wm_title(img_path)
        img = Image.open(img_path)
        photo_img = ImageTk.PhotoImage(img)
        label_img.configure(image=photo_img)
        label_img.image = photo_img
    if event.char == 'q':
        root.quit()
        exit()
    if event.char == 'x':
        old_index = simpledialog.askstring('Exchange color index', 'Color index to be changed: ')
        new_index = simpledialog.askstring('Exchange color index', str(old_index) + ' -> ')
        
        img = Image.open(img_path)
        img_indexed = np.array(img)
        
        img_indexed[np.where(img_indexed == int(old_index))] = int(new_index)
        # np.place(img_indexed, img_indexed==old_index, [new_index])
        # img_indexed[img_indexed == old_index] = new_index
        img_new = Image.fromarray(img_indexed)
        img_new.putpalette(palette)
        photo_img = ImageTk.PhotoImage(img_new)
        label_img.configure(image=photo_img)
        label_img.image = photo_img
        # checkPalette
        
        w_canvas.delete('all')
        displayLabels(img_new)
        img_new.save(img_path)
    
    root.bind_all('<Key>', key)


if __name__ == "__main__":
    main()
