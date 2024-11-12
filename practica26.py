#Manejo de Archivos CSV

#Leer un archivo
"""with open('productos.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar la información por columnas
import csv

with open('productos.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")
        
        
        #clase 31 falta por entender