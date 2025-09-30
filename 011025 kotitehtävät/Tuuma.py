mitta=2.54
Tuuma = 0
while True:
    kysy=(int(input("Anna tuumamäärä, jonka haluat minun muuttavan senttimetreiksi. ")))
    if kysy*mitta<=0:
        print("Arvoa ei voida muuttaa")
        break
    print("Antamasi arvo on", kysy * mitta, "senttimetriä.")






