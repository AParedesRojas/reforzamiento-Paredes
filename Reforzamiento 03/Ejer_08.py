from string import printable

lista= [0]*10

print("por favor ingrese 10 números")
for i in range(10):
    lista[i]= float(input(f"Número {i+1}: "))

# Suma de números:

suma=sum(lista)

# media de los números ingresados:
media= suma/10

print(f"La suma de los números ingresados es: {suma}")
print(f"La media de los números ingresados es: {media}")









