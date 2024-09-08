
agenda={}

cant_contactos= int(input("¿Cuántos contactos vas a registrar?:"))

for i in range(cant_contactos):
    nombre= str(input(f"Ingrese el nombre del contacto {i+1}: "))
    telefono = int(input(f"Indique el numero de teléfono de {nombre}:"))
    agenda[nombre]= telefono

buscar_nombre= input("Ingrese el nombre del contacto a buscar:")
if buscar_nombre in agenda:
    print(f"{buscar_nombre} tiene el numero de teléfono {agenda[buscar_nombre]}")

else:
    print("No se encuentra registrado")
