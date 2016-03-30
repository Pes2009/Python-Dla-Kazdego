# gra kolko-krzyzyk
#demonstruje wiele w chuj rzeczy xd
import random


# stale globalne 
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUAREs = 9	


#wyswietl instrukcje gry 
def display():
	"""Wyświetl instrukcję gry."""  
	print(
	"""
	Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
	gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
	ludzkim mózgiem a moim krzemowym procesorem.  

	Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
	Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:

					0 | 1 | 2
					---------
					3 | 4 | 5
					---------
					6 | 7 | 8

	Przygotuj się, Człowieku.  Ostateczna batalia niebawem się rozpocznie. \n
	"""
	)


def ask_yes_no(question):
	"""Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
	response = None
	while response not in ("t", "n"):
		response = input(question).lower()
	return response

# ustalnie kolejnosci ruchu

def kogo_ruch():
	ruch = ["czlowiek","komputer"]
	global KOLEJNOSC
	KOLEJNOSC = random.choice(ruch)
	if KOLEJNOSC == "czlowiek":
		human = X
		komputer = O
	else:
		human = O
		komputer = X
	return komputer,human


	def new_board():
	"""Utwórz nową planszę gry."""
	board = []
	for square in range(NUM_SQUARES):
	board.append(EMPTY)
	return board


def display_board(board):
	"""Wyświetl planszę gry na ekranie."""
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\t", board[3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
	"""Utwórz listę prawidłowych ruchów."""
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves

def winner(board):
	"""Ustal zwyciezce gry"""
	WAYS_TO_WIN = ((0,1,2),
				   (3,4,5),
				   (6,7,8),
				   (0,3,6),
				   (1,4,7),
				   (2,5,8),
				   (0,4,8),
				   (2,4,6))

	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner

	if EMPTY not in board:
		return TIE

	return None

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")