import random
Arpakuutiot=int(input("Kuinka monta arpakuutiota heitetään? "))
summa=0
for i in range(Arpakuutiot):
    luvut = random.randint(1,6)
    summa+=luvut
    #print(luvut)
    #yllä oleva tuloste on tässä, jotta varmistan, että ohjelma toimii oikeasti
print(summa)

