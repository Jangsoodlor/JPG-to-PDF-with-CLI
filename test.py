import unittest
from paper import Paper

class Image:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

class AspectRatioTest(unittest.TestCase):
    def setUp(self):
        self.test_paper = Paper.A4.value

    def test_square(self):
        image = Image(200, 200)
        p_width, p_height, xp, yp = Paper.new_wh_portrait(self.test_paper, image)
        l_width, l_height, xl, yl = Paper.new_wh_landscape(self.test_paper, image)
        self.assertEqual(self.test_paper[0], p_width)
        self.assertEqual(self.test_paper[0], p_height)
        self.assertEqual(self.test_paper[0], l_width)
        self.assertEqual(self.test_paper[0], l_height)
        self.assertEqual(yl, 0)
        self.assertEqual(xp, 0)

    def test_landscape_slim_image(self):
        image = Image(300, 100)
        new_width, new_height, x, y = Paper.new_wh_landscape(self.test_paper, image)
        self.assertEqual(self.test_paper[1], new_width)
        self.assertEqual(image.width/image.height, new_width/new_height)
        self.assertEqual(x,0)

    def test_landscape_fat_image(self):
        image = Image(300, 400)
        new_width, new_height, x, y = Paper.new_wh_landscape(self.test_paper, image)
        self.assertEqual(self.test_paper[0], new_height)
        self.assertEqual(image.width/image.height, new_width/new_height)
        self.assertEqual(y,0)

    def test_portrait_fat_image(self):
        image = Image(500, 300)
        new_width, new_height, x, y = Paper.new_wh_portrait(self.test_paper, image)
        self.assertEqual(self.test_paper[0], new_width)
        self.assertEqual(image.width/image.height, new_width/new_height)
        self.assertEqual(x,0)

    def test_portrait_slim_image(self):
        image = Image(100, 400)
        new_width, new_height, x, y = Paper.new_wh_portrait(self.test_paper, image)
        self.assertEqual(self.test_paper[1], new_height)
        self.assertEqual(image.width/image.height, new_width/new_height)
        self.assertEqual(y,0)
