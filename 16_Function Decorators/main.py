
class Main:
    
    def decorator(func):
        def wrapper():
            func()
            print("Function is being called")
        return wrapper
    
    @decorator
    @staticmethod
    def say_hello():
        print("Hello, World!")        
        
Main.say_hello()