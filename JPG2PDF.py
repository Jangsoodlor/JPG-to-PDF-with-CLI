#-----------import stuffs--------------------#
from fpdf import FPDF
from PIL import Image
import os
import natsort

while True:
    # --------------- USER INPUT -------------------- #

    folderinput = input("insert your picture's folder directory: ")
    folder = rf'{folderinput}'                                                                                 # Folder containing all the images.
    name = str(input("insert your desired document name: "))+".pdf"                                            # Name of the output PDF file.
    size = input("insert the paper size: ") or 'a4'


    
    # ---------------FPDF--------------------------------#
    pdf = FPDF(format = f'{size}')
    imagelist = []                                                                                             # Contains the list of all images to be converted to PDF.

    # --------------- DEFINE OUTPUT PAPER SIZE --------------------#

    if size == "A3" or size == "a3":
        x = int(297)
        y = int (420)
    elif size == "A4" or size == "a4":
        x = int(210)
        y = int(297)
    elif size == "A5" or size == "a5":
        x = int(148)
        y = int (210)   


    # ------------- ADD ALL THE IMAGES IN A LIST ------------- #
    print('your directory is: ' + folder +'\n')

    for item in os.listdir(folder):
        if item.endswith('jpg') or item.endswith('png') or item.endswith('JPG') or item.endswith('PNG'):
            full_path = folder + '\\' + f'{item}'
            print(full_path)
            imagelist.append(full_path)
            print(imagelist)

    imagelist.sort()                                               # Sort the images by name.
    print('\n sorted imagelist \n')
    print(imagelist)
    for i in range(0, len(imagelist)):
        print(imagelist[i])

    # --------------- ROTATE ANY LANDSCAPE MODE IMAGE IF PRESENT (Disabled for now) ----------------- #
    
                
    

    # -------------- CONVERT TO PDF ------------ #
    print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")
    for i in range(0, len(imagelist)):
        im1 = Image.open(imagelist[i])                             # Open the image.
        print(im1)
        width, height = im1.size                                   # Get the width and height of that image.
        if width > height:
            pdf.add_page('L')
            pdf.image(imagelist[i], 0, 0, y, x)
        if width < height:
            pdf.add_page('P')
            pdf.image(imagelist[i], 0, 0, x, y)
        
    pdf.output(folder + '\\' + f'{name}', "F")                                 # Save the PDF.

    print("PDF generated successfully!")
    # ---------------Exit----#
    print("Press Y if you want to exit, Otherwise press ENTER twice.:")
    if input() == "y" or input() == "Y":
        exit()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
