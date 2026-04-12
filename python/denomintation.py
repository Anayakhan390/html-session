#DENOMINATION CALCULATOR
from tkinter import *
from tkinter messagebox
from PIL import Image, ImageTk

root = Tk()
root.tittle("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox = "ok":
     topwin()

     button1 =Button(
        root,
        text="Let's get started!"
        command=msg,
        bg="brown",
        fg="white"
     )
     button1.pplace(x=269, y=360)

     def topwin():
        top = Toplevel()
        top.tittle("denominations Calculator")
        top.configure(bg="light grey")
        top.geometry("600x350+50=50")

        label = Label(top, text="Enter totala amount", bg="light grey")
        entry = Entry(top)

        lbl = Label(
           top,
           text="Here are number of notes for each denonation",
           bg="Light grey"
        )

        l1 = Label(top, text="2000", bg="light grey")
        l2 = Label(top, text="500", bg="light grey")
        l3 = Label(top, text="100", bg="light grey")

        t1 = entry(top)
        t2 = entry(top)
        t3 = entry(top)

        def calculator():
           try:
               amount = int(entry.get())

               role2000 = amount // 2000
               amount %= 2000

               note500 = amount // 500
               amount %= 500

               note100 = amount // 100

               t1.delte(0, END)
               t2.delte(0, END)
               t3.delte(0, END)

               t1.insert(END, str(note2000))
               t2.insert(END, str(note100))
               t3.insert(END, str(note100))

           except ValueError:
              messagebox.showerror("Error", "Please enter a valid number.")

              btn = Button(
                 top,
                 text="Calculate",
                 command=calculator,
                 bg="brown",
                 fg="white"
              )

              top.mainloop()
              root.mainloop()
              