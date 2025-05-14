
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (int(c) * 9/5) + 32
    
# Example usage

celsius = input("Enter temperature in Celsius: ")
if not celsius.isdigit():
    print("Please enter a valid number.")
else:
    fahrenheit = Temperature.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
