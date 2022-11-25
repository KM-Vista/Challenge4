# Opdracht 8. Fibonacci (2)
# Schrijf een programma dat de eerste 15 getallen van de Fibonacci reeks op het scherm laat zien. Gebruik hiervoor een lus.
# https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
# https://pythonguides.com/python-fibonacci-series/

def fibonacci(n):
    a=0 #eerste getal = 0
    b=1 #tweede getal = 1

    #als een getal kleiner dan 0 wordt ingevoerd, dan wordt 'foute invoer' teruggekoppeld
    if n<0:
        print("Foute invoer. Voer 0 of groter in.")
    #als 0 wordt ingevoerd, dan is de uitkomst 0    
    elif n==0:
        return 0
    #als 1 wordt ingevoerd dan wordt de waarde van b geprint > 1
    elif n==1:
        return b
    #in alle andere gevallen worden de waardes van de 0e en 1e plaats geprint + de waardes vanaf de 2e t/m de 15e plaats
    else:
        print(a)
        print(b)
        for i in range (2,n): #print de range vanaf het 2e item t/m het n-de item
            c=a+b 
            a=b
            b=c
            print(c)

print(fibonacci(15))
