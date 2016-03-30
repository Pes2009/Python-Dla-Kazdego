#utworz liste zawierajaca elementy

invetory = ["miecz","zbroja","tarcza","napoj hp"]
for item in invetory:
	print(item)
input("\nAby kontynuowac misje,wcisnij enter")
print ("twoj dobytek zawiera ",len(invetory)," elementy.")
input("\nAby kontynuowac misje,wcisnij enter")
print("dozyej dni w ktorym stoczysz walke.")
input("\nAby kontynuowac misje,wcisnij enter")
i = None
try:
	i = int(input("wprowadz indeks elementu inventarza"))
	if i >=4:
		print(invetory[i])
except:
	print("wystapil blad")
input("\nAby kontynuowac misje,wcisnij enter")
box = ("zloto", "klejnoty")
print("znajdujesz skrzynia ktora zawiera: ", box,)
input("\nAby kontynuowac misje,wcisnij enter")
print("dodajesz zawartosc skrzynki do swojego plecaka")
invetory += box

print("twoj aktualny plecak zawiera: ", invetory,)
input("\nAby kontynuowac gre,wcisnij enter")

print("wymieniasz swoj miecz na kusze.")
invetory[0] = "kusza"
print("twoj aktualny inventarz to: ", invetory,)
input("\nAby kontynuowac gre,wcisnij enter")

print("zuzywasz swoje zloto i kejnotow do kupienia kuli do wrozenia")
invetory[4:6] = ["kula do wrozenia"]
print("twoj aktualny inventarz to: ", invetory,)
input("\nAby kontynuowac gre,wcisnij enter")

print("w wielkie bitwie twoja tarcza zostaje zniszczona")
del invetory[2]
print("twoj aktualny inventarz to: ", invetory,)
input("\nAby kontynuowac gre,wcisnij enter")

print("twoja kusza i zbroja zostaly skradzione przez zlodzei.")
del invetory[1],invetory[0]
print("twoj aktualny inventarz to: ", invetory,)
input("\nAby kontynuowac gre,wcisnij enter")