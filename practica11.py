#Comprehension Lists en Python
squares = [x**2 for x in range(1, 11)]
#print("Cuadrados:", squares) quitar el codigo numeral para dar una respuesta

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
#print("Temperatura en F:", fahrenheit)}quitar el codigo numeral para dar una respuesta

# Números pares
evens = [x for x in range(1, 21) if x % 2 == 0]
#print(evens)quitar el codigo numeral para dar una respuesta


matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]


transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
#print(transposed)quitar el codigo numeral para dar una respuesta

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

#print(transposed)quitar el codigo numeral para dar una respuesta

#utilizar el codigo "clear" para borrar resultados anteriores