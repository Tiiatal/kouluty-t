Sukupuoli = input("Anna sukupuolesi kiitos. ")
if Sukupuoli=="Nainen":
    Hemna = int(input("Anna hemoglobiiniarvosi kiitos. "))
    if 117>Hemna:
        print("Hemoglobiinisi on liian matala.")
    elif 117<=Hemna<175:
        print("Hemoglobiinisi on normaalilla tasolla.")
    elif Hemna>=176:
        print("Hemoglobiinisi on liian korkea.")
if Sukupuoli=="Mies":
    Hemmi=int(input("Anna hemoglobiiniarvosi kiitos. "))
    if 134>Hemmi:
        print("Hemoglobiinisi on liian matala.")
    elif 134<=Hemmi<195:
        print("Hemoglobiinisi on normaalilla tasolla.")
    elif Hemmi>=196:
        print("Hemoglobiinisi on liian korkea.")












