# Opdracht 15. Wie mag er beginnen? (2)
# Vraag hoeveel spelers er zijn. 
# Vraag vervolgens per speler de naam. 
# Laat op het scherm de naam van een willekeurige speler zien. 
# Deze speler mag beginnen. 

import random

aantal = int(input("Hoeveel spelers zijn er in totaal (getal): "))
naam = (input("Voer de naam van de speler in: "))
namenlijst = []
namenlijst.append(naam)

while aantal != len(namenlijst):
    naam = (input("Voer de naam van de speler in: "))
    namenlijst.append(naam)
else: print("Random naam: " + random.choice(namenlijst))