import qrcode
import tkinter as tk
from PIL import Image, ImageTk


url = input("Enter the url or message you want to encode: ")

img = qrcode.make(url)
img.save("PhantomForces.jpg")


window = tk.Tk()
window.title("Generated QR Code")
window.geometry('420x420')

im=Image.open("PhantomForces.jpg")  
photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas()  
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(10, 10, image=photo, anchor='nw')  



window.mainloop()