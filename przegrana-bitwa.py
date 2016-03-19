# Przegrana bitwa
# Demonstruje przerażającą pętlę nieskończoną

print("Twój samotny bohater jest otoczony przez ogromną armię trolli.")
print("Wielka masa ich zgniłozielonych ciał rozciąga się aż po horyzont.")
print("Bohater wyjmuje miecz z pochwy, gotów do stoczenia swej ostatniej walki.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage
    
    print("Bohater pokonuje złego trolla, " \
          "ale odnosi obrażenia i traci", damage, "punkty zdrowia.\n")

print("Twój bohater walczył dzielnie i pokonał", trolls, "trolli.")
print("Lecz niestety Twój bohater już nie żyje.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

