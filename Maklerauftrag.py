raumliste = {}
fortfahren = "y"
gesamtFlaeche = 0
while fortfahren == "y":
    print('Bitte geben Sie das Zimmer an, welches Sie gerade messen:')
    raumBezeichnung = str(input())
    print('Bitte geben Sie die Länge der ersten Wand in Metern an:')
    ersteWand = float(input())
    print('Bitte geben Sie die Länge der zweiten Wand in Metern an:')
    zweiteWand = float(input())
    raumGroesse = ersteWand * zweiteWand
    gesamtFlaeche = gesamtFlaeche + raumGroesse
    print(raumBezeichnung, raumGroesse)
    print('Wollen Sie ein weiteres Zimmer messen? Falls ja, geben Sie "y" ein')
    fortfahren = input()
gesamtFlaeche = round(gesamtFlaeche, 2)
print(gesamtFlaeche)