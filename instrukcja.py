# Instrukcja
# Demonstruje funkcje tworzone przez programistę

def instructions():

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


# main
print("Oto instrukcja do gry kolko i krzyzyk :")
instructions()
print("Ponownie ta sama instrukcja")
instructions()
print("\nPrawdopodobnie juz zrozumiales.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")