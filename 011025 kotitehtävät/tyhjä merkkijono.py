while True:
    luku1 = str(input("Anna luku kiitos. Tyhjä vastaus pysäyttää ohjelman. "))
    luku2 = str(input("Anna luku kiitos. Tyhjä vastaus pysäyttää ohjelman. "))
    luku1!=""
    luku2!=""
    if luku1 =="":
        if luku1>luku2:
           print(" Kiitos, pienin lukusi oli",luku2, "ja isoin lukusi oli", luku1)
        if luku2>luku1:
            print("Kiitos, pienin lukusi oli", luku1, "ja isoin lukusi oli", luku2)
        break
    elif luku2 == "":
        if luku1>luku2:
            print(" Kiitos, pienin lukusi oli", luku2, "ja isoin lukusi oli", luku1)
        if luku2>luku1:
            print("Kiitos, pienin lukusi oli", luku1, "ja isoin lukusi oli", luku2)
        break

#Ei ihan toimi tehtävänannon mukaan, mutta parempaan en pystynyt. En saa samanaikaisesti toimimaan silmukkaa ja if lauseita.
#If lause rikkoo silmukan toistumisen ilman tulostetta, vaikka ei painaisi yhtäkään tyhjää