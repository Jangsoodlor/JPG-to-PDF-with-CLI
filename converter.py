from fpdf import FPDF
from PIL import Image
import os
from datetime import datetime
from paper import Paper

class Converter:
    def __init__(self, images_path: list = None,
                 paper: tuple = (210, 297),
                 where:str = os.getcwd()) -> None:
        self.__paper = paper
        self.__images_path = images_path
        self.__where = where

    @property
    def paper(self):
        return self.__paper

    @paper.setter
    def paper(self, value):
        self.__paper = value

    @property
    def images_path(self):
        return self.__images_path

    @images_path.setter
    def images_path(self, new_array):
        self.__images_path = new_array

    @property
    def output(self):
        return self.__where

    @output.setter
    def output(self, where):
        self.__where = where

    def __get_name(self):
        return f'{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf'

    def convert(self):
        fpdf = FPDF(unit='mm', format=self.__paper)
        for item in self.__images_path:
            image = Image.open(item)
            if image.width >= image.height:
                w, h = Paper.new_wh_landscape(self.__paper, image)
                fpdf.add_page('L')
            else:
                w, h = Paper.new_wh_portrait(self.__paper, image)
                fpdf.add_page('P')
            fpdf.image(item, x=0, y=0, w=w, h=h)

        fpdf.output(os.path.join(self.__where, self.__get_name()))


if __name__ == '__main__':
    folder = r'C:\Users\Jangsoodlor\codes\JPG-to-PDF-with-CLI\test\png'
    os.chdir(folder)
    img_arr = []
    for i in os.listdir():
        if i.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_arr.append(os.path.join(folder, i))
    
    c = Converter()
    c.images_path = img_arr
    c.output = os.getcwd()
    c.convert()
