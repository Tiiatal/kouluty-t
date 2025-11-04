def bensiini(gallona):
    litra=3.785*gallona
    print("Bensiini:", litra)
    return litra

gallona=float(input("Anna bensiinin määrä gallonan arvolla. Ohjelma kertoo sinulle paljonko määrä olisi litroina. "))

while gallona>=0:
    bensiini(gallona)
    gallona = float(input("Anna bensiinin määrä gallonan arvolla. Ohjelma kertoo sinulle paljonko määrä olisi litroina. "))
if gallona<0:
    print("Arvoa ei voida muuttaa. Päätetään ohjelma.")

#en ole ihan varma, mutta tää taitaa toimia nyt kuten kuuluu?