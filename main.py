import numpy as np
import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def generateCode():
    msg = input("_________________________\n\nEnter the url or message you want to encode: ")
    print("\nDouble-check to make sure there are no typos! Resize the window if you have to. Scan the code to check if it's right!\n")
    print("Close the pop-up to exit the program.\n_________________________\n")

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
    print("_________________________\n\nOpen your image file from the pop-up dialog.")
    window = tk.Tk()
    window.title("Open Your Image File")
    window.geometry("300x20")
    button = tk.Button(window, text="Open File", command=processFile)
    button.pack()
    window.mainloop()


def processFile():
    path = filedialog.askopenfilename(title="Open the image file of your QR Code", filetypes=(("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("PNG Files","*.png"), ("All Files", "*")))
    file = open(path, 'rb')
    img = cv2.imread(file.name)
    
    reader = cv2.QRCodeDetector()
    val, points, straight_qrcode = reader.detectAndDecode(img)
    print("\nHere is the decoded message (If your message is empty, it is likely that the image was not a valid QR Code):\n_________________________\n\n\n" + val + "\n\n_________________________\n\nClose the pop-up to exit the program.\n_________________________\n")
    
    file.close()


def run():
    choice = input("\n_________________________\n\nQR Code Generator/Reader\n_________________________\n\n--> Enter '1' to Generate a Code\n--> Enter '2' to Read a Code\n--> ")

    match choice:
        case "1": 
            generateCode()
        case "2":
            readCode()
        case _: 
            print("There was an error in input. Please re-run the code.")
            run()

#Main
run()