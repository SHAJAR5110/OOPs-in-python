
### 📄 Static Method 

---

## 🧾 Assignment Description

**Objective:**
Create a class `Temperature` with a **static method** `celsius_to_fahrenheit(c)` that:

* Takes temperature in Celsius as input
* Converts it to Fahrenheit
* Returns the result without needing to create an instance of the class

---

## 🧠 Key Concepts

### 🔹 Static Method

A **static method** is defined using the `@staticmethod` decorator. Unlike instance or class methods, it:

* Doesn’t access `self` or `cls`
* Belongs to the class rather than any instance
* Is used for utility functions that logically belong to the class but don’t operate on instance data

In this case:

```python
@staticmethod
def celsius_to_fahrenheit(c):
    return (int(c) * 9/5) + 32
```

---

## 🧪 How It Works

* The user is prompted to enter a temperature in Celsius.
* The program checks if the input is a valid number.
* If valid, the static method `celsius_to_fahrenheit` is called **directly from the class** to convert the temperature.


## 📌 Summary

* The `Temperature` class defines a **utility conversion function** using a static method.
* No object creation is necessary to use the method.
* This structure is ideal for **utility or helper functions** related to a class’s concept but not tied to any specific object.

