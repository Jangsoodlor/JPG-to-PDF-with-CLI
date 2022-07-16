#-----------import stuffs--------------------#
from fpdf import FPDF
import imageio as iio
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

#get time function#
def getDateTimeStr():
    now = datetime.now()
    return now.strftime('%Y%m%d_%H%M%S')

# open folder w/gui function#
def openFolder():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path

def AspCalc_P(w,h,im1):
    pwratio = im1.shape[1] // w    #594
    phratio = im1.shape[0] // h     
    if phratio >= pwratio:
        new_width = im1.shape[1] // phratio
        new_height = h
    elif phratio < pwratio:
        new_width = w
        new_height = im1.shape[0] // pwratio

    return new_width,new_height

def AspCalc_L(w,h,im1):
    pwratio = im1.shape[1] // h
    phratio = im1.shape[0] // w     
    if phratio >= pwratio:
        new_width = im1.shape[1] // phratio
        new_height = w
    elif phratio < pwratio:
        new_width = h
        new_height = im1.shape[0] // pwratio

    return new_width,new_height
def folder_src(folder):
    imagelist = []
    print('your directory is: ' + folder +'\n')                                                                                     
    for item in os.listdir(folder):
        if item.lower().endswith(('.png', '.jpg', '.jpeg')):
            full_path = folder + '\\' + f'{item}'
            imagelist.append(full_path)
            imagelist.sort()      # Sort the images by name.
    return imagelist

def listmaker():
    imagelist = []
    while True:
        src = input('insert da sauce')
        if src == '':
            break
        imagelist.append(src)
    return imagelist      

while True:
    # -------------- TUTORIAL ----#

    print("JPG-to-PDF with CLI v.3.3.1" + '\n' + 'Copyright (c) 2022 Jangsoodlor. All rights reserved.' + '\n')
    print('Please move all of your pictures that you desired to be convert to a PDF file one folder before using this program.' + '\n'
    + 'If you left your field blank, the configuration of your PDF document will be automatically set by the default parameters.'+'\n'+'The outputted file will be located in the directory of your folder that is containing your images.'+'\n')

    # --------------- USER INPUT -------------------- #
    how = input('How do you want to import photos')
    name = str(input('insert your desired document name (if left blank, your document will be named after the current time): ')) or getDateTimeStr()                    # Name of the output PDF file.
    size = input('insert the paper size [A3/A4/A5] (Default: A4): ') or 'a4'
    aspect = str(input('keep your aspect ratio?[Y/N] (Default: Y): ')) or 'y'
    
    
    # ---------------Declaring how to import photos -----------------------#
    pdf = FPDF(format = f'{size}')
    if how == 'fol':
        src_input = input("insert your picture's folder directory (or Press ENTER to open select dialog): ") or openFolder()
        folder = rf'{src_input}'
        imagelist = folder_src(folder)
    elif how == 'man':             
        imagelist = listmaker()                                                                             # Contains the list of all images to be converted to PDF.
        folder = input('insert da folder baka')  
    # --------------- DEFINE OUTPUT PAPER SIZE --------------------#

    if size.lower().endswith(('a3')):
        w = int(297)
        h = int (420)
    elif size.lower().endswith(('a4')):
        w = int(210)
        h = int(297)
    elif size.lower().endswith(('a5')):
        w = int(148)
        h = int (210)

    # -------------- CONVERT TO PDF ------------ #
    print('\nFound ' + str(len(imagelist)) + ' images. Converting to PDF....\n')
    for i in range(0, len(imagelist)):
        im1 = iio.v3.imread(imagelist[i])
        print(imagelist[i])
        
        if im1.shape[1] > im1.shape[0]:
            pdf.add_page('L')
            if aspect.lower() == 'n':
                pdf.image(imagelist[i], 0, 0, h, w)
            elif aspect.lower() == 'y':
                print(AspCalc_L(w,h,im1))                
                pdf.image(imagelist[i], 0, 0, AspCalc_L(w,h,im1)[0], AspCalc_L(w,h,im1)[1])
        
        elif im1.shape[1] <= im1.shape[0]:
            pdf.add_page('P')
            if aspect.lower() == 'n':                
                pdf.image(imagelist[i], 0, 0, w, h)
            elif aspect.lower() == 'y':
                print(AspCalc_P(w,h,im1))  
                pdf.image(imagelist[i], 0, 0, AspCalc_P(w,h,im1)[0], AspCalc_P(w,h,im1)[1])        

        
    pdf.output(folder + '\\' + name + '.pdf' , 'F')                      # Save the PDF.

    print('PDF generated successfully!')


    # ---------------Exit----#
    print('Press Y if you want to exit, Otherwise press ENTER twice.:')
    if input() == 'y' or input() == 'Y':
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')