
tamano_lista= int(input(f"Ingrese el tamaño de la lista de alumnos: "))

nombre_alumnos= []
print(f"Por favor ingrese los nombres de {tamano_lista} alumnos: ")
for i in range(tamano_lista):
    nombre= input(f"Nombre {i+1}: ")
    nombre_alumnos.append(nombre)

print("El tamaño de la lista es:{}".format(len(nombre_alumnos)))
print("Los nombres de los alumnos ingresados son:")
for nombre in nombre_alumnos:
    print(nombre)






