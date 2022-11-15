# Opdracht: 5. Tientallen (1)
# Gebruik een lus om alle tientallen van 10 tot en met 100 op het scherm te tonen.
# https://www.w3schools.com/python/python_for_loops.asp
for x in range(10,101,10):
    print(x)

# Opdracht: 9. Woord draaien (1)
# Vraag om een woord en zorg ervoor dat het omgedraaid op het scherm getoond wordt.
# https://www.w3schools.com/python/python_howto_reverse_string.asp
text = "Vista college" [::-1]
print (text)

#Opdracht: 10. Delen (1)
# Vraag de gebruiker om 3 getallen in te voeren. Het programma deelt deze 3 getallen door elkaar en toont de uitkomst op vier decimalen nauwkeurig op het scherm.
# Bron: workshop tijdens challenge 3
# https://stackoverflow.com/questions/54968686/how-to-round-to-4-decimal-places#54971765
cijfer1 = float(input("Voer het eerste cijfer in: "))
cijfer2 = float(input("Voer het tweede cijfer in: "))
cijfer3 = float(input("Voer het derde cijfer in: "))

som = (cijfer1 / cijfer2 / cijfer3)
print(round(som,4))

# Opdracht: 18. Faculteit (1)
# Maak een programma dat de faculteit van een door de gebruiker ingevoerd getal kan berekenen en op het scherm toont.
# https://www.w3schools.com/python/ref_math_factorial.asp
cijfer = int(input("Voer een getal in: "))
import math

print(math.factorial(cijfer))

# >>> NOG NIET HELEMAAL AF! <<<
# Opdracht: 19. Dobbelsteen nr 1 (1)
# Vraag de gebruiker hoeveel dobbelstenen deze wil gooien. Laat zien dat de dobbelstenen gegooid worden, wat het resultaat per dobbelsteen is en wat de som is van het aantal ogen.
# https://www.geeksforgeeks.org/python-program-to-design-an-unbiased-dice-throw-function/
import random
def dice_throw():
    return random.choice([1,2,3,4,5,6])
print("Dobbelsteen worp: ", dice_throw())

# Opdracht: 2. Getallen (2)
# Het programma vraagt de gebruiker 5 getallen in te voeren, gescheiden door een spatie. Vervolgens worden deze getallen van groot naar klein gesorteerd op het scherm getoond.
# 
Getallen = int(input("Voer 5 getallen in, gescheiden door een spatie: "))
print(Getallen)