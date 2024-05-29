from fpdf import FPDF
from PIL import Image
import os
from datetime import datetime

class Converter:
    def __init__(self, img_arr=None):
        self.__img_arr = img_arr

    def get_datetime():
        return datetime.now().strftime('%Y%m%d_%H%M%S')

    def new_wh_portrait(self, paper_short, paper_long, image):
        paper_ratio = paper_short / paper_long
        image_ratio = image.width / image.height

        if image_ratio >= paper_ratio:
            new_width = paper_short
            new_height = paper_short / image_ratio

        else:
            new_width = paper_long * image_ratio
            new_height = paper_long
        return new_width, new_height

    def new_wh_landscape(self, paper_short, paper_long, image):
        paper_ratio = paper_long / paper_short
        image_ratio = image.width / image.height

        if image_ratio >= paper_ratio:
            new_width = paper_long
            new_height = paper_long / image_ratio
        else:
            new_width = paper_short * image_ratio
            new_height = paper_short
        return new_width, new_height
