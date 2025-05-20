

### 📄 Custom Exception in Python


The objective of this assignment is to **create and raise a custom exception** in Python using a user-defined exception class. This is helpful when you want more control and clarity over specific error scenarios in your program.

---

## 💡 What is a Custom Exception?

In Python, you can define your own exceptions by creating a class that inherits from the built-in `Exception` class. This allows you to:

* Handle specific error cases cleanly
* Provide meaningful messages for debugging
* Improve code readability and maintenance

---

## 🧱 Code Structure Explanation

### ✅ Custom Exception Definition

```python
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass
```

* `InvalidAgeError` is a custom exception.
* It inherits from Python’s built-in `Exception` class.
* You can add a docstring to explain its purpose.

---

### 🔍 Validation Function

```python
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
```

* This function checks if the provided age is below 18.
* If the condition is true, it raises the `InvalidAgeError`.

---

### 🔐 Try-Except Handling

```python
try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
```

* **`try` block**: Gets input from the user and validates the age.
* **`except InvalidAgeError`**: Catches and handles your custom exception.
* **`except ValueError`**: Catches cases where input is not a valid integer.

---

## ✅ Example Outputs

**Case 1 – Valid Input:**

```
Enter your age: 22
Age is valid.
```

**Case 2 – Age Below 18:**

```
Enter your age: 15
InvalidAgeError: Age must be at least 18.
```

**Case 3 – Non-integer Input:**

```
Enter your age: abc
Please enter a valid integer for age.
```

---

## 📌 Key Takeaways

* Custom exceptions make your code **more descriptive and precise**.
* Use them for **business logic errors**, like "age must be 18+", "invalid username", etc.
* Always combine them with proper `try-except` blocks for robust error handling.

