# prywatny zwierzak
# demonstruje uzycie prywant  atrybutow i metod

class Kot(object):
	"""wirtualny zwierzaczek"""
	def __init__(self,name,mood):
		print("urodzin sie nowy zwierzak!")
		self.name = name # publiczny atrybut
		self.__mood = mood #  atrybut prywatny

	def talk(self):
		print("\nJestem", self.name)
		print("W tej chwili czuje sie", self.__mood, "\n")

	def __private_method(self):
		print("To jest mtoda prywatna.")

	def public_method(self):
		print("To jest metoda publiczna")
		self.__private_method()

# czesc glowna
ziom = Kot(name = "Reksio", mood = "szczesliwy")
ziom.talk()
ziom.public_method()


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

