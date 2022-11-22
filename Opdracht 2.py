# >>> NOG NIET HELEMAAL AF! <<<
# Opdracht: 19. Dobbelsteen nr 1 (1)
# Vraag de gebruiker hoeveel dobbelstenen deze wil gooien. Laat zien dat de dobbelstenen gegooid worden, wat het resultaat per dobbelsteen is en wat de som is van het aantal ogen.
# https://www.geeksforgeeks.org/python-program-to-design-an-unbiased-dice-throw-function/
import random
def dice_throw():
    return random.choice([1,2,3,4,5,6])
print("Dobbelsteen worp: ", dice_throw())