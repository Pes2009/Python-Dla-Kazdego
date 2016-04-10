# gra rpg

# klasa bohatera
class Postac(object):

	def __init__(self, name, lvl=1, exp=0,hp = 100):
		self.name = name
		self.lvl = lvl
		self.exp = exp
		self.hp = hp

	def __str__(self):
		rep = "\nnick = " + self.name
		rep += "\nexperiance = " + str(self.exp)
		rep += "\nlevel = " + str(self.lvl)
		rep += "\nzycie = " + str(self.hp)

		return rep

	def level(self):

		print("moj poziom to ", self.lvl)


	def zycie(self):
		max_zycie = 100 + (self.lvl * 5)
		self.max_zycie = max_zycie
		poziom_zycia = self.hp
		self.poziom_zycia = poziom_zycia
		print("max zycie to:", max_zycie)
		print("\naktualne zycie to ",poziom_zycia)


	def expi(self,exp):

		self.exp += exp
		if self.exp <= 100:
			self.lvl = 2
		elif self.exp <= 200:
			self.lvl = 3
		
		elif self.exp <= 800:
			self.lvl = 4
		elif self.exp <= 1000:
			self.lvl = 5
		elif self.exp <= 1200:
			self.lvl = 6
		elif self.exp <= 2000:
			self.lvl = 7
		elif self.exp <= 2800:
			self.lvl = 8
		elif self.exp <= 4000:
			self.lvl = 9
		elif self.exp <= 5500:
			self.lvl = 10
		print("moj exp to ", self.exp)

	def  ciosy(self):
		self.poziom_zycia = poziom_zycia - enemy.



char = Postac("Ziom")

print(char)

char.expi(100)

print(char)

char.expi(100)


print(char)




char.zycie()


class Smok(object):
	"""smok"""
	def __init__(self,atak = 50, hp = 1000):
		self.atak = atak
		self.hp = hp

	def ogien(self)



input("\n\nAby zakończyć program, naciśnij klawisz Enter.")