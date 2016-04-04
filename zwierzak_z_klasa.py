# zwierzak z klasa
# demonstruje metody statyczne i atrybuty klasy a nie obiektu danego

class Kot(object):
	"""wirtualny pupil"""
	total = 0

	@staticmethod
	def status():
		print("\n ogolna liczba zwierzakow wynosi", Kot.total)


	def __init__(self,name):
		print("Urodzil sie zwierzak!")
		self.name = name
		Kot.total += 1


#czesc glowna 
print("Uzyskiwanie dostepy do atrybutu klasy Kot.total:", end=" ")
print(Kot.total)

print("\n tworzenie zwierzakow.")
ziom1 = Kot("Zwierzzak 1")
ziom2 = Kot("Zwierzzak 2")
ziom3 = Kot("Zwierzzak 3")

Kot.status()

print("\n Uzyskiwanie dostep do atrybutu klasy poprzez obiekt", end= " ")
print(ziom1.total)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
