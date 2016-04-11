# Leniwe przyciski
# Demonstruje tworzenie przyciskow

from tkinter import *

# otworz okno glowne
root = Tk()
root.title("Leniwe przyciski")
root.geometry("200x100")

# otworz ramke w oknie na inne widgedy

app = Frame(root)
app.grid()

# utworz w ramce przycisk
bttn1 = Button(app, text = "Nic nie robie!")
bttn1.grid()

# utworz w ramce drugi przycisk
bttn2 = Button(app)
bttn2.grid()

bttn2.configure(text = "Ja rowniez!")

# utworz trzeci przycisk w ramce
bttn3 = Button(app)
bttn3.grid()

bttn3["text"] = "To samo mnie dotyczy!"

root.mainloop()