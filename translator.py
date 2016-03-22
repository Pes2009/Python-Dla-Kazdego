# translator slangu komputerowego
# Demonstruje uzywanie slownikow
geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nie znaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących jakiejś osoby.",
        "Keyboard Plaque" : "(skojarzone z kamieniem nazębnym)zanieczyszczenia nagromadzone w klawiaturze komputera.",
        "Link Rot" : "(obumieranie linków) proces, w  wyniku którego linki do stron WWW stają się nieaktualne.",
        "Percussive Maintenance" : "(konserwacja perkusyjna)naprawa urządzenia elektronicznego przez stuknięcie.",
        "Uninstalled" : "(odinstalowany) zwolniony z pracy;  termin szczególnie popularny w okresie bańki internetowej."}  
wybor = None
while wybor != "0":
	print("Translator slangu komputerowego\n")
	print(
		"""
		0 - zakoncz
		1 - znajdz termin
		2 - dodaj nowy termin
		3 - zmien definicje terminu
		4 - usun termin
		"""
		)
	wybor = input("wybierasz: ")
	# konczenie programu
	if wybor == "0":
		print("Dowidzenia.")
    # pobierz definicje
	elif wybor == "1":
		for i in geek
:			print (i)
		termin = input("Jaki termin mam przetlumaczyc? ")
		if termin in geek:
			definicja = geek[termin]
			print ("\n", termin, "oznacza ", definicja)

		else:
			print("\nNiestety nie znam terminu,", termin)
    # dodaj pare termin-definicja
	elif wybor == "2":
		termin = input("Jaki termin mam dodac? ")
		if termin not in geek:
			definicja = input("Podaj definicje terminu: ")
			geek[termin] = definicja

	#  zmiana definicji istejacego terminu
	elif wybor == "3":
		termin = input("Podaj termin ktory chcesz zmienic")
		if termin in geek:
			definicja = input("podaj nowa definicje: " )
			geek[termin] = definicja
			print("\nTermin", termin, "został przedefiniowany.")
		else:
			print("\nTen termin nie istnieje! Spróbuj go dodać.")
    # usuniecie pary termin-definicja
	elif wybor == "4":
		termin = input("Podaj termin ktory chcesz usunac. ")
		if termin in geek:
			del greek[termin]
			print("\nOk termin zostal usuniety")
		else:
			print("\nNie moglem usunac terminu", termin, "poniewaz nie odnalazlem go!")
    # nieznana opcja
	else:
		print("\nNiestety,", choice, "to nieprawidłowy wybór.")
  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")    








