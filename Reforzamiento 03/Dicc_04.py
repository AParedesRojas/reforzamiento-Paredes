diccionario= {
    "Nombre": "Margarita",
    "Edad": "30",
    "Salario": 3000
}

# 3. Agrega un nuevo key llamado “dni” con su respectivo valor
diccionario["dni"]=("12345678")
# luego mostrar el valor de salario en consola.
print("Su Salaraio es: {}".format(diccionario["Salario"]))

#También elimina el key edad de tu diccionario, incluyendo su valor Mostrar finalmente el diccionario actualizado.
diccionario.pop("Edad")

print("El diccionario actualizado es: {}".format(diccionario))

#Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene.

lista= list(diccionario.items())
print(lista)
print(type(lista))







