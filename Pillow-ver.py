#-----------import stuffs--------------------#
from fpdf import FPDF
from PIL import Image
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
    imageWidth = image.width // paperWidth
    imageHeight = image.height // paperHeight
    if imageHeight >= imageWidth:
        newWidth = image.width // imageHeight
        newHeight = paperHeight
    elif imageHeight < imageWidth:
        newWidth = paperWidth
        newHeight = image.height // imageWidth

    return newWidth, newHeight

def AspCalc_L(paperWidth, paperHeight, image):
    imageWidth = image.width // paperHeight
    imageHeight = image.height // paperWidth   
    if imageHeight >= imageWidth:
        newWidth = image.width // imageHeight
        newHeight = paperWidth
    elif imageHeight < imageWidth:
        newWidth = paperHeight
        newHeight = image.height // imageWidth

    return newWidth, newHeight

def folderSrc(folder):
    imageList = []
    print('\n'+ 'Your directory is: ' + folder +'\n')                                                                                     
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

# def open():
#     path = folder
#     command = 'explorer.exe ' + path
#     os.system(command)      

while True:
    # -------------- TUTORIAL ----#

    print("JPG-to-PDF with CLI v.3.4.0_P" + '\n' + 'Copyright (c) 2022 Jangsoodlor. All rights reserved.' + '\n')
    print('Please move all of your pictures that you desired to be convert to a PDF file one folder before using this program.' + '\n'
    + 'If you left your field blank, the configuration of your PDF document will be automatically set by the default parameters.'+'\n'+'The outputted file will be located in the directory of your folder that is containing your images.'+'\n')

    # --------------- USER INPUT -------------------- #
    how = input('How do you want to import photos (folder/manual): ')

    # Declaring how to import photos
    if how == 'fol':
        srcInput = input("Insert image folder (or Press ENTER to open select dialog): ") or openFolder()
        folder = rf'{srcInput}'
        imageList = folderSrc(folder)
    elif how == 'man':             
        imageList = listMaker()
        saveDir = input('Insert the folder that you want to save the PDF file to: ') or openFolder()
        folder = rf'{saveDir}'
    # End of the declaration

    name = str(input('Insert your desired document name (if left blank, your document will be named after the current time): ')) or getDateTimeStr() # Name of the output PDF file.
    size = input('Insert the paper size [A3/A4/A5] (Default: A4): ') or 'a4'
    aspect = str(input('Keep aspect ratio [Y/N] (Default: Y): ')) or 'y'  
    
    

    # --------------- DEFINE OUTPUT PAPER SIZE --------------------#
    pdf = FPDF(format = f'{size}')
    if size.lower().endswith(('a3')):
        paperWidth = int(297)
        paperHeight = int (420)
    elif size.lower().endswith(('a4')):
        paperWidth = int(210)
        paperHeight = int (297)
    elif size.lower().endswith(('a5')):
        paperWidth = int(148)
        paperHeight = int (210)

    # -------------- CONVERT TO PDF ------------ #
    

    print('\nFound ' + str(len(imageList)) + ' images. Converting to PDF....\n')
    for i in range(0, len(imageList)):
        image = Image.open(imageList[i])                             # Open the image.
        print(image)
        width, height = image.size                                   # Get the width and height of that image.
        print(imageList[i])    
        
        if width > height:
            pdf.add_page('L')
            if aspect.lower() == 'n':
                pdf.image(imageList[i], 0, 0, paperHeight, paperWidth)
            elif aspect.lower() == 'y':
                print(AspCalc_L(paperWidth, paperHeight, image))                
                pdf.image(imageList[i], 0, 0, AspCalc_L(paperWidth, paperHeight, image)[0], AspCalc_L(paperWidth, paperHeight, image)[1])
        
        elif width <= height:
            pdf.add_page('P')
            if aspect.lower() == 'n':                
                pdf.image(imageList[i], 0, 0, paperWidth, paperHeight)
            elif aspect.lower() == 'y':
                print(AspCalc_P(paperWidth,paperHeight,image))  
                pdf.image(imageList[i], 0, 0, AspCalc_P(paperWidth, paperHeight, image)[0], AspCalc_P(paperWidth, paperHeight, image)[1])        

        
    pdf.output(folder + '\\' + name + '.pdf' , 'F')                      # Save the PDF.

    print('PDF generated successfully!')


    # ---------------Exit----#
    print('Press Y if you want to exit, Otherwise press ENTER twice.: ')
    if input() == 'y' or input() == 'Y':
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')