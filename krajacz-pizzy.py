#krajacz pizzy
#demonstruje tworzenie wycinkow lancucha

word = "pizza"

print(
"""
  'Ściągawka' tworzenia wycinków

      0   1   2   3   4   5
      +---+---+---+---+---+ 
      | p | i | z | z | a | 
      +---+---+---+---+---+ 
     -5  -4  -3  -2  -1

"""
)

print("Wprowadź początkowy i końcowy indeks wycinka łańcucha 'pizza'.")
print("Aby zakończyć tworzenie wycinków, w odpowiedzi na monit 'Początek:'\n"
      + "naciśnij klawisz Enter.")

start = None
while start != "":
    start = (input("\nPoczątek: "))
    
    if start:
        start = int(start)

        finish = int(input("Koniec: "))

        print("word[", start, ":", finish, "] to", end=" ")
        print(word[start:finish])




input("\n\nAby zakończyć program, naciśnij klawisz Enter.")