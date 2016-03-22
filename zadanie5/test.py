#Kreator postaci
# 30 pkt do rozdania do  4  cech, mozna dodawac i odejmowac ( cofac)


pkt = 30

postac = {"sila":0, "zycie":0,"zrecznosc":0,"obrona":0}

print(postac)

choice = None

while choice != "0":
	print("Witam w kreatorze postaci\n na start masz 30 pkt do rozdaniach do 4 cech, oto one\n")
	print(
	"""
	0 - wyjscie z gry
	1 - sila
	2 - zycie
	3 - zrecznosc
	4 - obrona 
	"""
	)

	choice = input("Wybierz ceche ktora chcesz ulepszyc: ")

	if choice == "0":
		print("Dowidzenia.")

	elif choice == "1":
		if pkt == 0:
			print("wykorzystane wszystkie pkt")
		else:
			print("dodales 1 pkt do sily\n")
			punkty = 1
			pkt = pkt - punkty
			postac["sila"] += 1
			print(postac)


	elif choice == "2":
		if pkt == 0:
			print("wykorzystane wszystkie pkt")
		else:
			print("dodales 1 pkt do zycia\n")
			punkty = 1
			pkt = pkt - punkty
			postac["zycie"] += 1
			print(postac)


	elif choice == "3":
		if pkt == 0:
			print("wykorzystane wszystkie pkt")
		else:
			print("dodales 1 pkt do zrecznosc\n")
			punkty = 1
			pkt = pkt - punkty
			postac["zrecznosc"] += 1
			print(postac)

	elif choice == "4":
		if pkt == 0:
			print("wykorzystane wszystkie pkt")
		else:

			print("dodales 1 pkt do obrona\n")
			punkty = 1
			pkt = pkt - punkty
			postac["obrona"] += 1
			print(postac)
			print(pkt)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")  