import random

numbers = []
for i in range(0, 5000):
    numbers.append(random.randint(0, 100000))

print("Máximo ", sum(numbers) / len(numbers))
