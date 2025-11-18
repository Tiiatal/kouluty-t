kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu",
             "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
kuukausi = int(input("Anna minulle haluamasi kuukauden numero. Kerron sinulle tiedon saatuani, mistä vuodenajasta on kysymys.\n"
                     "Huomioithan, että lasken ensimmäiseksi talvikuukaudeksi joulukuun. "))
vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
vastaus = (kuukaudet[kuukausi-1])
print(vastaus)
#nyt se printtaa sentään oikean kuukauden
if kuukausi == 1 :
    print("Talvi")
if 2<=kuukausi<=4:
    print("Kevät")
if 5<=kuukausi<=8:
    print("Kesä")
if 9<=kuukausi<=11:
    print("Syksy")
if 12== kuukausi:
    print("Talvi")


