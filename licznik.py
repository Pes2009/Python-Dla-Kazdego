#licznik
# demonstruje uzycie range() z petla for 

print("liczy od 0 do 9")
for i in range(0,10,1):
	print (i, end=" ") # end =" " to ustala co bedzie przedzielac nasze liczby
print("\n")
print("liczy do 5 od 0 do 45")
for i in range(0,50,5):
	print (i, end=" ")
print("\n")
print("liczy od tylu od 9 do 0")

for dycha in range(10,0,-1):
	print(dycha, end=" ")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")