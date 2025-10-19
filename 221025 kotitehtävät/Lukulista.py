Luvut=[]
while True:
    luvut = str(input("Anna luku kiitos. Jos annat tyhjnä luvun toiminto pysähtyy. "))
    Luvut.append(luvut)
    if luvut == "":
        break

Luvut.sort(reverse=True)
Luvut.remove("")
print(Luvut)

#toimii!