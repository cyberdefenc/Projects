from tkinter import *
from PIL import Image, ImageTk
import os


mahmudul_root = Tk()
mahmudul_root.title("Image Viewer")
mahmudul_root.geometry("955x944")


image_path = "../Images/2.jpg" 


if not os.path.exists(image_path):
    print("Image file not found:", os.path.abspath(image_path))
else:
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    
    varun_label = Label(mahmudul_root, image=photo)
    varun_label.pack()

    
    varun_label.image = photo


mahmudul_root.mainloop()
