import random

numbers = []

for i in range(0,10):
    a = random.randrange(-15,15)
    numbers.append(a)
squares = [x**2 for x in numbers]

print("Random numbers:", numbers)
print("Squares:", squares)