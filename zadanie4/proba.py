#odwrotne slowa
# program wyspiuje tekst od konca jaki pod uzytkownik.

#slowo = input("Podaj slowo, a program wypisze je od konca: ")

i = input("Wprowadz slowo: ")

last = len(i)
nowe =""

for w in i:
	last = last - 1
	y =""
	y = (i[last])
	nowe = nowe + y

print (nowe)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")