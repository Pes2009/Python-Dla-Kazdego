# progrm ktory rzuca 100x moneta i podaje ilosc orzelkow i reszt
import random
licznik = 0
moneta = ("orzel", "resztka")
orzel = 0
resztka = 0

while licznik < 100:
	if random.choice(moneta) == "orzel":
		orzel = orzel + 1
	else:
		resztka = resztka + 1
	licznik +=1


print ("Resztek wylosowales: ", resztka, "razy")
print ("Orzelka wylosowales: ", orzel, "razy")

input("\n\nAby zakonczyc pogram,nacisnij enter.")
