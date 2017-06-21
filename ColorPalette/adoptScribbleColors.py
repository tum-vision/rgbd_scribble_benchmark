#! /usr/bin/env python3
from PIL import Image
import glob, os
import numpy as np
import string

original_map = np.loadtxt("pixelvalues.txt")
original_map = original_map.astype(int)

for scribble_path in sorted(glob.glob("../LabeledImages/*scribbles.png")):
    gt_path = str.replace(scribble_path, 'scribbles', 'gt')
    
    scribble_img = Image.open(scribble_path)
    gt_img = Image.open(gt_path)
    
    scribble_indexed = np.array(scribble_img) # Convert to NumPy array to easier access
    gt_indexed = np.array(gt_img)
    
    changed = False
    for x in range(scribble_indexed.shape[0]):
        for y in range(scribble_indexed.shape[1]):
            if x > 700 or y > 700:
                scribble_img.save(scribble_path, dpi=(640,480))
                print(scribble_path)
                exit()
            if scribble_indexed[x,y] != 0 and scribble_indexed[x,y] != gt_indexed[x,y]:
                changed = True
                scribble_indexed[x,y] = gt_indexed[x,y]
    
    if (changed):
        scribble_img = Image.fromarray(scribble_indexed)
        scribble_img.putpalette(gt_img.getpalette())
        
        scribble_img.save(scribble_path)
        print("Adopted: " + scribble_path)
