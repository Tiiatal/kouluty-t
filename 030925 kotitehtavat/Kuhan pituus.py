kuha=int(input("Minkä mittainen kuha on senttimetreissä? "))
if kuha<37:
    print("Laske kuha takaisin veteen, kala on alimittainen. Kuha on", 37-kuha, "senttimetriä liian lyhyt.")
elif kuha>37:
    print("Hienoa! Kuha on täysimittainen ja voit pitää sen!")