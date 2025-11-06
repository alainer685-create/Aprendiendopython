def sumar_numeros(num1 , num2):
    return num1 + num2

print(sumar_numeros(10 , 20))

def celsius_a_fahrenheit(celsius):    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = float(input("ingresa temperatura en celsius: "))
if temp_c >= 1:
   print("En fahrenheit:" , celsius_a_fahrenheit(temp_c))
else:
    print("La temperatura es 0 o menor, no se realiza la conversión.") 

def suma_hasta_n(n):
    suma = 0  # Inicializamos la suma en 0
    for i in range(1, n + 1):  # Bucle desde 1 hasta n
        suma += i  # Agregamos i a la suma
    return suma

# Prueba la función
numero = int(input("Ingresa un número n: "))
print("La suma del 1 al", numero, "es:", suma_hasta_n(numero))

def suma_hasta_n_while(n):
    suma = 0
    i = 1
    while i <= n:
        suma += i
        i += 1
    return suma

numero = int(input("Ingresa un número n: "))
print("La suma del 1 al", numero, "es:", suma_hasta_n(numero))
