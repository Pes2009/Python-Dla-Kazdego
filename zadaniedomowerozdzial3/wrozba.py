# program ktory losuje 1 z 5 przepowiedni z ciasteczka
import random
print("Witam w programie przepowiednia ciasteczkowa")
print("wylosujemy jedna z pieciu przepowiedni uwaga!")
los = random.randint(1, 5)
print (los)

if los == 1:
	print("wylosowales pierwsza przepowiednie")
elif los== 2:
	print("wylosowales druga przepowiednie")
elif los== 3:
	print("wylosowales trzecia przepowiednie")
elif los==4:
	print("wylosowales trzecia przepowiednie")
elif los==5:
	print("wylosowales piata przepowiednie")

input("\n\nAby zakonczyc pogram,nacisnij enter.")