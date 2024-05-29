from enum import Enum

class Paper(Enum):
    A3 = (297, 420)
    A4 = (210, 297)
    A5 = (148, 210)
    Letter = (215.9, 279.4)
    Legal = (215.9, 355.6)

    @classmethod
    def new_wh_portrait(self, paper, image):
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
        return new_width, new_height

    @classmethod
    def new_wh_landscape(self, paper, image):
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
        return new_width, new_height

if __name__ =='__main__':
    print(Paper.A4.value)
