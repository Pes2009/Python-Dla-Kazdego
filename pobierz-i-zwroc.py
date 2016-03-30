# pobierz i zwroc
# demonstruje parametry i wartosci zwrotne

def display(message):
	print(message)


def give_me_five():


	five = 5
	return five

def ask_yes_no(question):
	"""Zadaj pytanie, na ktore mozna podpowiedz tak lub nie"""
	respone = None
	while respone not in ("t","n"):
		respone = input(question).lower()
	return respone

# main
display("To wiadomosc dla Ciebie.\n")

number = give_me_five()
print("oto co otrzymalem z funkcji 	give_me_five()", number)


answer =  ask_yes_no("\nProsze wprowadzic 't' lub 'n': ")
print("dziekuje za wprowadzenie", answer)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")