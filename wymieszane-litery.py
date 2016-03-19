# wymieszane litery
# komputer wybiera losowo slowo, a potem miesza jego litery
import random

WORDS = ("python",'ziom',"dlaczego","ziomeczek","dom")

word = random.choice(WORDS)
print (word)

poprawnie = word

# utworz pomieszana wersje slowa
jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print (jumble)


# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")
    
if guess == correct:
    print("Zgadza się! Zgadłeś!\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
