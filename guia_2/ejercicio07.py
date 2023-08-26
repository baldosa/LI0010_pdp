input_number = 1
numbers = []
while input_number != 0:
    input_number = int(input("Ingrese un número, para finalizar ingrese 0: "))
    numbers.append(input_number)

print(sum(numbers) / len(numbers))
