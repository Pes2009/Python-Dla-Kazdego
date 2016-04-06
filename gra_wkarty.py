# Gra w karty
# demonstruje tworzenie kombinacji obiektow

class Card(object):
	"""Karta do gry"""
	RANKS = ["A","2","3","4","5","6","7","8","9","10","j","Q","K",]

	SUITS = ["c","d","h","s"]

	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		rep = self.rank + self.suit
		return rep 


class Hand(object):
	""" reka - karty w reku gracza"""
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			rep =""
			for card in  self.cards:
				rep += str(card) + " "
		else:
			rep = "<pusta>"
		return rep

	def clear(self):
		self.cards = []

	def add(self, card):
		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)



# czesc glowna

card1 = Card(rank = "A", suit = "c")

print("wyswietlam obiekt klasy (klasa card):")
print (card1)


card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c") 
print("\nWyswietlam reszte obiektow pojedynczo")
print(card2)
print(card3)
print(card4)
print(card5)


my_hand = Hand()
print("\nWyswietlam zawartosc mojej reki przed dodaniem kart")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)

print("\nWyswietlam zawartosc mojej reki po dodaniu 5 kart")
print(my_hand)

your_hand = Hand()

my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nPrzekazuje dwie karty z mojej reki do twojej")
print("twoja reka")
print(your_hand)
print("\n moja reka")
print(my_hand)

my_hand.clear()
print("\nMoja reka po usunieciu kart wyglada twojak : ")
print(my_hand)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
