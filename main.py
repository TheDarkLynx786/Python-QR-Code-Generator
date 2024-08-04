import numpy as np
import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def generateCode():
    msg = input("Enter the url or message you want to encode: ")
    print("\nDouble-check to make sure there are no typos!\n")

    img = qrcode.make(msg)
    imageName = "QR_Code.jpg"
    img.save(imageName)

    window = tk.Tk()
    window.title("Generated QR Code - " + msg)
    window.geometry('420x420')

    im=Image.open(imageName)  
    photo=ImageTk.PhotoImage(im)  
    cv = tk.Canvas()  
    cv.pack(side='top', fill='both', expand='yes')  
    cv.create_image(10, 10, image=photo, anchor='nw')  

    window.mainloop()


def readCode():
   print("Open your image file from the dialog")
   window = tk.Tk()
   button = tk.Button(text="Open File", command=processFile)
   button.pack()
   window.mainloop()


def processFile():
    path = filedialog.askopenfilename(title="Open the image file of your QR Code", filetypes=(("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("PNG Files","*.png"), ("All Files", "*")))
    file = open(path, 'rb')
    img = cv2.imread(file.name)
    
    reader = cv2.QRCodeDetector()
    val, points, straight_qrcode = reader.detectAndDecode(img)
    print("Here is the decoded message:\n\n" + val + "\n")
    
    file.close()


choice = input("QR Code Generator/Reader\nEnter '1' to Generate a Code\nEnter '2' to Read a Code >>> ")

match choice:
    case "1": 
        generateCode()
    case "2":
        readCode()
    case _: 
      print("There was an error in input. Please re-run the code.")