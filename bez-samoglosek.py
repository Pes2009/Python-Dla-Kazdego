program = input("Wprowadz komunikat: ")

nowa_wiadomosc = ""
SAMOGLOSKI = "aeiouy"
print()

for letter in program:
	if letter.lower() not in SAMOGLOSKI:
		nowa_wiadomosc += letter
		print("Zostal utworzony nowy lancuch: ", nowa_wiadomosc )

print("\nTwoj komunikat bez samoglosek to: ", nowa_wiadomosc )





input("\n\nAby zakonczyc pogram,nacisnij enter.")