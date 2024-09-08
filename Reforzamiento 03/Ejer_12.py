from itertools import count

tamano_lista= int(input(f"Ingrese el tamaño de la lista: "))

companias_ti= []
print(f"Por favor ingrese 5 nombres de {tamano_lista} compañias de TI: ")
for i in range(5):
    compania= input(f"Compañía {i+1}: ")
    companias_ti.append(compania)

companias_repetidas= companias_ti.copy()
print(f"Por favor ingrese otras 2 compañias de TI")
for i in range(2):
    compania_repetida= input(f"Compañía {i + 1}: ")
    companias_repetidas.append(compania_repetida)



print(companias_ti)
print(nombres_no_repetidos)
print(companias_repetidas)








