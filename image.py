import PIL
from PIL import Image


class ImageFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.image = self.SetImage()
        self.x, self.y = self.image.size

    def SetImage(self):
        image = PIL.Image.open(self.file_path, 'r', None)
        return image

