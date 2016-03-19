#inwentarz bohatera
#demonstruje tworzenie krotek

#otorz pusta krotke
invetory = ()

#potraktuj krotke jako warunek
if not invetory:
	print("nie posiadasz niczego")

input("\nAby kontynuowac misje,wcisnij enter")


#utworz krotke zawierajaca elementy
invetory = ("miecz","zbroja","tarcza","napoj hp")

#wyswietl krotke
print("\nWykaz zawartosci krotki")
print(invetory)

#wyswietl kazdy element krotki
print("elementy twojego wyposazenia")
for i in invetory:
	print(i)

input("\nAby zakonczyc misje,wcisnij enter")