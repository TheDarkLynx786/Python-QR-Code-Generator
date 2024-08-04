import qrcode
import tkinter as tk
from PIL import Image, ImageTk






img = qrcode.make("https://www.roblox.com/games/292439477/Phantom-Forces")
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