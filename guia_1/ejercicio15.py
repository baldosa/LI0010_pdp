"""
Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.
"""

numbers = input("Ingresá 3 números separados por coma: ")

n1, n2, n3 = [int(x) for x in numbers.split(",")]

agg = n1 + n2 + n3

if agg > 10:
    print(agg // 2)
else:
    print(agg**3)
