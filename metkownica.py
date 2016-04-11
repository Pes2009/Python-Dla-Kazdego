# metkownica
# demonstruje uzycie widgedu label w gui

from tkinter import *

# otworz glowne okno

root = Tk()
root.title("Metkownica")
root.geometry("200x50")

# otworz w oknie ramke jako pojemnik na inne widzety
app = Frame(root)

app.grid()

# otworz w rame etykiete
lbl = Label(app, text = "Jestem etykieta!")

lbl.grid()
# utworz petle
root.mainloop()