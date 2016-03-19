# udzielony-odmowiony
# demonstruje klauzule else
import os

print("Witaj w systemie firmy bezpieczny komputer SA")
print("-- bezpieczenstwo to podstawa naszego dzialania\n")

password = ""

while password != "sekret":
    password = input("Wprowadz haslo: ")
    if password == "sekret":
	    print("Dostep zostl udzielony")
    else:
	    print("odmowa dostepu")

input("\n\nAby zakonczyc pogram,nacisnij enter.")