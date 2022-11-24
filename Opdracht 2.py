# Opdracht: 2. Getallen (2)
# Het programma vraagt de gebruiker 5 getallen in te voeren, gescheiden door een spatie. Vervolgens worden deze getallen van groot naar klein gesorteerd op het scherm getoond.
# https://www.w3schools.com/python/python_lists_sort.asp
# https://www.w3schools.com/python/ref_string_split.asp

cijfers = (input("Voer 5 getallen in, gescheiden door een spatie: ")).split()
cijfers.sort(reverse = True)
print(cijfers)
