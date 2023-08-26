numbers = input("Ingresá 2 números separados por coma: ")

n1, n2 = [int(x) for x in numbers.split(",")]

for i in range(n1, n2 + 1):
    if i % 2 != 0:
        print(i)
