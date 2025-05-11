class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

        
class Teacher(Person):
    def __init__(self, name, age, height, subject):
        super().__init__(name, age, height)
        self.subject = subject

    def show(self):
        print(f"Name: {self.name}, \nAge: {self.age}, \nHeight: {self.height}, \nSubject: {self.subject}")

# Example usage
person1 = Person("Shajar", 22, 5.5)
teacher1 = Teacher("Shajar", 22, 5.8, "Mathematics")
teacher1.show()

