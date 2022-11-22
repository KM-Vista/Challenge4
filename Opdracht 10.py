# Opdracht: 10. Delen (1)
# Vraag de gebruiker om 3 getallen in te voeren. Het programma deelt deze 3 getallen door elkaar en toont de uitkomst op vier decimalen nauwkeurig op het scherm.
# Bron: workshop tijdens challenge 3
# https://stackoverflow.com/questions/54968686/how-to-round-to-4-decimal-places#54971765
cijfer1 = float(input("Voer het eerste cijfer in: "))
cijfer2 = float(input("Voer het tweede cijfer in: "))
cijfer3 = float(input("Voer het derde cijfer in: "))

som = (cijfer1 / cijfer2 / cijfer3)
print(round(som,4))