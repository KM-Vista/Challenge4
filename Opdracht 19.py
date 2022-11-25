# Opdracht: 19. Dobbelsteen nr 1 (1)
# Vraag de gebruiker hoeveel dobbelstenen deze wil gooien. Laat zien dat de dobbelstenen gegooid worden, wat het resultaat per dobbelsteen is en wat de som is van het aantal ogen.
# https://www.includehelp.com/python/program-to-design-a-dice-throw-function.aspx

import random

throw = int(input("Voer in hoeveel dobbelstenen er gegooid moeten worden: "))

for x in range(throw):
    def dice_throw():
        sequence = [1,2,3,4,5,6]
        return random.choice(sequence)

    print("Dobbelsteen gegooid: ",[dice_throw()])

sum = 0
sequence = []

for x in sequence():
    sum += x
    print(sum)
