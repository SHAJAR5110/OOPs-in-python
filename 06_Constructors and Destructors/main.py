
class Logger:
    def __init__(self):
        print("Constructor called, object created")
        
    def hello(self):
        print("Hello, world!")
            
    def __del__(self):
        print("Destructor called, object destroyed")

# Create an object of the Logger class
# This will call the constructor
# The destructor will be called when the object is deleted or goes out of scope
obj1= Logger()
# Call the hello method
obj1.hello()            