from tkinter import *

root =Tk()

root.geometry("300x300")
root.title("CBS")
f1 = Frame(root, bg="blue", borderwidth=6, relief="sunken")
f1.pack(side="left", fill="y")

f2 = Frame(root, bg="yellow", borderwidth=8, relief="sunken")
f2.pack(side="top", fill="x")

l=Label(f1, text="Hello Project")
l.pack(pady=142)

l=Label(f2, text="Start Project", font="helvetica 12 bold", fg="red")
l.pack()

root.mainloop()