# prosty zwierzak
# demonsturje podsstawy klasy i obiektu

class Kot(object):
	"""wirtualny pupil"""
	def talk(self):
		print("czesc, jestem egzemplarzem klasy kot.")

# czesc glowny
crit = Kot()
crit.talk()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")