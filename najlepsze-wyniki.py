# Najlepsze wyniki 2.0
# Demonstruje metody listy

wyniki = []

choice = None
while choice != "0":

	print("Najlepsze Wyniki\n")
	print(
	"""

	0 - zakoncz
	1 - pokaz wyniki
	2 - dodaj wynik 

	"""
	)

	choice = input("wybierasz: ")

	print()


# zakoncz program
	if choice == "0":
		print("do widzenia. ")
# wypisz tabele najlepszych wynikow i sortuje odrazu
	elif choice == "1":	
		print("Najlepsze wyniki. : \n")
		print("GRACZ\WYNIK")
		for entry in wyniki:
			wynik, imie = entry
			print(imie, "\t", wynik)

	elif choice == "2":	
		imie =input("wprowadz swoj nick: ") 
		wynik = int(input("jaki wynik uzyskales? "))
		entry = (wynik, imie)
		wyniki.append(entry)
		wyniki.sort(reverse=True)
#nieznana opcja
	else:
		print("niestety,", choice, "nie jest prawidlowym wyborem.")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")