import random

numbers = []
for i in range(0, 1000):
    numbers.append(random.randint(0, 10000))

print("Promedio ", sum(numbers) / len(numbers))
