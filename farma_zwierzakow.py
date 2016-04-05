# farma zwierzakow

import random

class Farma(object):
	"""wirtualna farma zwierzakow"""
	def __init__(self,name,hungry,happy):
		self.name = name
		self.hungry = hungry
		self.happy = happy

	def __str__(self):
		rep = "obiekt klasy Kot\n"
		rep += "name: " + self.name + "\n"
		return rep

	def __pass_time(self):
		self.hungry += 1
		self.happy += 1

	@property
	def mood(self):
		poziom_glodu = self.hungry
		poziom_happy = self.happy
		self.poziom_happy = poziom_happy
		self.poziom_glodu = poziom_glodu
		if poziom_glodu < 5:
			animal = "najedzony"
		elif poziom_glodu < 10:
			animal = "troszke glodny"
		elif poziom_glodu < 15:
			animal = "głodny"
		else:
			animal = "glodny na maxa"

		if poziom_happy < 5:
			animalo = "szczesliwy"
		elif poziom_happy < 10:
			animalo = "ehh moze byc"
		elif poziom_happy < 15:
			animalo = "jestem zly!"

		else:
			animalo = "zly na maxa !!!"

		znacznik = animal + " oraz  " + animalo

		return znacznik
		


	def talk(self):
		print("czesc, nazywam sie : ", self.name, " i jestem ", self.mood, "\n")
		print("poziom smutku ")
		print(self.poziom_happy, "\n")
		print("poziom glodu ")
		print(self.poziom_glodu)
		self.__pass_time()

	def eat(self,food = 12):
		while food > 10:

			food = int(input("ile posilkow chcesz nam dac?"))
			if food > 10:
				print("za duzo")
			else:
				print("mniam, mniam dziekujemy!")
				self.hungry -= food
				if self.hungry < 0:
					self.hungry = 0
				self.__pass_time
	def play(self, zabawa = 12):

		while zabawa > 10:
			zabawa = int(input("jak dlugo chcesz sie bawic ze zwierzaczkiem?"))
			if zabawa > 10:
				print("zbyt wiele godzin ,wybierz mniejsza liczbe")
			else:

				print("oo jak fajnie!")
				self.happy -= zabawa
				if self.happy < 0:
					self.happy = 0
				self.__pass_time


def main():


	zwierzak_name = input("jakie imie dla 1? ")
	zwierzak1 = Farma(name = zwierzak_name, hungry = random.randrange(0,10), happy = random.randrange(0,10))
	zwierzak_name = input("jakie imie dla 2? ")
	zwierzak2 = Farma(name = zwierzak_name, hungry = random.randrange(0,10), happy = random.randrange(0,10))
	zwierzak_name = input("jakie imie dla 3? ")
	zwierzak3 = Farma(name = zwierzak_name, hungry = random.randrange(0,10), happy = random.randrange(0,10))


	choice = None
	while choice != "0":
		print \
		("""
		opiekun farmy
		0 - zakoncz
		1 - sluchaj zwierzat
		2 - nakarm
		3 - baw sie
		4 - pokaz status zwierzat
		""")

		choice = input("wybierasz: ")
		print()

		# wyjdz z petli
		if choice == "0":
			print("do widzenia")

		elif choice == "1":
			zwierzak1.talk()
			zwierzak2.talk()
			zwierzak3.talk()
			


		elif choice == "2":
			zwierzak1.eat(),zwierzak2.eat(),zwierzak3.eat()

		elif choice == "3":
			zwierzak1.play()
			zwierzak2.play()
			zwierzak3.play()

		elif choice == "4":
			print(zwierzak1)
			print(zwierzak2)
			print(zwierzak3)
		else:
			print("\n nie wybrales zadnej opcji, sproboj jeszcze raz")

main()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

