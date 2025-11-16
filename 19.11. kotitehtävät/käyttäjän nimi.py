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

#olipas ihanan HELPPO! <3 Tuli hyvä mieli, kun tähän meni vain 15 minuuttia tuntien sijaan :)