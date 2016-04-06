# gry
# demonstruje tworzenie modulu

class Player(object):
	"""Uczestnik gry"""
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

	def __str__(self):
		rep = self.name + ":\t" + str(self.score)

		return rep

def ask_yes_no(question):
	"""Zadaj pytanie na ktore mozna odpowiedziec tak lub nie"""
	respone = None
	while respone not in ("t", "n"):
		respone = input(question).lower()
	return respone

def ask_number(question, low, high):
	"""popros o podanie liczby z okrelonego zakresu"""
	respone = None
	while  respone not in range(low, high):
		respone = int(input(question))
	return respone

	if __name__ == "__main__":
		print("Uruchomiles ten modul bezposrednio, zamiast go zaimportowc.")

