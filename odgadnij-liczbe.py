import random

liczb = random.randint(0, 100,)


liczba = int(input("wybierz liczbe z przedzialu od 1 do 100\t"))
prob = 1

while liczba != liczb:

    if liczba > liczb:
    	print("Twoja liczba jest wieksza, sproboj jeszcze raz")
    elif liczba < liczb:
    	print("Twoja liczba jest mniejsza, sproboj jeszcze raz")
    liczba = int(input("wybierz liczbe z przedzialu od 1 do 100\t"))
    prob += 1
print("brawo zgadles, twoja liczba prob to :", prob,)

input("\n\nAby zakonczyc pogram,nacisnij enter.")
