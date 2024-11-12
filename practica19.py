#Fundamentos de Programación Orientada a Objetos en Python
class Person:
    def _init_(self, name, age):
        self.age = age



    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")
        
    
person1 = Person("Ana", 30)
person2 = Person("Luis", 25)

person1.greet()
person2.greet()