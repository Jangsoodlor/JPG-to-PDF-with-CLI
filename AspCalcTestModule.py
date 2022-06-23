#-----------import stuffs--------------------#
from fpdf import FPDF
from PIL import Image
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

imagelist = []    
w = 297
h = 210

folder = 'C:\\Users\\Jangsoodlor\\Desktop\\test\\landscapepik'

def AspCalc(w,h,im1):
    if im1.width > im1.height:
        pwratio = im1.width // w    #594
        phratio = im1.height // h   #450
        if phratio >= pwratio:
            new_width = im1.width // phratio
            new_height = h
        elif phratio < pwratio:
            new_width = w
            new_height = im1. height // pwratio
        return new_width,new_height     


for item in os.listdir(folder):
        if item.lower().endswith(('.png', '.jpg', '.jpeg')):
            full_path = folder + '\\' + f'{item}'
            imagelist.append(full_path)
            imagelist.sort()      # Sort the images by name.

                                            
for i in range(0, len(imagelist)):
    print(imagelist[i])

print('\nFound ' + str(len(imagelist)) + ' images. Converting to PDF....\n')
for i in range(0, len(imagelist)):
    im1 = Image.open(imagelist[i])                             # Open the image.
    print(im1)
    width, height = im1.size
    print(AspCalc(w,h,im1))


