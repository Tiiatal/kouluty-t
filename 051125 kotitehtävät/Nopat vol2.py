import random
def nopat(silmäluku):
    for i in range(silmäluku):
        luku=random.randint (0,silmäluku)
    print(luku)
    return luku
#funktio arpoo nopan silmäluvun ja tulostaa sen

silmäluku=(int(input("Millaista noppaa haluat heittää? Kerro haluamasi maksimi silmäluku nopalle. ")))
luku=nopat(silmäluku)
while luku!=silmäluku:
    luku=nopat(silmäluku)

print("Heittäminen loppui, kiitos pelaamisesta!")

#Siis toimiiko tää oikeasti vaan 5 minuutin rakentelun jälkeen täydellisesti? :D