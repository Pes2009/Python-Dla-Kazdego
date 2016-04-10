# komputer zgaduje moja liczbe z przedzial od 1 do 100

# wybieram liczbe
# komputer zawsze wybiera liczbe 2 razy mniejsza od maximum
# jesli wieksza to wybiera z wiekszych , jesli mniejsza to z mniejszych

import random

liczba = 55
print(liczba)

i= 0
prob = 1
najwieksza = 100
najmniejsza = 0
najwieksza1 = 100
lista = [50]

zgaduj = 50

while zgaduj != liczba:

	if zgaduj == liczba:
		print("komputer zgadl, za pierwszym razem. Dobry jest ;).")
	elif zgaduj < liczba:
		print("Komputer podal za mala liczbe.")
		prob += 1
		if zgaduj == 50:
			zgaduj = (int(zgaduj) + 25)
			zgaduj = int(zgaduj)
			najmniejsza = 50
			lista.append(zgaduj)
		else:
			najmniejsza = int(zgaduj)
			zgaduj = (int(zgaduj) + int(najwieksza)) /2
			zgaduj = int(zgaduj)
			lista.append(zgaduj)


	else:
		print("liczba komputera jest zbyt wysoka.")
		prob += 1
		if najmniejsza > 0:
			najwieksza = int(zgaduj)
			zgaduj = (int(zgaduj) + int(najmniejsza))/2
			zgaduj = int(zgaduj)
			lista.append(zgaduj)
		else:
			najwieksza = int(zgaduj)
			zgaduj = int(zgaduj/2)
			lista.append(zgaduj)


print("szukana liczba to ", liczba)
print("licz prob to",prob)
print("najwieksza to ",najwieksza)
print("najmniejsza to ", najmniejsza)

print("lista prob komputera ", lista)

input("\n\nAby zakonczyc pogram,nacisnij enter.")

