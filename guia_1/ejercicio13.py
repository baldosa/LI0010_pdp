"""
info
1 pie = 12 pulgadas 
1 yarda = 3 pies 
1 pulgada = 2.54 centímetros 
1 metro = 1000 milimetros
"""
print(
    """
      Convertir a centímetros.
      1. Pies a centímentros
      2. Pulgadas a centímetros
      """
)
option = float(input("Elegí una opción: "))

if option == 1:
    foot = float(input("Ingresá pies a convertir... "))
    print(f"Son {foot*30.48} centímetros")
elif option == 2:
    inch = float(input("Ingresá pulgadas a convertir... "))
    print(f"Son {inch*2.54} centímetros")
else:
    print("Opción incorrecta")
