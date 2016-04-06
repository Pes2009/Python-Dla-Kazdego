# dostep swobodny
# demonstruje indeksowanie lancuchow znakow
import random

word = input("warto zmiennej word to: ")
for i in word:
	print (random.choice(word))

print("\n",word)

input("\n\nAby zakonczyc pogram,nacisnij enter.")

