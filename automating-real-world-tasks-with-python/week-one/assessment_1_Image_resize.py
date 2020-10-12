#!/usr/bin/env python3

import os, glob
from PIL import Image

new_size = 128, 128  #Setting the new size into 128x128

#Iterating to each image file 
for file in glob.glob("ic_*"): 
       img = Image.open(file).convert('RGB')  
       img.rotate(270).resize(new_size).save("/opt/icons/" + file, "JPEG") #Rotating,resizing and saving while iterating
