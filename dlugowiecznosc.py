# Długowiecznosc
# demonstruje widgety Text i Entry oraz menager ukladu Grid

from tkinter import *

class Aplikacja(Frame):
	"""Aplikacja GUI ktora  moze ujawnic sekret. """
	def __init__(self , master):
		"""inicjaliuzj ramke """
		super(Aplikacja, self).__init__(master)
		self.grid()
		self.create_widget()

	def create_widget(self):
		""" utworz widgety typu Button, Text I Entry. """
		# utworz etykiete z instrukcja
		self.inst_lbl = Label(self, text = "Wprowadz haslo do sekretu dlugowiecznosci")
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

		# utworz etykiete do hasla
		self.pw_lbl = Label(self, text = "Haslo:" )
		self.pw_lbl.grid(row = 1, column = 0, sticky = W)

		# utworz widget Entry do przyjecia hasloa
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row = 1, column = 1, sticky = W)

		# utworz przycisk 'Akceptuj'
		self.submit_bttn = Button(self, text = "Akceptuj", command = self.reveal)
		self.submit_bttn.grid(row = 2, column = 0, sticky = W)


		# utworz widget Text do wyswietlenia komunikatu
		self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
		self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		"""wyswietl komunikat zalezny od poprawnosci hasla. """
		contents = self.pw_ent.get()

		if contents == "sekret":
			message = "Oto tajemny przepis na dozycie 100lat: dozyj 99 lat," \
					  "a potem badz BARDZO ostrozny."
		else:
			message = "TO nie jest poprawne haslo, wiec nie moge sie z Toba podzielic moim sekretem"

		self.secret_txt.delete(0.0, END)
		self.secret_txt.insert(0.0, message)

#czesc glowna

root = Tk()
root.title("Dlugowiecznosc")
root.geometry("300x150")

app = Aplikacja(root)

root.mainloop()