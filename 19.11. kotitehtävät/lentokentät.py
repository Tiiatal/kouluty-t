kentat = set()
kysymys=input("Hei ja tervetuloa. Haluatko syöttää uuden lentokentän tiedon, hakea jo syöttämäsi kentän tunnuksen vai lopettaa tämän ohjelman käytön? ")
while kysymys == "Syötä uusi tieto":
    kysymys1 = input("Anna uuden lentokentän tunnus ja nimi. ")
    kentat.add(kysymys1)
    print(kentat)
    kysymys = input("Haluatko syöttää uuden lentokentän tiedon, hakea jo syöttämäsi kentän tunnuksen vai lopettaa tämän ohjelman käytön? ")
if kysymys == "Hae":
    print(kentat)
    kysymys = input("Haluatko syöttää uuden lentokentän tiedon, hakea jo syöttämäsi kentän tunnuksen vai lopettaa tämän ohjelman käytön? ")
if kysymys == "Lopeta":
    print("Selvä, ohjelma lopetettu.")
print("Hyvää päivän jatkoa!")

#nyt 16.11. klo 19:03 ohjelma kysyy aina uudelleen mitä käyttäjä haluaa tehdä. Kaikki toiminnot toimivat ja jo lisätyt tiedot pysyvät muistissa.
#seuraavaksi pitää miettiä miten ohjelma tarjoaisi koodia vastaavan kentän nimen?
