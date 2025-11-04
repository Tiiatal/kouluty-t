import random
def nopat():
    luku=random.randint (1,6)
    print(luku)
    return luku
#funktio arpoo nopan silmäluvun ja tulostaa sen
print("Hei heitetään noppaa! Noppaa heitetään niin kauan kunnes nopan silmäluku on 6. Kivoja pelihetkiä!")
luku=nopat()
while luku!=6:
    luku=nopat()

print("Heittäminen loppui, kiitos pelaamisesta!")
#ohjelma näyttäisi nyt toimivan?


