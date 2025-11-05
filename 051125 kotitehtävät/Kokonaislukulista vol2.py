def lista(luvut):
    for luvut in annetut[:]:
        if luvut%2==0:
            annetut.remove(luvut)
    print(luvut)
    return luvut

annetut=[]

luvut=int(input("Anna lista kokonaislukuja. "))
annetut.append(luvut)
lista(luvut)

#en saa tehtyä tästä kuin yhden numeron mittaisena toimivan