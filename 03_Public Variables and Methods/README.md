

### 📘 Accessing Public Variable & Method


### 🔍 Overview:

This assignment demonstrates the concept of **public variables** and **public methods** in Python using a simple `Car` class.

---

### 🧠 Key Concepts:

#### ✅ Public Variable:

* `brand` is declared as a public class variable.
* Public variables can be accessed directly through any object.
* In this example, the brand is `"Toyota"` and is printed using `print(car1.brand)`.

#### ✅ Public Method:

* `start()` is a public method that can be called using any object.
* It uses the `brand` variable to print a message that the car is starting.
* Being public means there are no restrictions on calling it from outside the class.

---

### 🧪 How It Works:

1. A class `Car` is defined with a public variable `brand` and a public method `start()`.
2. An object `car1` is created from this class.
3. From outside the class:

   * `car1.brand` accesses and prints the public variable.
   * `car1.start()` calls the public method and prints the message.

---

### 📊 Summary:

* **Public variable** = accessible via object (e.g., `car1.brand`)
* **Public method** = callable via object (e.g., `car1.start()`)
* Demonstrates object interaction with class members from outside the class scope.

