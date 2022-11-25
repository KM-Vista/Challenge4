# Opdracht 11. Vermenigvuldigen (2)
# Vraag de gebruiker om 2 getallen in te voeren. 
# Gebruik een functie om het product uit te rekenen. 
# Toon het resultaat van de functie op het scherm. 
# De functie zelf mag dus niets op het scherm plaatsen.
# https://www.w3schools.com/python/python_functions.asp

getalX = float(input("Voer getal x in: "))
getalY = float(input("Voer getal y in: "))

def functie(getalX, getalY): #functie definieren 
    return getalX * getalY #aangeven wat de functie moet teruggeven
print(functie(getalX, getalY)) #uitkomst van vermenigvuldiging
