from tkinter import *
window = Tk()
window.title('Tkinter sample window')
window.geometry('300x300')
greeting = Label(text="Hello user", fg='black', bg='white')
button = Button(text="Click me", bg='black', fg='white')
entry = Entry(fg="yellow", bg="blue", width=50)
greeting.pack()
button.pack()
entry.pack()
frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()
textbox = Text(fg='green', bg='yellow')
textbox.pack()

# window = tk.Tk()

# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row1=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"row {i}\ncolumn {j}")
#         label.pack()

# window.mainloop()

