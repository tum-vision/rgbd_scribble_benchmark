from PIL import Image
import glob, os
import numpy as np

original_map = np.loadtxt("pixelvalues.txt")
original_map = original_map.astype(int)

for infile in glob.glob("../LabeledImages/Bedroom/Labelling/*.png"):
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)
    
    indexed = np.array(img) # Convert to NumPy array to easier access
    
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
