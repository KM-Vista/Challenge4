# Opdracht 17. Lootbox (2)
# Maak een progamma dat een loot drop simuleert. 
# Common, Uncommon, Rare, Epic en Legendary zijn de verschillende niveau's qua loot, op volgorde van wat het meest voor komt tot wat het minst voor komt. 
# Zorg er voor dat jouw programma hier rekening mee houdt.

import random #random om willekeurig een uit te kiezen

a = "Common"
b = "Uncommon"
c = "Rare"
d = "Epic"
e = "Legendary"

sequence=[a, a, a, a, a, b, b, b, b, c, c, c, d, d, e]

print("Loot: " + random.choice(sequence))
