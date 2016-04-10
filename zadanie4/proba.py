# Najlepsze wyniki
# Demonstruje metody listy
import os
os.system('CLS')
wyniki = []

choice = None
while choice != "0":

	print("Najlepsze Wyniki\n")
	print(
	"""

	0 - zakoncz
	1 - pokaz wyniki
	2 - dodaj wynik 
	3 - usun wynik
	4 - posortuj wynik
	"""
	)

	choice = input("wybierasz: ")

	print()


# zakoncz program
	if choice == "0":
		print("do widzenia. ")
# wypisz tabele najlepszych wynikow
	elif choice == "1":
		print("Najlepsze wyniki. : ")
		for score in wyniki:
			print(score)

	elif choice == "2":
		score =	 int(input("jaki wynik uzyskales? "))
		wyniki.append(score)

# usun wyniik
	elif choice == "3":
		print(wyniki)
		score = int(input("Ktory wynik chcesz usunac?"))
		if score in wyniki:
			wyniki.remove(score) # remove usuwa na podstawie wartosci, nie ma nr ktory jest w liscie
		else:
			print(score, "nie ma na liscie wynikow")
	# sortowanie wynikow
	elif choice == "4":
		wyniki.sort(reverse=True)	

#nieznana opcja
	else:
		print("niestety,", choice, "nie jest prawidlowym wyborem.")
