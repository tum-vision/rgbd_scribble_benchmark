from PIL import Image
import glob, os
import numpy as np
import pandas as pd

colormap = np.loadtxt("LabelColorMapping.csv",skiprows=1,delimiter=';',usecols=(1,2,3))
colormap = colormap.astype(int)

csv_file = pd.read_csv("LabelColorMapping.csv",delimiter=";")
labels = csv_file['Label']

###### Go to first unlabeled
# find first element of labels which is empty and save corresponding row index
# use index to get corresponding color from colormap

# use function findImages(color) to get a list of images with this color
# create an image with this color
# show this image
# open first image from the returned list
# user can type n for next image and p previous image, c for color image, l for label input
# add label input to labels
# csv_file.set_value(row)['Label'] = l
# csv_file.to_csv("LabelColorMapping.csv", sep=';')

for infile in glob.glob("../LabeledImages/*gt.png"):
    # file, ext = os.path.splitext(infile)
    img = Image.open(infile)
    
    img_colors = np.array(img) # Convert to NumPy array to easier access
    
    # Get the colour palette
    palette = img.getpalette()
    
    if palette == None:
        print('Add palette: ' + file)
        img.putpalette(original_map)
        img.save(infile)
    else:
        
        # Determine the total number of colours
        num_colours = len(palette)/3
        
        # Determine maximum value of the image data type
        # max_val = float(np.iinfo(indexed.dtype).max)
        
        # Create a colour map matrix
        map = np.array(palette).reshape(num_colours, 3) # / max_val
        
        if (np.array_equal(original_map,map)):
            print('Correct: ' + file)
        else:
            print('False: ' + file)


def findImages(color):
    out = []
    for infile in glob.glob("../LabeledImages/*gt.png"):        
        img = Image.open(infile)
        img_colors = np.array(img)
        
        if (color in img_colors.tolist()):
            out.push(infile)
