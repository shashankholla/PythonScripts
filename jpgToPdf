import glob
from PIL import Image
from fpdf import FPDF
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input folder names with starting letter")
parser.add_argument("-o", "--output", help="output file name")
parser.add_argument("-r", "--res", help="output file name")
args = parser.parse_args()

if args.input:
    inputFile = args.input + "*"
else:
    inputFile = "Volume *"


if args.output:
    output = args.output
else:
    output = "op.pdf"

if args.res:
    resolution = float(args.res)
else:
    resolution = 100.0

folders = glob.glob(inputFile)
images = glob.glob(folders[0]+"/*")
imSize = Image.open(images[0]).size
imageList = []



for folder in folders:
    imageList.append(glob.glob(folder + "/*"))

imageList = [Image.open(image) for folderList in imageList for image in folderList ]
print("Number of files:" + str(len(imageList)))

#fileName = "op.pdf"
#print(imageList)
im1 = imageList[0]
#im1.show()
print("Please wait...")
im1.save(output, "PDF", resolution=resolution, save_all=True, append_images=imageList[1:])
    
for im in imageList:
    im.close()

        
        
   
    



  
    
    
    
    
