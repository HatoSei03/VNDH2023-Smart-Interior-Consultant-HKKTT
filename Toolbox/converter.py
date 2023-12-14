import os
from PIL import Image

def convert(jpg, png):
    try:
        with Image.open(jpg) as img:
            img = img.convert('RGB')
            img.save(png, 'PNG')
            print(f"Image successfully converted and saved as {png}")
            os.remove(jpg)
    except IOError as e:
        print(f"An error occurred when converting {jpg}: {e}")

def convertAll(folderPath):
    for fileName in os.listdir(folderPath):
        if fileName.lower().endswith('.jpg'):
            jpg = os.path.join(folderPath, fileName)
            png = os.path.join(folderPath, os.path.splitext(fileName)[0] + '.png')
            convert(jpg, png)

fold = '../img/'
convertAll(fold)