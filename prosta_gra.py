# Prosta gra

import gry, random

print("Witam w najprostrzej grze na swiecie!\n")

ponownie = None
while ponownie != "n":
	gracze = []
	num = gry.ask_number(question = "Podaj liczbe graczy (2 - 5)", low = 2, high = 5)

	for i in range(num):
		name = input("Podaj nick ")
		score = random.randrange(100) + 1 
		player = gry.Player(name, score)
		gracze.append(player)

	print("\nOto wyniki gry: ")
	for player in gracze:
		print(player)
	ponownie = gry.ask_yes_no("\nCzy chcesz zagrać ponownie? (t/n): ")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")