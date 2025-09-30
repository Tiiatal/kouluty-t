raja=1
while True:
    tunnus = input("Kirjoita salasana ja käyttäjätunnus: ")
    if tunnus!= "python rules":
        print("Pääsy evätty.")
        raja+=1
        if raja>5:
            print("Kiitos hei")
            break
    if tunnus == "python rules":
        print("Tervetuloa!")
        break
