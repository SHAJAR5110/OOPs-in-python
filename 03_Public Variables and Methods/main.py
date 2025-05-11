class Car:

    # Public variable    
    brand= "Toyota"
    
    # Public method
    def start(self):
        print(f"Car named {self.brand} is starting.")


car1 = Car()
# Accessing the public variable
print(car1.brand)
# Accessing the public method
car1.start()
 
        
