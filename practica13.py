#Bucles y Control de Iteraciones
numbers = [1, 2, 3, 4, 5, 6]

# Imprimir los elementos con su índice incrementado en 1
for i in numbers:
    print("Aquí i es igual a:", i+1)

# Imprimir los números del 3 al 9
for i in range(3, 10):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruta in fruits:
    print(fruta)
    # Verifica si la fruta es "Naranja" e imprime un mensaje
fruit = "Naranja"
if fruit == "Naranja":
    print("Naranja encontrada")

# Ciclo while que imprime los valores de x
x = 0
while x <= 5:
    if x == 3:
        # Sale del ciclo cuando x es 3
        break                                          # este break te limita hasta cierta pocision de datos
    print(x)
    x += 1
    numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    if i == 3:
        # Sale del ciclo cuando i es 3
        break
    print("Aquí i es igual a:", i)