class Employee:
    
    
    def __init__(self,name ,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    
    
obj1 = Employee("Shajar Abbas", 50000, "123-45-6789")   
public = obj1.name
protected = obj1._salary 

# ❌ Direct access to private variable will raise an error
# private = obj1.__ssn  # Uncommit this line to see the error

private_that_works = obj1._Employee__ssn 

# The public variable can be accessed directly
# The protected variable can be accessed directly but is not recommended
# The private variable cannot be accessed directly, but can be accessed through a method
print(f"Private variable that works: {private_that_works}")
print(f"Public variable: {public} \nProtected variable: {protected}")

        