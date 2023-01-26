from tkinter import *
root = Tk()
root.title('5 elementos')
chosen = StringVar()
list = Listbox(root)
elements = ["Fuego", "Tierra", "Aire", "Agua", "Vacío"]

list.insert(END, *elements)

list.pack()
label = Label(text="Lista de elementos")
label.pack()
root.mainloop()