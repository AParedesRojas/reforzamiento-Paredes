
diccionario={}

print("Ingrese 04 números")

for i in range(4):
    keys= int(input(f"Ingrese el número {i+1}: "))
    diccionario[keys]=keys**3


print("El diccionario es: {}".format(diccionario))