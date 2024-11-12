#CALCULADORA
# Función para sumar
def sumar(num1, num2):
    return num1 + num2

# Función para restar
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir
def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir por cero"

# Menú de la calculadora
print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Solicitar al usuario que elija una opción
opcion = input("Por favor, elija una opción (1/2/3/4): ")

# Solicitar los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada por el usuario
if opcion == '1':
    print("El resultado de la suma es:", sumar(num1, num2))
elif opcion == '2':
    print("El resultado de la resta es:", restar(num1, num2))
elif opcion == '3':
    print("El resultado de la multiplicación es:", multiplicar(num1, num2))
elif opcion == '4':
    print("El resultado de la división es:", dividir(num1, num2))
else:
    print("Opción inválida. Por favor, elija una opción válida.")