import random

possibilities = [1,2,3,4,5,6]
total = 0
result = []
rolls = int(input("How many dices do you want to throw? "))

for x in range(rolls):
    result.append(random.randint(1, 6))
print(result)

for x in result:
    total += x
print(total)