#Uso de super() en Python

#Diferencia entre el atributo y el argumento del constructor
#Te habrás fijado que name y self.name parecen ser lo mismo, pues no, son diferentes aunque contengan el mismo valor.
#La sentencia self.name hace referencia al atributo del objeto, mientras que name hace referencia al valor del argumento de __init__ cuando se crea una instancia.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")

student = Student("Ana", 20, "S123")
student.greet()