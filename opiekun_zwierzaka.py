# opiekun zwierzaka
# ....

class Kot(object):
	"""wirtualny zwierzak"""
	def __init__(self,name,glod = 0,nuda = 0):
		self.name = name
		self.glod = glod
		self.nuda = nuda

	def __str__(self):
		rep = "obiekt klasy Kot\n"
		rep += "name: " + self.name + "\n"
		return rep


	def __pass_time(self):
		self.glod += 1
		self.nuda += 1

	@property
	def mood(self):

		poziom_nieszczescia = self.glod + self.nuda
		if poziom_nieszczescia < 5:
			m = "szczesliwy"
		elif poziom_nieszczescia <= 10:
			m = "zadowolony"
		elif poziom_nieszczescia <= 15:
			m = "podenerwowany"
		else:
			m = "wsciekly"
		return m

	def talk(self):
		print("nazywam sie", self.name, "i jestem", self.mood, "teraz\n")
		self.__pass_time()
	
	def eat(self, food = 12):
		while food > 10:

			food = int(input("ile jedzonka chcesz dac koteczkowi?"))
			if food > 10:
				print("a duzo jedzonka, chcesz zeby peknal zwierzak?")
			else:		
				print("mniam, mniam dziekuje")
				self.glod -= food
				if self.glod < 0:
					self.glod = 0
				self.__pass_time

	def play(self, zabawa = 12):
		while zabawa > 10:
			zabawa = int(input("jak dlugo chcesz sie bawic ze zwierzaczkiem?"))
			if zabawa > 10:
				print("zbyt wiele godzin ,wybierz mniejsza liczbe")
			else:

				print("oo jak fajnie!")
				self.nuda -= zabawa
				if self.nuda < 0:
					self.nuda = 0
				self.__pass_time

def main():
	zwierzak_name = input("Jak chcesz nazwac swojego pupila? ")
	zwierzak = Kot(zwierzak_name)


	choice = None
	while choice != "0":
		print \
		("""
		opiekun zwierzaka
		0 - zakoncz
		1 - sluchaj zwierzaka
		2 - nakarm
		3 - baw sie
		4 - pokaz status zwierzaka
		""")

		choice = input("wybierasz: ")
		print()

		# wyjdz z petli
		if choice == "0":
			print("do widzenia")

		elif choice == "1":
			zwierzak.talk()

		elif choice == "2":
			zwierzak.eat()

		elif choice == "3":
			zwierzak.play()

		elif choice == "4":
			print(zwierzak)
		else:
			print("\n nie wybrales zadnej opcji, sproboj jeszcze raz")

main()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")





