# Gra w karty 3.0
#  demonstruje dziedziczenie -  przeslanianie metod

class Card(object):
	"""Karta do gry"""
	RANKS = ["A","2","3","4","5","6","7","8","9","10","j","Q","K",]

	SUITS = ["c","d","h","s"]

	def __init__(self,rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		rep = self.rank + self.suit
		return rep

class Unprintable(Card):
	"""Karta ktorej ranga i kolor nie sa ujawnione przy jej wyswietleniu"""
	def __str__(self):
		return "<utajniona>"

class Positionable_Card(Card):
	"""Karta ktora moze byc zakryta lub odkryta"""
	def __init__(self, rank, suit, face_up=True):
		super(Positionable_Card, self).__init__(rank, suit)
		self.is_face_up = face_up

	def __str__(self):
		if self.is_face_up:
			rep = super(Positionable_Card, self).__str__()
		else:
			rep = "XX"
		return rep

	def flip(self):
		self.is_face_up = not self.is_face_up



# czesc glowna

card1 = Card("A", "c")
card2 = Unprintable("A", "d")
card3 = Positionable_Card("A", "h")

print("\nWyswietlenie obiektu klasy Card")
print(card1)

print("\nWyswietlenie obiektu klasy Unprintable")
print(card2)

print("\nWyswietlenie obiektu klasy Positionable_Card")
print(card3)

card3.flip()

print("Odwracam stan obiektu klasy Positionable_Card ( odkrycie-zakrycie karty ).")
print(card3)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
