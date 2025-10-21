luku = int(input("Anna kokonaisluku kiitos, niin kerron sinulle onko kyseessä alkuluku. ")) #kysyy lukua
for i in range(2,luku):
    if luku % i == 0:       #jos luku jaettuna rangen luvulla on 0, kyse ei alkuvusta
        print("Luku ei ole alkuluku.")
        break
else:                   #jos jakojäänne olisi muuta kuin 0 tämän pitäisi tapahtua
    print("Luku on alkuluku!")






#nyt pitäisi toimia!