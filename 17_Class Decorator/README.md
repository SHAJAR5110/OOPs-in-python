

### 📄 Class Decorators in Python

This assignment demonstrates the use of a **class decorator** in Python to **dynamically add behavior (a method)** to a class.

---

## 💡 What is a Class Decorator?

A **class decorator** is a function that takes a class as an argument, modifies it (optionally), and returns the modified class.
It allows for dynamic enhancement of class functionality **without modifying the original class directly.**

---

## 🧩 Code Explanation

```python
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass
```

### How it works:

1. `add_greeting(cls)` is a **class decorator function**.
2. Inside this function, we **define a method `greet`** and attach it to the class (`cls.greet = greet`).
3. The `@add_greeting` decorator **modifies the `Person` class** by adding the `greet()` method dynamically.
4. Now, any instance of `Person` will have access to `greet()` even though it wasn't originally defined in the class.

---

Even though the `Person` class has no methods defined initially, it now has a `greet()` method because of the class decorator.

---

## 🧠 Summary

* **Class decorators** allow us to modify or enhance classes without altering the original code.
* This is useful for **adding common behavior**, **tracking**, or **registering classes** dynamically.
* The `@decorator` syntax makes it clean and reusable.


