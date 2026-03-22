from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.tittle('image')
root.geometry('400x400')

upload = Image.open("img.png")
image = ImageTk.PhotoImage(upload)
label = Label(root, image-image, height-350, width-300)
label.place(x=50, y=0)
label2 = Label(root, text='this is how you add image in tkinter window')
label2.place(x=40, y=360)
root.mainloop()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert", "Stop! virus found.")
    
button = Button(root, text="scan for virus",command=nsg)
button.place(x=40, y=80)
root.mainloop()

# Function to open new (top level) Window
def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.tittle("toplevel")

    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
    top.mainloop()
    l2 = Label(root, text = "This is toplevel Window")
    l2.pack()
    top.mainloop()

    l = Label(root, text = "This is root window")
    btn = Button(root, text = "Click here to open another window", command = topwin)

    l.pack()
    btn.pac()



