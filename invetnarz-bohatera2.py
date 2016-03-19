#utworz krotke zawierajaca elementy
invetory = ("miecz","zbroja","tarcza","napoj hp")
for item in invetory:
	print(item)
input("\nAby kontynuowac misje,wcisnij enter")
print ("twoj dobytek zawiera ",len(invetory)," elementy.")
input("\nAby kontynuowac misje,wcisnij enter")
print("dozyej dni w ktorym stoczysz walke.")
input("\nAby kontynuowac misje,wcisnij enter")

i = int(input("wprowadz indeks elementu inventarza"))
print(invetory[i])
input("\nAby kontynuowac misje,wcisnij enter")
box = ("zloto", "klejnoty")
print("znajdujesz skrzynia ktora zawiera: ", box,)
input("\nAby kontynuowac misje,wcisnij enter")
print("dodajesz zawartosc skrzynki do swojego plecaka")
invetory += box

print("twoj aktualny plecak zawiera: ", invetory,)
input("\nAby zakonczyc gre,wcisnij enter")

