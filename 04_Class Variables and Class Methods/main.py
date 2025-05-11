
class Bank:
    bank_name = "Bank of Python"  
    
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Bank Name: {self.bank_name}")
        
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to: {cls.bank_name}")
        

# Create instances of the Bank class        
bank1 = Bank("Bank A")
# Display initial bank name
bank1.display_info()  
# Change the bank name using the class method
Bank.change_bank_name("Bank of Code")            
# Display the bank name again to show that it has changed
bank1.display_info()


