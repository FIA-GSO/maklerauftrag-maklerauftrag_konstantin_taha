class Raum():
    gesamtFlaeche=0
    anzahl=0
    
    def __init__(self, bezeichnung, length, width,ausschnitte):
        
        
        self.bezeichnung=bezeichnung
        self.length=length
        self.width=width
        self.flaeche=length*width
        self.ausschnitte=ausschnitte
        
        for self.element in self.ausschnitte:
            self.flaeche=self.flaeche-self.element.ausschnittsflaeche
        Raum.gesamtFlaeche+=self.flaeche
        Raum.anzahl+=1

    def __str__(self):
        return f"Raum: {self.bezeichnung} | Fläche: {self.flaeche} m²"
    
    def gesamtFlaecheAusgeben():
        return Raum.gesamtFlaeche
    
    def durchschnittFlaeche():
        return Raum.gesamtFlaeche/Raum.anzahl
    
class ausschnitt():
    def __init__(self,length, width):
        self.ausschnittsflaeche=length*width

        
raumListe = []
fortfahren = "y"
while fortfahren == "y":
    print('Bitte geben Sie an welches Zimmer Sie gerade messen:')
    raumBezeichnung = str(input())
    print('Wie viele Ausschnitte hat das Zimmer?')
    anzahlAus = int(input())
    ausschnitte=[]
    
    print("Wie lang ist Wand A des Zimmers (in m)?")
    laengeA=int(input())
    print("Wie lang ist Wand B des Zimmers (in m)?")
    laengeB=int(input())    

    for i in range(0,anzahlAus):
        print(f'Wie lang ist Wand 1 von Ausschnitt {i+1} (in m)?')
        width = int(input())
        print(f'Wie lang ist Wand 2 von Ausschnitt {i+1} (in m)?')
        length = int(input())
        ausschnitte.append(ausschnitt(length, width))

    raumListe.append(Raum(raumBezeichnung,laengeA,laengeB,ausschnitte))
    print()
    print(raumListe[len(raumListe)-1])
    print()
    print('Wollen Sie ein weiteres Zimmer messen? Falls ja, geben Sie "y" ein')
    fortfahren = input()
#gesamtFlaeche = round(, 2)

print()
for raum in raumListe:
    print(raum)
print()
print(f"Gesamtfläche aller Räume: {Raum.gesamtFlaeche} m²")
print(f"Durchschnittsfläche aller Räume: {round(Raum.durchschnittFlaeche(), 2)} m²")
print()