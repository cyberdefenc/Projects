from tkinter import *

root=Tk()

def h1():
    print("Hello")

def h2():
    print("Hello2")

def h3():
    print("Hello3")

def h4():
    print("Hello4")


f1=Frame(root, borderwidth=2, relief="sunken",bg="green")
f1.pack(side='left', anchor='nw')

b1=Button(f1, fg="red", text="Hello Pi", command=h1)
b1.pack(side='left', padx=23)

b2=Button(f1, fg="red", text="Hello Pi", command=h2)
b2.pack(side='left', padx=23)

b3=Button(f1, fg="red", text="Hello Pi", command=h3)
b3.pack(side='left', padx=23)

b4=Button(f1, fg="red", text="Hello Pi", command=h4)
b4.pack(side='left', padx=23)
root.mainloop()

