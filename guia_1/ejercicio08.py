steps = int(input("Cantidad de numeros de Fibonnaci: "))

step = 0

n, nn = 0, 1

while step < steps:
    fibonnaci = n + nn
    print(fibonnaci)
    n = nn
    nn = fibonnaci
    step += 1
