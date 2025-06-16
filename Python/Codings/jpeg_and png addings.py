from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()
mahmudul_root.geometry("955x944")

image = Image.open("../Images/2.jpg")
photo = ImageTk.PhotoImage(image)

# Display the image in a Label
varun_label = Label(image=photo)
varun_label.pack()

# This line keeps the reference to the image alive
varun_label.image = photo  # 💡 VERY IMPORTANT in some cases

mahmudul_root.mainloop()
