area_trabajo= []

area_trabajo.append("Cobranzas")
area_trabajo.append("Ventas")
area_trabajo.append("RR.HH")
area_trabajo.append("Facturación")

# Quitar 2 elementos por valor:

area_trabajo.remove("Cobranzas")
area_trabajo.remove("RR.HH")
print("La lista final es: {}.".format(area_trabajo))

print( "La cantidad total de ítems es: {}".format(len(area_trabajo)))