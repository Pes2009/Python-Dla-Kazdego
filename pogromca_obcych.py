# Pogromca obcych
# Demonstruje współdziałanie  obiektów 

class Player(object):
	"""gracz w grze strzelance"""
	def blast(self, enemy):
		print("Gracz razi wroga.\n")
		enemy.die()

class Alien(object):
	"""obcy w grzze strzelance"""
	def die(self):
		print("Obcy z trudem lapie oddech, 'to juz koniec. Ale wielki koniec...\n" \
			"tak, juz sie robi ciemno. Powiedz moim dwom milionom larw, ze je kochalem...\n" \
			"zegnaj okrutny swiecie.'")


# main

hero = Player()

invander = Alien()

hero.blast(invander)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")