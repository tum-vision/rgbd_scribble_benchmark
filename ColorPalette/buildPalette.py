from PIL import Image

rgbTuples = []
with open("pixelvalues.txt","r") as inputFile:
    for line in inputFile.readlines():
        stringTuple = tuple((line.rstrip()).split('\t'))
        intTuple = [int(x) for x in stringTuple]
        
        rgbTuples.append(intTuple)

img = Image.new( 'RGB', (16,16), "black") # create a new black image
pixels = img.load()

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = tuple(rgbTuples.pop())

img.save("truecolor_source.png")
