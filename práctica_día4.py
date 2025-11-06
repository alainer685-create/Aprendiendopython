# Lista inicial de compras
compras = ["leche", "pan", "huevos", "frutas"]

# Agrega un ítem
compras.append("café")
print("Lista actualizada:", compras)

# Elimina un ítem por valor
compras.remove("pan")
print("Después de eliminar pan:", compras)

# Inserta en posición específica
compras.insert(1, "jugo")
print("Después de insertar jugo:", compras)

# Ordena la lista
compras.sort()
print("Lista ordenada:", compras)

# Crea una tupla de precios fijos
precios = (2.5, 1.0, 3.0, 4.0)  # Inmutable
print("Precios:", precios)

#Tupla de precios (del ejemplo)
precios = (2.5, 1.0, 3.0, 4.0)  # Inmutable

# Función para sumar elementos de una tupla o lista (integrando bucles del Día 2 y funciones del Día 3)
def suma_elementos(coleccion):
    suma = 0.0  # Usamos float para manejar decimales
    for elemento in coleccion:  # Iteramos directamente sobre los elementos
        suma += elemento  # Sumamos cada uno
    return suma

# Prueba la función
print("La suma de los precios", precios, "es:", suma_elementos(precios))

# Usando while 
def suma_elementos_while(coleccion):
    suma = 0.0
    i = 0
    while i < len(coleccion):  # len() da el tamaño
        suma += coleccion[i]
        i += 1
    return suma

print("Suma con while:", suma_elementos_while(precios))

# Integrar if
def suma_elementos_condicional(coleccion):
    suma = 0.0
    for elemento in coleccion:
        if elemento > 1.0:
            suma += elemento
    return suma

print("Suma de precios > 1.0:", suma_elementos_condicional(precios))  # Debería ser 2.5 + 3.0 + 4.0 = 9.5
