#PARTE2
# Crear la cadena de texto
text = "Hola mundo"

# Crear el iterador
iter_text = iter(text)

# Iterar a través del iterador e imprimir cada carácter
for char in iter_text:
    print(char)
    #PARTE3
    # Definir el límite
limit = 10

# Crear un iterador para los números impares
odd_iter = iter(range(1, limit+1, 2))

# Iterar a través del iterador e imprimir los números
for num in odd_iter:
    print(num)