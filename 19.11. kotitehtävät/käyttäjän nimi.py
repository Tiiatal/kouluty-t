nimet= set()
nimi = input("Anna nimesi kiitos. Jos vastaat tyhjän(painat vain enteriä), ohjelma päättyy. ")
nimet.add(nimi)

while nimi != "":
    nimi = input("Anna nimesi kiitos. Jos vastaat tyhjän(painat vain enteriä), ohjelma päättyy. ")
    nimet.add(nimi)
if nimi == "":
    nimet.remove("")
    print("Tulostan sinulle nyt lisäämäsi nimet.")
print(nimet)

#nyt tää lisää nimet listaan, mutta enpä tiedä millä se testaisi löytyykö ne sieltä myöhemmin