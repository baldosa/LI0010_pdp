"""
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, 
proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: 
Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar 
la dirección de mail sería: fsteffolani@umet.edu.ar. 
Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: 
.@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería: soledad.steffolani@umet.edu.ar
"""
name = input("Nombre: ").lower()
surname = input("Apellido: ").lower()
domain = input("Dominio: ").lower()

name_first_letter = name[0:1].lower()
surname_first_letter = surname[0:1].lower()

if name_first_letter == surname_first_letter:
    email = f"{name}.{surname}@{domain}"
else:
    email = f"{name_first_letter}{surname}@{domain}"

print(email)
