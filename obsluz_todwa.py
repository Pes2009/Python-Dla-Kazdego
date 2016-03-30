try:

	num = float(input("\nWprowadz liczbe: "))
except ValueError:
	print("To nie byla liczba!")
else:
	print("\nWprowadziles liczbe ", num)


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")