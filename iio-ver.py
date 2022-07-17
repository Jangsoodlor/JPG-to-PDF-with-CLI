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
    filePath = filedialog.askdirectory()
    return filePath

def AspCalc_P(paperWidth, paperHeight, image):
    imageHeight = image.shape[1] // paperWidth   #594
    imageWidth = image.shape[0] // paperHeight    
    if imageWidth >= imageHeight:
        newWidth = image.shape[1] // imageWidth
        newHeight = paperHeight
    elif imageWidth < imageHeight:
        newWidth = paperWidth
        newHeight = image.shape[0] // imageHeight

    return newWidth, newHeight

def AspCalc_L(paperWidth, paperHeight, image):
    imageHeight = image.shape[1] // paperHeight
    imageWidth = image.shape[0] // paperWidth     
    if imageWidth >= imageHeight:
        newWidth = image.shape[1] // imageWidth
        newHeight = paperWidth
    elif imageWidth < imageHeight:
        newWidth = paperHeight
        newHeight = image.shape[0] // imageHeight

    return newWidth, newHeight

def folder_src(folder):
    imageList = []
    print('Your directory is: ' + folder +'\n')                                                                                     
    for item in os.listdir(folder):
        if item.lower().endswith(('.png', '.jpg', '.jpeg')):
            fullPath = folder + '\\' + f'{item}'
            imageList.append(fullPath)
            imageList.sort()      # Sort the images by name.
    return imageList

def listMaker():
    imageList = []
    while True:
        src = input('Insert image path: ')
        if src == '':
            break
        imageList.append(src)
    return imageList      

while True:
    # -------------- TUTORIAL ----#

    print("JPG-to-PDF with CLI v.3.3.1" + '\n' + 'Copyright (c) 2022 Jangsoodlor. All rights reserved.' + '\n')
    print('Please move all of your pictures that you desired to be convert to a PDF file one folder before using this program.' + '\n'
    + 'If you left your field blank, the configuration of your PDF document will be automatically set by the default parameters.'+'\n'+'The outputted file will be located in the directory of your folder that is containing your images.'+'\n')

    # --------------- USER INPUT -------------------- #
    how = input('How do you want to import photos (folder/manual): ')
    name = str(input('Insert your desired document name (if left blank, your document will be named after the current time): ')) or getDateTimeStr()                    # Name of the output PDF file.
    size = input('insert the paper size [A3/A4/A5] (Default: A4): ') or 'a4'
    aspect = str(input('keep your aspect ratio?[Y/N] (Default: Y): ')) or 'y'
    
    
    # ---------------Declaring how to import photos -----------------------#
    pdf = FPDF(format = f'{size}')
    if how == 'fol':
        srcInput = input("insert your picture's folder directory (or Press ENTER to open select dialog): ") or openFolder()
        folder = rf'{srcInput}'
        imageList = folder_src(folder)
    elif how == 'man':             
        imageList = listMaker()                                                                             # Contains the list of all images to be converted to PDF.
        folder = input('Insert the folder that you want to save the PDF file to: ') or openFolder()
    # --------------- DEFINE OUTPUT PAPER SIZE --------------------#

    if size.lower().endswith(('a3')):
        paperWidth = int(297)
        paperHeight = int (420)
    elif size.lower().endswith(('a4')):
        paperWidth = int(210)
        paperHeight = int(297)
    elif size.lower().endswith(('a5')):
        paperWidth = int(148)
        paperHeight = int (210)

    # -------------- CONVERT TO PDF ------------ #
    print('\nFound ' + str(len(imageList)) + ' images. Converting to PDF....\n')
    for i in range(0, len(imageList)):
        image = iio.v3.imread(imageList[i])
        print(imageList[i])
        
        if image.shape[1] > image.shape[0]:
            pdf.add_page('L')
            if aspect.lower() == 'n':
                pdf.image(imageList[i], 0, 0, paperHeight, paperWidth)
            elif aspect.lower() == 'y':
                print(AspCalc_L(paperWidth, paperHeight, image))                
                pdf.image(imageList[i], 0, 0, AspCalc_L(paperWidth, paperHeight, image)[0], AspCalc_L(paperWidth, paperHeight, image)[1])
        
        elif image.shape[1] <= image.shape[0]:
            pdf.add_page('P')
            if aspect.lower() == 'n':                
                pdf.image(imageList[i], 0, 0, paperWidth, paperHeight)
            elif aspect.lower() == 'y':
                print(AspCalc_P(paperWidth, paperHeight, image))  
                pdf.image(imageList[i], 0, 0, AspCalc_P(paperWidth, paperHeight, image)[0], AspCalc_P(paperWidth, paperHeight, image)[1])        

        
    pdf.output(folder + '\\' + name + '.pdf' , 'F')                      # Save the PDF.

    print('PDF generated successfully!')


    # ---------------Exit----#
    print('Press Y if you want to exit, Otherwise press ENTER twice.: ')
    if input() == 'y' or input() == 'Y':
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')