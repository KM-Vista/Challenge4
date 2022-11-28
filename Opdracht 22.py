# 22. Baggins (4)
#Kopieer de onderstaande dictionary naar jouw Python file. Maar, let op: pas deze dictionary verder niet aan!
# Maak updates voor deze dictionary aan de hand van de volgende gebeurtenissen.
# Je vindt 12 zilver. Voeg een key toe aan je bezittingen met de juiste waarde.
# Je zakmes valt uit je buidel zonder dat je het doorhebt. 
# Verwijder deze uit je bezittingen.
# Je besluit de items in je rugzak op alfabetische volgorde te sorteren.
# Print je bezittingen in de terminal.
# https://www.w3schools.com/python/python_dictionaries_add.asp
# https://www.w3schools.com/python/python_dictionaries_remove.asp 

bezittingen = {
     'goud' : 500,
     'buidel' : ['touw', 'vuursteen', 'zakmes'],
     'rugzak' : ['panfluit', 'dolk', 'slaapzak','appel']
}

bezittingen['zilver'] = 12
bezittingen.pop('zakmes')
