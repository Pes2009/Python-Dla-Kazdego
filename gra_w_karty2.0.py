# Gra w karty 2.0
# demonstruje dziedziczenie 

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


class Deck(Hand):
	"""Talia kart do gry"""

	def populate(self):
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit))

	def shuffle(self):
		import random
		random.shuffle(self.cards)


	def deal(self, hands, per_hand = 1):
		for rounds in range(per_hand):
			for hand in  hands:
				if self.cards:
					top_card = self.cards[0]
					self.give(top_card, hand)
				else:
					print("Nie moge dalej rozdawac, zabraklo kart!")


# czesc glowna

deck1 = Deck()
print("utworzylem nowa talie: ")
print(deck1)
print("\n lecz jest ona poki co pusta...")

deck1.populate()

print(deck1)
print("\n Teraz talia jest pelna ")

deck1.shuffle()

print("\n potasowalem talie")
print(deck1)

my_hand = Hand()
your_hand = Hand()

hands = [my_hand, your_hand]

deck1.deal(hands, per_hand = 5)

print("\nMoja reka posiada nastepujace karty")
print(my_hand)

print("\nTwoja reka posiada nastepujace karty")
print(your_hand)

print("W talii zostalo : ", len(deck1.cards), "kart")
print(deck1)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")