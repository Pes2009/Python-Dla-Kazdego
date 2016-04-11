# Leniwe przyciski dwa
# demonstruje uzycie klasy w programie wykorzystujacym Tkinter

from tkinter import *

class Aplikacja(Frame):
	"""Aplikacja oparta na GUI z trzema przyciskami. """
	def __init__(self, master):
		"""incjalizuj ramke"""
		super(Aplikacja, self).__init__(master)
		self.grid()
		self.stworz_widget()

	def stworz_widget(self):
		"""utworz trzy przyciski, ktore nic nie robia. """
		# otworz pierwszy przycisk
		self.bttn1 = Button(self, text = "nic nie robie")
		self.bttn1.grid()

		# otworz drugi przycisk
		self.bttn2 = Button(self, text = "Ja rowniez")
		self.bttn2.grid()

		#otworz trzeci przycisk
		self.bttn3 = Button(self)
		self.bttn3.grid()
		self.bttn3["text"] = "To samo mnie dotyczy!"



# czesc glowna

root = Tk()
root.title("Leniwe przyciski 2")
root.geometry("215x100")

app = Aplikacja(root)

root.mainloop()