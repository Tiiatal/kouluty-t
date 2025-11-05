def lista(Kokoluku):
    summa=sum(Kokoluku)
    print(summa)
    return summa

Kokoluku=[]
while True:
    koko=int(input("Anna minulle haluamasi määrä kokonaislukuja. Palautan sinulle niiden yhteenlasketun summan. Lukujen kysyminen päättyy, kun annat tyhjän vastauksen. "))
    Kokoluku.append(koko)
    if koko == str(""):
        Kokoluku.remove(str(""))
        lista(Kokoluku)
#en keksi mikä tässä mättää
