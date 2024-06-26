#-----------import stuffs--------------------#
from fpdf import FPDF
from PIL import Image
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

imageList = []

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

def AspCalc_P(paper_Short, paper_long, image):
    pdf.add_page('P') 
    paper_ratio = paper_Short/paper_long
    image_ratio = image.width/image.height

    if image_ratio >= paper_ratio:
        newHeight = paper_Short / image_ratio
        newWidth = paper_Short

    elif image_ratio < paper_ratio:
        newWidth = paper_long * image_ratio
        newHeight = paper_long
    
    pdf.image(imageList[i], 0, 0, newWidth, newHeight)
    # return newWidth, newHeight

def AspCalc_L(paper_Short, paper_long, image):
    pdf.add_page('L')
    paper_ratio = paper_long / paper_Short
    image_ratio = image.width / image.height

    if image_ratio > paper_ratio:
        newWidth = paper_long
        newHeight = paper_long / image_ratio
    
    elif image_ratio <= paper_ratio:
        newWidth = paper_Short * image_ratio
        newHeight = paper_Short
    
    pdf.image(imageList[i], 0, 0, newWidth, newHeight)
    # return newWidth, newHeight

def folderSrc(folder):
    print('\n'+ 'Your directory is: ' + folder +'\n')                                                                                     
    for item in os.listdir(folder):
        if item.lower().endswith(('.png', '.jpg', '.jpeg')):
            # fullPath = folder + '\\' + f'{item}'
            fullPath = os.path.join(folder, item)
            imageList.append(fullPath)
            imageList.sort()      # Sort the images by name.
    return imageList

def listMaker():
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

    print("JPG-to-PDF with CLI v.3.5.0" + '\n' + 'Copyright (c) 2022 - 2023 Jangsoodlor. All rights reserved.' + '\n')
    print('If you left your field blank, the configuration of your PDF document will be automatically set by the default parameters.'+'\n'+'The outputted file will be located in the directory of your folder that is containing your images.'+'\n')

    # --------------- USER INPUT -------------------- #
    how = input('Choose how you want to import your photos \n 1. Import from folder (fol) \n 2. Import from specific files (man) \n: ')

    # Declaring how to import photos
    if how == 'fol':
        srcInput = input("Insert image folder (or Press ENTER to open select dialog): ") or openFolder()
        folder = rf'{srcInput}'
        imageList = folderSrc(folder)
    elif how == 'man':             
        imageList = listMaker()
        saveDir = input('Insert the folder that you want to save the PDF file to: ') or openFolder()
        folder = rf'{saveDir}'
    else:
        pass
    # End of the declaration

    name = str(input('Insert your desired document name (if left blank, your document will be named after the current time): ')) or getDateTimeStr() # Name of the output PDF file.
    size = input('Insert the paper size [A3/A4/A5] (Default: A4): ') or 'a4'
    aspect = str(input('Keep aspect ratio [Y/N] (Default: Y): ')) or 'y'  
    
    

    # --------------- DEFINE OUTPUT PAPER SIZE --------------------#
    pdf = FPDF(format = f'{size}')
    if size.lower().endswith(('a3')):
        paper_Short = int(297)
        paper_long = int (420)
    elif size.lower().endswith(('a4')):
        paper_Short = int(210) 
        paper_long = int (297)
    elif size.lower().endswith(('a5')):
        paper_Short = int(148)
        paper_long = int (210)

    # -------------- CONVERT TO PDF ------------ #
    

    print('\nFound ' + str(len(imageList)) + ' images. Converting to PDF....\n')
    for i in range(0, len(imageList)):
        image = Image.open(imageList[i])                             # Open the image.
        print(image)
        width, height = image.size                                   # Get the width and height of that image.
        print(imageList[i])    
        
        if aspect.lower() == 'y':
            if width >= height:
                AspCalc_L(paper_Short, paper_long, image)             

            elif width < height:
                AspCalc_P(paper_Short,paper_long,image)

        elif aspect.lower() == 'n':
            if width >= height:
                pdf.add_page('L')
                pdf.image(imageList[i], 0, 0, paper_long, paper_Short)

            elif width < height:
                pdf.add_page('P')              
                pdf.image(imageList[i], 0, 0, paper_Short, paper_long)


    pdf.output(folder + '\\' + name + '.pdf' , 'F')                      # Save the PDF.

    print('PDF generated successfully!')


    # ---------------Exit----#
    print('Press Y if you want to exit, Otherwise press ENTER twice.: ')
    if input() == 'y' or input() == 'Y':
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')