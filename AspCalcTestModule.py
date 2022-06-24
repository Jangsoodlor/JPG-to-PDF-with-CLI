from PIL import Image
import os

imagelist = []    
w = 210
h = 297

folder = 'C:\\Users\\Jangsoodlor\\Desktop\\test\\landscapepik'

def AspCalc(w,h,im1):
    
    if im1.width > im1.height:
        width = h
        height = w
        pwratio = im1.width // width    #594
        phratio = im1.height // height   #450        
        if phratio >= pwratio:
            new_width = im1.width // phratio
            new_height = height
        elif phratio < pwratio:
            new_width = width
            new_height = im1. height // pwratio

    elif im1.width <= im1.height:
        width = w
        height = h
        pwratio = im1.width // width    #594
        phratio = im1.height // height   #450
        if phratio >= pwratio:
            new_width = im1.width // phratio
            new_height = height
        elif phratio < pwratio:
            new_width = width
            new_height = im1. height // pwratio

    return new_width,new_height
         


for item in os.listdir(folder):
        if item.lower().endswith(('.png', '.jpg', '.jpeg')):
            full_path = folder + '\\' + f'{item}'
            imagelist.append(full_path)
            imagelist.sort()      # Sort the images by name.

    

print('\nFound ' + str(len(imagelist)) + ' images. Converting to PDF....\n')
for i in range(0, len(imagelist)):
    print(imagelist[i])
    im1 = Image.open(imagelist[i])                             # Open the image.
    print(im1)
    width, height = im1.size
    print(AspCalc(w,h,im1)[1])


