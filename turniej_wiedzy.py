# gra turniej wiedzy
# gra sprawdza wiedze ogolna ,odczytuje dane z pliku tekstowego

import sys

def open_file(file_name, mode):
	"""otworz plik."""
	try:
		the_file = open(file_name, mode)
	except IOError as e:
		print("Nie mozna otworzyc pliku", file_name, "Program zostanie zakonczony.\n", e)
		input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
		sys.exit()
	else:
		return the_file

def next_line(the_file):
	"""zwroc kolejy wiersz pliku mafia po sformatowaniu go"""
	line = the_file.readline()
	line = line.replace("/", "\n")
	return line


def next_block(the_file):
	"""zwroc kolejny blok danych z pliku mafia.txt"""
	kategoria = next_line(the_file)

	pytanie = next_line(the_file)

	odpowiedzi = []
	for i in range(4):
		odpowiedzi.append(next_line(the_file))

	poprawna = next_line(the_file)
	if poprawna:
		poprawna = poprawna[0]
	wyjasnienia = next_line(the_file)

	return kategoria, pytanie, odpowiedzi, poprawna, wyjasnienia

def witaj(tytul):
	"""fukncja wita gracza"""
	print("\t\t\tWitaj w grze turniej wiedzy!\n")
	print("\t\t\t", tytul ,"\n")



def main():
	otwieracz = open_file("mafia.txt", "r")
	tytul = next_line(otwieracz)
	witaj(tytul)
	score = 0
	# pobierz pierwszy blok 
	kategoria, pytanie, odpowiedzi, poprawna, wyjasnienia = next_block(otwieracz)

	while kategoria:
		print(kategoria)
		print(pytanie)
		for i in range(4):
			print("\t", i + 1, "-", odpowiedzi[i])


		# uzyskaj odpowiedz
		odp = input("Podaj poprawna odpowiedz\t")
		if odp == poprawna:
			print("brawo udalo Ci sie, zdobywasz 10 pk")
			score += 10
		else:
			print("zla odpowiedz, zdobywasz 0 pkt")
		print(wyjasnienia)
		print("wynik: ", score, "\n\n")

		# pobieram kolejny blok

		kategoria, pytanie, odpowiedzi, poprawna, wyjasnienia = next_block(otwieracz)

	otwieracz.close()
	print("to bylo ostatnie pytanie smieszku hehe.\n")
	print("twoj wynik to : ", score)
		
main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")