# zyczenia urodzinowe
# demonstruje argumenty nazwane  i domyslne wartosci parlamentow

# parlamenty pozycyjne
def urodziny(imie, wiek):
	print("Szczesliwych urodzin", imie, "!", "masz juz", wiek, "lat\n")

# parametry z wartosciami domyslnymi

def urodziny2(imie = "Janusz", wiek = 5):
	print("Szczesliwych urodzin", imie, "!", "masz juz", wiek, "lat\n")

urodziny("Janusz", 5)
urodziny(5, "Janusz")
urodziny(imie = "Janusz", wiek = 5 )
urodziny(wiek = 5, imie = 'Janusz')

urodziny2()
urodziny2(imie = "Katarzyna")
urodziny2(wiek = 12)
urodziny2(imie = "Katarzyna", wiek = 12)
urodziny2("Katarzyna", 12)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")