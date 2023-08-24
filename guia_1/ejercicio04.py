a = int(input("valor a: "))
b = int(input("valor b: "))

# fmt: off
binomial = ((a + b)) ** 2
binomial_expanded = (a ** 2) + (2 * a * b) + (b ** 2)

print(binomial)
print(binomial_expanded)

if binomial == binomial_expanded:
    print("Es igual")
else:
    print("No es igual")
