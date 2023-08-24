"""
info
1 pie = 12 pulgadas 
1 yarda = 3 pies 
1 pulgada = 2.54 centímetros 
1 metro = 1000 milimetros
"""

input_data = float(input("Ingrese pies a convertir: "))

input_yards = input_data / 3
input_inches = input_data * 12
input_centimeter = input_inches * 2.54
input_meter = input_centimeter / 100


print("yards: ", input_yards)
print("inches: ", input_inches)
print("centimeter: ", input_centimeter)
print("meter: ", input_meter)
