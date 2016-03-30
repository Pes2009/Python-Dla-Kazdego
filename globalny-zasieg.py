# Globalny zasieg
# Demonstruje zmienne globalne

def read_global():
	print("Wartosc zmiennej value odczytana wewnatrz funckji zakresu lokalnego",
		"\nFunkcji read_global() wynosi:", value)


def shadow_global():
	value = -10
	print("wartosc zmiennej value wewnatrz zakresu lokalnego ",
		"\nfunkcji shadow_global() wynosi: ", value )


def change_global():
	global value
	value = 10
	print("wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
		"\nFunkcji change_global() wynosi: ", value )

# glowna czesc programu
#  value jest  zmienna globalna, poniewaz jestesmy teraz w zakresie globalnym

value = 5
print("W zakresie globalnym wartosc zmiennej value zostala ustawiona na: ", value, "\n")


read_global()
print("Po powrocie do zakresu globalnego wartość zmiennej value nadal wynosi:", value,
      "\n")

shadow_global()
print("Po powrocie do zakresu globalnego wartość zmiennej value nadal wynosi:", value,
      "\n")

change_global()
print("Po powrocie do zakresu globalnego okazuje się, że wartość zmiennej value",
      "\nzmieniła się na:", value)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

