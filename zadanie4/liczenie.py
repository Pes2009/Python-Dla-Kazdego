poczatek = int(input("Podaj pierwsza wartosc poczatkowa: "))
koniec = int(input("podaj wartosc koncowa: "))
krok = int(input("Podaj co ile program ma liczyc: "))

end = koniec + 1

for i in range(poczatek, end, krok):
	print (i)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")