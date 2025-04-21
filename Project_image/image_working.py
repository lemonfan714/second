from PIL import Image, ImageOps, ImageFilter
class Image_Editor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()
        self.ext = self.get_extenchion()
    def  my_open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('File not defined')
    def do_bw(self):
        gray_img = ImageOps.grayscale(self.original)
        gray_img.save('gray_pic' + self.ext)
        gray_img.show()

    def get_extenchion(self):
        index = self.filename.rfind('.')
        return self.filename[index:]
    def do_blur(self):
        blured_img = self.original.filter(ImageFilter.BoxBlur(100))
        blured_img.show()
    def do_sharper(self):
        sharp_img = self.original.filter(ImageFilter.SHARPEN)
        sharp_img.show()

img = Image_Editor('../Garbage/Без названия (4).jpg')
img.my_open()
img.do_sharper()
