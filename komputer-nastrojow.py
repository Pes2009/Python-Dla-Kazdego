# komputer nastrojow
# demonstruje klauzule elif

import random

print("Wyczuwm Twoja energie. Twoje prawdziwe emocje znajduja odbicie na moim ekranie.")
print("jestes...")

mood = random.randint(1, 3)

if mood == 1:
	# szczesliwy
	print ("xD")

elif mood == 2:
	# obojetny
	print("(-.-)")

elif mood == 3:
	print(":(")

else:
	print("Nieprawidlowa wartosc nastroju! ( musisz byc naprawde w zlym humorze).")
input("\n\nAby zakonczyc pogram,nacisnij enter.")