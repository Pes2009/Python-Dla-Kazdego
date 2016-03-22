# program losuje slowa i je wypisuje bez powtorzen

import random 


slowa = ["dupa","upa","ala","mala"]
uzyte = []
for i in slowa:
	slowko = random.choice(slowa)
	while slowko in uzyte:
		slowko = random.choice(slowa)
	uzyte.append(slowko)

print(uzyte)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")    
