
notas_alumnos={}

cant_alumnos= int(input("Indique la cantidad de alumnos a ingresar:"))

for i in range(cant_alumnos):
    nombre= str(input(f"Ingrese el nombre {i+1}: "))
    nota = float(input("Indique la nota:"))
    notas_alumnos[nombre]= nota

for nombre,nota in notas_alumnos.items():
    print(f"{nombre} tiene la nota de {nota}")

media_notas= sum(notas_alumnos.values())/cant_alumnos
print("La media de todas las notas es: {}".format(media_notas))
