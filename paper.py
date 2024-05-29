"""Containts the Paper class"""
from enum import Enum


class Paper(Enum):
    """Contains paper size and methods to resize pictures to fit the paper"""
    A3 = (297, 420)
    A4 = (210, 297)
    A5 = (148, 210)
    LETTER = (215.9, 279.4)
    LEGAL = (215.9, 355.6)

    @classmethod
    def new_wh_portrait(cls, paper, image):
        paper_short = paper[0]
        paper_long = paper[1]
        paper_ratio = paper_short / paper_long
        image_ratio = image.width / image.height
        if image_ratio >= paper_ratio:
            new_width = paper_short
            new_height = paper_short / image_ratio
        else:
            new_width = paper_long * image_ratio
            new_height = paper_long
        margin_x = (paper_short - new_width)/2
        margin_y = (paper_long - new_height)/2
        return new_width, new_height, margin_x, margin_y

    @classmethod
    def new_wh_landscape(cls, paper, image):
        paper_short = paper[0]
        paper_long = paper[1]
        paper_ratio = paper_long / paper_short
        image_ratio = image.width / image.height
        if image_ratio >= paper_ratio:
            new_width = paper_long
            new_height = paper_long / image_ratio
        else:
            new_width = paper_short * image_ratio
            new_height = paper_short
        margin_x = (paper_long - new_width)/2
        margin_y = (paper_short - new_height)/2
        return new_width, new_height, margin_x, margin_y
