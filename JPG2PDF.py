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
    # moon = str(input("Do you want to auto-rotate landscape pictures to portrait?(Y/N)?: ")) or 'n'
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
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in [f for f in filenames if f.endswith(".jpg") or f.endswith(".png")]:
            full_path = os.path.join(dirpath, filename)
            imagelist.append(full_path)

    imagelist.sort()                                               # Sort the images by name.
    for i in range(0, len(imagelist)):
        print(imagelist[i])

    # --------------- ROTATE ANY LANDSCAPE MODE IMAGE IF PRESENT (Disabled for now) ----------------- #
    # if moon == 'y' or  moon == 'Y':
    #     for i in range(0, len(imagelist)):
    #         im1 = Image.open(imagelist[i])                             # Open the image.
    #         print(im1)
    #         width, height = im1.size                                   # Get the width and height of that image.
    #         if width > height:
    #             print("rotating picture")
    #             im2 = im1.transpose(Image.ROTATE_270)                  # If width > height, rotate the image.
    #             os.remove(imagelist[i])                                # Delete the previous image.
    #             im2.save(imagelist[i])                                 # Save the rotated image.
                
    print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")

    # -------------- CONVERT TO PDF ------------ #
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

    # for image in imagelist:
    #     pdf.add_page()
    #     pdf.image(image, 0, 0, 297, 210)     
        
    pdf.output(folder + '\\' + f'{name}', "F")                                 # Save the PDF.

    print("PDF generated successfully!")
    # ---------------Exit----#
    print("Press Y if you want to exit, Otherwise press ENTER twice.:")
    if input() == "y" or input() == "Y":
        exit()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
