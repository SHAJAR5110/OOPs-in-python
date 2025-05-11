class MathUtils:
        
    static_var = 0
    
    def __init__(self):
        MathUtils.static_var += 1
    
    def show_static_var(self):
        print(f"Static variable value: {MathUtils.static_var}")
        
    @staticmethod
    def add(a, b):
        return a + b
    
# The static method can be called directly from the class without creating an instance 
ans = MathUtils.add(5, 10)
print(f"Sum is: {ans}")  


obj1 = MathUtils()
obj2 = MathUtils()
obj2.show_static_var()

