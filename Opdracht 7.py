# Opdracht 7. Rijbewijs nr 2 (2)
# Vraag de geboortedatum van de gebruiker
# en toon wat deze gebruiker vandaag volgens de Nederlandse wet mag op het gebied van motorrijden.

import datetime
x = datetime.datetime.now()

geboortedatum = int(input("Voer je geboortedatum in in dit format 2022-11-24: "))

if geboortedatum >= x:
    print("Je mag autorijden.")
elif geboortedatum < x:
    print("Je mag nog niet autorijden.")
