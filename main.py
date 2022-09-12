import os.path as Path
import sys
import image
import PIL.ImageFont
from PIL import Image


def VerifyFileExists(file_name):
    file_path = "../images/" + file_name
    file_exists = Path.exists(file_path)
    if file_exists:
        print("File Found")
        return file_path
    else:
        print("File NOT Found")
        exit()


file_name = sys.argv[1]
file_path = VerifyFileExists(file_name)

image1 = image.ImageFile(file_path)


