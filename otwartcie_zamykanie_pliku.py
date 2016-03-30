# otwarcie i zamykanie plikku
# program demonstruje odczytywanie tekstu z pliku.txt

print("Otwarcie i zamkniecie pliku")
text_file = open("odczytaj_to.txt", "r")
text_file.close()

print("\nOdczytywanie znakow z pliku.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.read(1)) # odczytuje do pierwszego znaku
print(text_file.read(7)) # odczytuje 7 znakow kolejnych !!! (od 2 do 8 ) bo 1 juz wczsniej zostal wczytany
text_file.close()


print("\nOdczytanie calego pliku za jednym razem")
text_file = open("odczytaj_to.txt", "r")
caly_text = text_file
print(caly_text.read()) # odczytuje caly plik
text_file.close()


print("\nOdczytywanie znakow z wiesza")
text_file = open("odczytaj_to.txt", "r")
print(text_file.readline(1))
print(text_file.readline(7))
text_file.close()


print("\nOdczytywanie po jednym wierszu na raz")
text_file = open("odczytaj_to.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()


print("\nWczytanie calego pliku do listy")
text_file = open("odczytaj_to.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
	print(line)
text_file.close()


print("\nPobieranie zawartosci pliku wiersz po wierszu przy uzyciu petli")
text_file = open("odczytaj_to.txt", "r")
for line in text_file:
	print(line)
text_file.close()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
