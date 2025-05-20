
class Engine:
    def __init__(self):
        print("Engine started")
        
        
class Car:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()
        

car = Car("Toyota")
