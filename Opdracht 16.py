# Opdracht 16. Verkiezingen (2)
# Gebruikers mogen net zo lang namen invoeren tot er "UITSLAG!" ingevoerd wordt. 
# De naam die het vaakst ingevoerd is wordt op het scherm getoond als de winnaar. 
# Bij het invoeren maken hoofdletters geen verschil.
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/ 

import statistics #de modus van een reeks staat onder 'statistics'
from statistics import mode #'mode' om het meest voorkomende item in de lijst te zoeken

naam = (input("Voer de naam in van de persoon waar je op stemt: ").lower()) #'.lower' om de invoer om te zetten naar kleine letters 
namenlijst = [] #de lijst zelf
namenlijst.append(naam) #item toevoegen aan de lijst 'namenlijst'

while naam != 'UITSLAG': #herhaal vraag om input totdat 'UITSLAG' wordt ingegeven
    naam = (input("Voer de naam in van de persoon waar je op stemt: ").lower()) #'.lower' om de invoer om te zetten naar kleine letters
    namenlijst.append(naam) #voegt de naam toe aan de lijst
else:
    namenlijst.remove(namenlijst[-1]) #verwijder het latste item > 'UITSLAG'
    #namenlijst.sort() #namenlijst sorteren op alfabetische volgorde
    #print(namenlijst) #namenlijst weergeven
    def most_common(namenlijst): #functie om de meest voorkomende naam weer te geven
        return(mode(namenlijst)) #zoek de meest voorkomende naam
    print(most_common(namenlijst)) #geef de meest voorkomende naam weer

