# Opdracht 14. Palindroom (2)
# Vraag een woord en laat de gebruiker weten of het ingevoerde woord een palindroom is.

woord = input("Geef een woord in: ") #input van het woord
if woord == woord[::-1]: #woord omdraaien en vergelijken met het oorspronkelijke woord
    print("Het woord is een palindroom.") #als true > dan wordt dit geprint
else:
    print("Het woord is geen palindroom.") #als wrong > dan wordt dit geprint