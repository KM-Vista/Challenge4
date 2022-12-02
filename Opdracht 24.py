# NOG NIET KLAAR
# Opdracht 24. Nachtjes slapen (4)
# In deze exercise ga je een programma schrijven om voor een datum te berekenen hoeveel dagen geleden het deze datum was, 
# of hoeveel dagen deze datum in de toekomst ligt. 
# Bijvoorbeeld: +48 dagen is 48 dagen in de toekomst en -12 dagen is 12 dagen geleden. 
# Voor deze opdracht is specifiek datetime.date erg handig. 

# Vraag de gebruiker om het jaar.
# Vraag de gebruiker om de maand.
# Vraag de gebruiker om de dag.
# Print hoeveel dagen verschil er zit tussen deze datum en vandaag.

# https://www.programiz.com/python-programming/datetime 
# https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/

import datetime
from datetime import datetime, date

jaar = input("Voer hier het jaar in (JJJJ): ")
maand = input("Voer hier de maand in (MM): ")
dag = input("Voer hier de dag in (DD): ")

dateformat = "%Y,%m,%d"
vandaag = datetime.today()
invoer = date(jaar,maand,dag, dateformat)

print(vandaag)
print(invoer)
print(vandaag-invoer).days 

#verschil = vandaag - invoer

#print(verschil)

#def verschil (invoer, vandaag):
    #return (vandaag-invoer).days
#print(verschil(invoer, vandaag), "days")