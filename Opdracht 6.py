# Opdracht 6. Rijbewijs nr 1 (2)
# Vraag de leeftijd van de gebruiker en toon of deze gebruiker mag autorijden.

leeftijd = int(input("Voer je leeftijd in: "))

if leeftijd >= 18:
    print("Je mag autorijden.")
elif leeftijd < 18:
    print("Je mag nog niet autorijden.")