#!/usr/bin/env python2

from gimpfu import *
import os
import numpy as np

def convert_indexed(pattern, path, palette):
    print("Convert images of " + pattern + " in directory " + path + " to indexed images, using palette: " + palette)
    # pattern = "*.xcf"
    # path = "/home/andreasw/Bilder"
    # palette = "/home/andreasw/rgbd_benchmark/ColorPalette/pixelvalues.txt"
    required_map = np.loadtxt(palette).astype(int)
    required_map = np.reshape(required_map,(1,-1)).tolist()[0]
    length = len(required_map)
    fullpathpattern = os.path.join(path, pattern)
    num_files, files = pdb.file_glob(fullpathpattern, 0)    
    print("Processing " + str(num_files) + " files:")
    # file = "/home/andreasw/Bilder/12_Scribbles.xcf"
    for file in files:
        img = pdb.gimp_file_load(file, file)
        if img.layers[0].is_rgb or img.layers[0].is_grey:
            print("Convert: " + file)
            pdb.gimp_image_convert_indexed(img, 0, 4, 256, False, False, 'rgbd_palette.gpl')
        if img.layers[0].is_indexed:
            print("Change color map: " + file)
            pdb.gimp_image_set_colormap(img, 256, required_map)
        pdb.gimp_file_save(img,img.layers[0],file,file)

register(
    "python-convert-indexed",
    "Do stuff",
    "Longer description of doing stuff",
    "Andreas Wiedemann",
    "Andreas Wiedemann",
    "2016",
    "Do Stuff...",
    "*",      # Alternately use RGB, RGB*, GRAY*, INDEXED etc.
    [
        (PF_STRING, "glob_pattern", "glob_pattern", "*.xcf"),
        (PF_DIRNAME, "path", "Input Dir", ""),
        (PF_STRING, "palette", "palette", "")
    ],
    [],
    convert_indexed,)

main()
