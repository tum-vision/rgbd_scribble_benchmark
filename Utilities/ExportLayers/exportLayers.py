#!/usr/bin/env python2

from gimpfu import *
import os

def export_layers(pattern, path, n_layer):
    pdb.gimp_message("Export layer "+ n_layer + " of " + pattern + " in directory " + path)
    
    fullpathpattern = os.path.join(path, pattern)
    num_files, files = pdb.file_glob(fullpathpattern, 0)

    pdb.gimp_message("Processing " + num_files + " files:")
    
    for file in files:
        img = pdb.gimp_file_load(file, file)
        pdb.gimp_message(file)
        export_layer(img, path, n_layer)

def export_layer(img, path, n_layer):
    dupe = img.duplicate()
    layers = dupe.layers
    
    for layer in layers:
        layer.visible = 0
            
    layer = layers[n_layer]
        
    layer.visible = 1
    filename = format_filename(img, n_layer)
    fullpath = os.path.join(path, filename)
    
    dupe.merge_visible_layers(0)
    pdb.file_png_save(1, dupe, dupe.layers[0], fullpath, filename, 0, 9, 1, 1, 1, 1, 1)


def format_filename(img, n_layer):
    imgname = os.path.splitext(img.name)[0]
    filename = imgname + '_layer_' + str(n_layer) + '.png'
    return filename



register(
    "python-export-layers",
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
        (PF_INT, "n_layer", "n_layer", "0")
    ],
    [],
    export_layers,)

main()
