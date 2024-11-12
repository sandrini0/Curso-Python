#Diccionario
numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Fidel", "Apellido": "Oses", "Altura": 1.80, "Edad": 30}
print(information)
del information["Edad"] #Usar la palabra "del" es para eliminar algun dato de codigo
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Fidel": {"Apellido": "Oses", "Altura": 1.80, "Edad": 30},
"Mauricio": {"Apellido": "Matos", "Altura": 2.00, "Edad": 22}}

print(contacts["Fidel"])