# analizator komunikato
# demonstruje funkcje len() i operator in

slowo = input("Wprowadz komunikat!: ")
 

print("dlugosc twojego slowa to ", len(slowo))

print("najczesciej wsytepujaca litera w jezyku Polskim to 'a' ")
if "a" in slowo:
    print("W twoim slowie, litera 'a' wystepuje")
else:
	print("niestety nie ma literki 'a' w twoim slowie ")

input("\n\nAby zakonczyc pogram,nacisnij enter.")