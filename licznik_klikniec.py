# Licznik klikniec
# demonstruje powiazanie zdarzenia z procedura obslugi zdarzen

from tkinter import *

class Aplikacja(Frame):
	"""Aplikacja z Gui, ktora zlicza klikniecia przycisku. """
	def __init__(self, master):
		"""inicjalizuj ramke. """
		super(Aplikacja, self).__init__(master)
		self.grid()
		self.bttn_clicks = 0 # licznik klikniec przycisku
		self.create_widget()

	def create_widget(self):
		"""otworz przycisk, ktory wysiwetla liczbe klikniec """
		self.bttn = Button(self)
		self.bttn["text"] = "Liczba klikniec: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()


	def update_count(self):
		""" zwiekrz licznik klikniec i wyswietl jego nowa wartosc"""
		self.bttn_clicks += 1
		self.bttn["text"] = "Liczba klikniec: " + str(self.bttn_clicks)


# czesc glowna
root = Tk()
root.title("Licznik klikniec")
root.geometry("200x50")

app = Aplikacja(root)


root.mainloop()