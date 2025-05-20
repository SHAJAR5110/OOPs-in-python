
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        
        
    def start_engine(self):
        return f"Engine with {self.horsepower} started."    
        
class Car:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine
        

obj = Engine(150)        

car = Car("Toyota", obj)
print(car.engine.start_engine())