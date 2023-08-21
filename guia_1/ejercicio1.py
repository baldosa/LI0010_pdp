# libra
kg = 2.2

print("Convertir kilogramos en libras")
input_value = input("Ingresá la cantidad de kilogramos a convertir: ")

try:
    print(f"Son {kg*float(input_value)} libras")
except:
    print("Error al convertir, ingresaste un número?")
