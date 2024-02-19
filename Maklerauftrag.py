raumListe = {}
fortfahren = "y"
gesamtFlaeche = 0
zaehler = 0
while fortfahren == "y":
    print('Bitte geben Sie das Zimmer an, welches Sie gerade messen:')
    raumBezeichnung = str(input())
    print('Hat das Zimmer einen Ausschnitt? Falls ja, geben Sie "y" ein, falls nein, geben Sie "n" ein')
    form = input()
    if form == "n":
        print('Bitte geben Sie die Länge der ersten Wand in Metern an:')
        ersteWand = float(input())
        print('Bitte geben Sie die Länge der zweiten Wand in Metern an:')
        zweiteWand = float(input())
        raumGroesse = ersteWand * zweiteWand
        raumListe[raumBezeichnung] = raumGroesse
    if form == "y":
        print('Bitte geben Sie die Länge der ersten äußeren Wand in Metern an:')
        ersteWand = float(input())
        print('Bitte geben Sie die Länge der zweiten äußeren Wand in Metern an:')
        zweiteWand = float(input())
        print('Bitte geben Sie die Länge der ersten inneren Wand in Metern an:')
        ersteWandInnen = float(input())
        print('Bitte geben Sie die Länge der zweiten inneren Wand in Metern an:')
        zweiteWandInnen = float(input())
        raumGroesse = ersteWand * zweiteWand - ersteWandInnen * zweiteWandInnen
        raumListe[raumBezeichnung] = raumGroesse
    zaehler = zaehler + 1
    gesamtFlaeche = gesamtFlaeche + raumGroesse
    print(raumBezeichnung, raumGroesse)
    print('Wollen Sie ein weiteres Zimmer messen? Falls ja, geben Sie "y" ein')
    fortfahren = input()
gesamtFlaeche = round(gesamtFlaeche, 2)
print(gesamtFlaeche)
print(raumListe)
durchschnittFlaeche = round(gesamtFlaeche/zaehler, 2)
print(durchschnittFlaeche)