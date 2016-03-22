# Szubienica
#
# klasyczn gra w szubienice, komputer losowo wybiera slowo,
# a gracz proboje odgadnac jego poszczegolne litery. Jesli gracz
# nie odgarnie w pore calego slowa, maly ludzik zostaje powieszony

import random

# stałe
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

# maxymalna liczba bledow jest o 1 mniejsza niz liczba rysunkow
MAX_WRONG = len(HANGMAN) - 1
# stala slowa
WORDS = ["GRACZ","ZIOM","MARTIN","DUPEK","NADZIEJA","TRAKTORZYSTA"]

word = random.choice(WORDS) # slowo do odgadniecia 


so_far = "-" * len(word)      # kreska zastępuje nieodgadniętą literę

wrong = 0 # liczba nietrafionych liter 

uzyte = [] # slowa juz uzyte w grze

print("Witam w grze szubienica")

while wrong < MAX_WRONG and so_far != word:
	print(HANGMAN[wrong])
	print("\nWykorzystałeś już następujące litery:\n", uzyte)
	print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)

	guess = input("\n\nWprowadź literę: ")
	guess = guess.upper()
    
	while guess in uzyte:
		print("Już wykorzystałeś literę", guess)
		guess = input("Wprowadź literę: ")
		guess = guess.upper()

	uzyte.append(guess)

	if guess in word:
		print("\nTak!", guess, "znajduje się w zagadkowym słowie!")

        # utwórz nową wersję zmiennej so_far, aby zawierała odgadniętą literę
		new = ""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += so_far[i]              
		so_far = new
	else:
		print("\nNiestety literka nie wystepuje w slowie")
		wrong += 1


if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nZostałeś powieszony!")
else:
    print("\nOdgadłeś!")
    
print("\nZagadkowe słowo to", word)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

