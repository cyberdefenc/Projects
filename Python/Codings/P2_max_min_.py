from tkinter import *

imaginary_tech_root = Tk()

imaginary_tech_root.geometry("644x434")
      # width * height --Geometry is the default size of the application when it opened

imaginary_tech_root.minsize(200,100)
      #width,height -- application can be minimized less than this

imaginary_tech_root.maxsize(1200,988)
      #width,height

shakaib = Label(text="Shakaib is a good boy and this is his GUI")
shakaib.pack()

imaginary_tech_root.mainloop()