from tkinter import StringVar, Radiobutton, Tk, Label, W, Button


def select():
    frame.config(text="{}".format(radiogroup.get()))


def reset():
    radiogroup.set(None)
    frame.config(text="")


root = Tk()
radiogroup = StringVar()
radiogroup.set(None)

Label(root, text="Choose one fantastic creature:").pack(anchor=W)

Radiobutton(root, text="Dragon", variable=radiogroup,
            value='Dragon', command=select).pack(anchor=W)

Radiobutton(root, text="Phoenix", variable=radiogroup,
            value='Phoenix', command=select).pack(anchor=W)

Radiobutton(root, text="Salamander", variable=radiogroup,
            value='Salamander', command=select).pack(anchor=W)

Radiobutton(root, text="Gnome", variable=radiogroup,
            value='Gnome', command=select).pack(anchor=W)

Radiobutton(root, text="Fay", variable=radiogroup,
            value='Fay', command=select).pack(anchor=W)

Button(root, text="Clean", command=reset).pack()

frame = Label(root)
frame.pack()

root.mainloop()