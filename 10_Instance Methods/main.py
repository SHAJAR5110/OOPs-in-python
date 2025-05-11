
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")
        

dog1 = Dog("Candy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
dog1.bark()
dog2.bark()