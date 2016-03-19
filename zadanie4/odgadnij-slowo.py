#program losuje slowo z lity i uzytkownik ma za zadanie odgadnac co to za slowo

import random

WORDS = ("python",'ziom',"dlaczego","ziomeczek","dom")

nowe= random.choice(WORDS)

print (nowe)

dlugosc = len(nowe)

print("Witam Cie w moim programie 'odgadnij slowo'\n")
print("komputer losuje slowo i masz 5 szans zeby je odgadnac\n")
print("za kazdym razem mozesz sie spytac czy dana litera wystepuje w slowie\n")
print("Zaczynamy,a wiec powodzenia!\n")
print("pierwsza litera slowa to: ", nowe[0],"\n")
print("dlugosc slowa to: ", dlugosc, "liter\n")
szansa = 0
while szansa <= 6:
	pyt = input("Spytaj czy litera wystepuje w slowie: ")
	if pyt in nowe:
		print("tak")
	else:
		print("nie")
	szansa = szansa + 1


odp = input("podaj slowo: ")
if odp == nowe:
	print("rawo zgadles slowo! ")
else:
	print("buuu nie zgadles,przegrales")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")