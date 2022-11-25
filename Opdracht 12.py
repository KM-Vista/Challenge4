# Opdracht 12. Sinterklaas verlanglijst (2)
# Vraag de gebruiker om in te voeren wat deze graag van Sinterklaas zou willen hebben. 
# Vraag één item per keer en blijf vragen tot de gebruiker "KLAAR!" ingetypt heeft. 
# Toon vervolgens de lijst in alfabetische volgorde op het scherm.
# https://www.w3schools.com/python/python_while_loops.asp


item = (input("Voer een item per keer in wat je graag van Sinterklaas wilt: "))
kadolijst = [] #de lijst zelf
kadolijst.append(item) #item toevoegen aan de lijst 'kadolijst'

while item != 'klaar': #herhaal vraag om input totdat 'klaar' wordt ingegeven
    item = (input("Voer een item per keer in wat je graag van Sinterklaas wilt: "))
    kadolijst.append(item)
else:
    kadolijst.remove(kadolijst[-1]) #verwijder het latste item > 'klaar'
    kadolijst.sort() #kadolijst sorteren op alfabetische volgorde
    print(kadolijst) #kadolijst weergeven
