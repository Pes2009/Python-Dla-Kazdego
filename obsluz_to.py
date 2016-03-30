	# Obsluz to
# demonstruje obsluge wyjatkow

try:
	num = float(input("Wprowadz liczbe: "))
except ValueError as e:
	print("nie udalo sie leszczu... a python by tak to okreslil")
	print(e)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
# obsluga  kilku typow wyjatkow

print()
for value in (None, "hej!"):
	try:
		print("proba konwersji:", value, "-->", end=" ")
		print (float(value))
	except (TypeError, ValueError):
		print("wystapil jakis blad")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")