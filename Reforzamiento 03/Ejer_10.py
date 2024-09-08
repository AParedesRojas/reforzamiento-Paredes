
departamentos= ["Junín", "Lima", "Ica", "Pasco", "Trujillo"]

print(f"Por favor ingrese 02 departamentos:")
for i in range(1):
    depto1= str(input(f"Departamento {i+1}: "))
    departamentos.append(depto1)
    depto2=str(input(f"Departamento {i+2}: "))

departamentos[0]=depto2

print(departamentos)








