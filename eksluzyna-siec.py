# eksluzywna siec
#demonstruje operatory logiczne i warunki zlozone

print("\tEksluzyna Siec Komputerowa")
print("\t     Tylko dla Czlonkow!\n")

security = 0

username =""

while not username:
	username = input("Uzytkownik: ")

password = ""
while not password:
	password = input("Haslo: ")

if username == "M.Dawson" and password == "sekret":
	print("Czesc Mike!")
	security = 5
elif username == "S.Meier"and password == "cywilizacja":
	print("Hej, Slid!")
	security = 3
elif username ==  "S.Miyamoto" and password == "mariobros":
	print("Co u Ciebie, Shigeru?")
	security = 3
elif username == "W.Wright" and password == "simsowie":
	print("Jak leci, Will?")
	security = 3
elif username ==  "gosc" or password == "gosc":
    print("Witaj, Gosciu!")
    security = 1
else:
	print("Nieudana proba logowanie, Nie jestes nikim wyjatkowym.\n")

	input("\n\nAby zakonczyc pogram,nacisnij enter.")