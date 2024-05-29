"""The Converter class"""
from fpdf import FPDF
from PIL import Image
import os
from datetime import datetime
from paper import Paper


class Converter:
    """Handle conversions from images to PDF"""
    def __init__(self, images_path: list = None,
                 paper: tuple = (210, 297),
                 where: str = os.getcwd()) -> None:
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
        """Get the name of the new document"""
        return f'{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf'

    def convert(self):
        """Convert images to PDF"""
        fpdf = FPDF(unit='mm', format=self.__paper)
        for item in self.__images_path:
            image = Image.open(item)
            if image.width > image.height:
                w, h, x, y = Paper.new_wh_landscape(self.__paper, image)
                fpdf.add_page('L')
            else:
                w, h, x, y = Paper.new_wh_portrait(self.__paper, image)
                fpdf.add_page('P')
            print(w, h, x, y)
            fpdf.image(item, x=x, y=y, w=w, h=h)

        fpdf.output(os.path.join(self.__where, self.__get_name()))
