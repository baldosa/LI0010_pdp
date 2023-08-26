import random

numbers = []
for i in range(0, 10000):
    numbers.append(random.randint(0, 100000))

print("Máximo ", max(numbers))
