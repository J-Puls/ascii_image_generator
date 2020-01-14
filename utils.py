from PIL import Image, ImageOps
from tkinter import filedialog

def getFile():
    fn =  filedialog.askopenfilename(initialdir = "C:\Desktop",
            title = "Select file",
            filetypes = (("jpeg files","*.jpg"),
                        ("png files", "*.png"),
                        ("all files","*.*")))
    return fn

def resizeImage(imgfile):
    img = Image.open(imgfile).resize((150, 150)).rotate(90)
    img = ImageOps.flip(img)
    return img

def saveAsTxt(data):
    filename = 'ASCII_pic.txt'
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)
    f.close()
    print(".txt file saved as", filename)

