# zwierzak z atrybutem
# demonsturje uzycie atrybow

class Kot(object):
	""" zwierzak z atrybutem"""
	def __init__(self,name):
		print("Urodzil sie nowy zwierzak")
		self.name = name

	def __str__(self):
		rep = "obiekt klasy Kot\n"
		rep += "name: " + self.name + "\n"
		return rep

	def talk(self):
		print("czesc , jestem ", self.name, "\n")

# czesc glowna

ziom1 = Kot("Reksio")
ziom1.talk()

ziom2 = Kot("pucek")
ziom2.talk()

print("wyswietlenie obiektu ziom1:")
print(ziom1)

print("Bezposrednie wyswietlenie wartosci atrybutu ziom1.name:")
print(ziom1.name)



input("\n\nAby zakończyć program, naciśnij klawisz Enter.")