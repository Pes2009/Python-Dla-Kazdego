# zwierzak z konstruktorem
# demonsturje uzycia kontruktora w klasie

class Kot(object):
	"""wirtualnny kot"""
	def __init__(self):
		print("Urodzil sie nowy zwierzak")

	def talk(self):
		print("jestem nowym zwierzakiem czesc!")

crit = Kot()
crit2 = Kot()

crit.talk()
crit2.talk()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")