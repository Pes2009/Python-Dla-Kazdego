# Zamarynuj to
# demonstruje marynowanie i  odkladanie danych na polke

import pickle, shelve

print("Marynowanie list.")

odmiana = ["lagodny","pikatny","kwaszony"]
krztalt = ["caly","krojony","w plasterki"]
marka = ["Dawtona","Klimex","Vortumnus"]


f = open("pikle1.dat", "wb")
pickle.dump(odmiana, f)
pickle.dump(krztalt, f)
pickle.dump(marka, f)
f.close()

print("\nOdmarynwanie list.")
f = open("pikle1.dat", "rb")
odmiana = pickle.load(f)
krztalt = pickle.load(f)
marka = pickle.load(f)

print(odmiana)
print(krztalt)
print(marka)
f.close()

print("\nOdkladanie list na polke.")
s = shelve.open("pikle2.dat")
s["odmiana"] = ["lagodny","pikatny","kwaszony"]
s["krztalt"] = ["caly","krojony","w plasterki"]
s["marka"] = ["Dawtona","Klimex","Vortumnus"]

s.sync() # upewnij sie , ze  dane zostaly zapisane


print("\nPobiernie list z polki")
print("marka - ", s["marka"])
print("krztalt - ", s["krztalt"])
print("odmiana - ", s["odmiana"])
s.close()


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")