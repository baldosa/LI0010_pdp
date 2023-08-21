"""
Jornal de un Operario. Se necesita desarrollar un programa para el área de 
recursos humanos de una empresa que permita informar el jornal de un 
determinado operario. Usted deberá cargar por teclado el código de turno 
que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) 
y la cantidad de horas trabajadas. La política de trabajo en la empresa es que 
los operarios de la misma pueden trabajar en el turno diurno o nocturno. 
Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, 
si lo hace en el turno diurno cobra 35.50 pesos la hora."""

print(
    """
    1. Turno diurno
    2. Turno nocturno  
    """
)
turn = int(input("Ingrese turno: "))

hours = int(input("Ingrese horas trabajadas: "))

if turn == 1:
    day_salary = hours * 35.5
elif turn == 2:
    day_salary = hours * 40.6

print("Monto del día: ", day_salary)
