# zwierzak z wlasciowoscia
# demonstruje wlasciwosci

class Kot(object):
	"""Wirtualny zwierzak"""
	def __init__(self,name):
		print("urodzil sie nowy zwierzak")
		self.__name = name

	@property
	def name(self):
	    return self.__name

	@name.setter
	def name(self, new_name):
		if new_name == "":
			print("Pusty lancuch znakow nie moze byc imieniem zwierzaczka")
		else:
			self.__name = new_name
			print("udalo sie zmienic imie zwierzaczka ;)")
	def talk(self):
		print("czesc jestem ", self.name)


# czesc glowna

ziom1 = Kot("Pawel")
ziom1.talk()

print("\nimie mojego kota to :", end= " ")
print(ziom1.name)


print("\n teraz sproboje zmienic imie mojego kota na ziomeczek")
ziom1.name = "ziomeczek"

print("\n nowe imie mojego zwierzaczka to,", end=" ")
print(ziom1.name)

print("\n teraz sproboje zmienic nazwe mojego kota na pusty lancuch", end=" ")
ziom1.name = ""


print("\n Imie mojego zwierzaka to ", end=" ")
print(ziom1.name)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

