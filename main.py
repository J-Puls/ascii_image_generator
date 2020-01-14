#################################################################################
# Ascii_Generator
# Written by Jeff Puls
# 1/14/2020
# 
# This program takes in an image from the user's file system, and then
# generates an image comprised of ASCII characters. The resulting image
# will be displayed in the program window, as well as saved as a .txt
# file in the same directory that it was executed. By default, the image
# is output as a "negative", where as the ASCII characters form the image's
# highlights.
# 
# To output the inverse of this, simply comment out line in the 'optimizeImage'
# function containing "optimizedImg = ImageChops.invert(optimizedImg)"
# 
###################################################################################

import tkinter as tk
from tkinter import Frame
from tkinter import Button
from tkinter import Canvas
from tkinter import Label
import optimize 
import convert
import utils

def processImage():
    print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    canvas = Canvas(back, width=r.winfo_width(), height=r.winfo_height(), highlightthickness=0, bg='black')
    canvas.pack()
    imgfile = utils.getFile()
    print("Processing: ", imgfile)
    
    try:
        print("Resizing...")
        img = utils.resizeImage(imgfile)
        print("Resize successful.")
    except Exception as e:
        print(type(e).__name__ + ":\n", e.args)
        canvas.create_text((r.winfo_width()/2), (r.winfo_height()/2),
            anchor='center',
            font=("Consolas", 16),
            fill='green',
            text='Error: This filetype is not supported.\nPlease reset and try again.',
            justify='center')
        raise
    
    try:
        print("Preparing for ASCII Conversion...")
        optimizedImg = optimize.optimizeImage(img)
        print("Ready to convert.")
    except Exception as e:
        canvas.create_text((r.winfo_width()/2), (r.winfo_height()/2),
            anchor='center',
            font=("Consolas", 16),
            fill='green',
            text='Something went wrong.\nPlease reset and try again.',
            justify='center') 
        raise
    # get dimensions & resolution
    w, h = optimizedImg.width, optimizedImg.height
    res = w * h

        ### Use this to simplify the JPEG ###
    # optimizedImg.save("optimizedImg.jpeg", 'JPEG', quality=150) 
    # optimizedImg = Image.open("optimizedImg.jpeg")

    px = optimizedImg.load()

        ### Use this in conjunction with above option to delete the copy it makes ###
    # import os
    # os.remove("optimizedImg.jpeg")
    try:
        asciiImg = convert.convert(w,h,px)
        print("Finished processing successfully!")
    except Exception as e:
        canvas.create_text((r.winfo_width()/2), (r.winfo_height()/2),
            anchor='center',
            font=("Consolas", 16),
            fill='green',
            text='Something went wrong.\nPlease reset and try again.',
            justify='center') 
        raise

    canvas.create_text((r.winfo_width()/2), ((r.winfo_height()/2)-20), anchor='center', font=("Consolas", 4), fill='green', text=asciiImg)
    
    try:
        print("Saving .txt file...")
        utils.saveAsTxt(asciiImg)
    except Exception as e:
        canvas.create_text((r.winfo_width()/2), (r.winfo_height()/2),
            anchor='center',
            font=("Consolas", 16),
            fill='green',
            text='Something went wrong.\nPlease reset and try again.',
            justify='center') 
        raise
    print("Process complete.")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")

def startGUI():
    global r
    global back
    r = tk.Tk()

    # frame that holds controls
    frame = Frame(master=r, bg='black', height=60)
    frame.pack(fill='x')

    # controls
    getFileBtn = Button(frame, text='Select Image', padx=10, pady=10, fg ='green',bg='black', command=processImage)
    getFileBtn.pack()
    getFileBtn.place(x=50, y=15)
    resetBtn = Button(frame, text='Reset', padx=20, pady=10, fg='red', bg='black', command=resetGUI)
    resetBtn.pack()
    resetBtn.place(x=170, y=15)
    wLabel = Label(frame, text='ASCII Image Generator',padx=15, pady=15, font=("Consolas", 16), fg ='white',bg='black')
    wLabel.pack()

    # window properties
    r.title('ASCII Image Generator')
    r.geometry("1280x720")
    r.state("zoomed")
    r.resizable(1, 1)

    # window background
    back = tk.Frame(master=r,bg='black')
    
    # back.pack_propagate(0) # Don't allow the widgets inside to determine the frame's width / height
    back.pack(fill=tk.BOTH, expand=True)
    
    r.mainloop() 

if __name__ == '__main__':
    def resetGUI():
        r.destroy()
        startGUI()
    startGUI()