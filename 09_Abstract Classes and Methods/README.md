
### 📄  Abstract Classes and `@abstractmethod`

---

## 🧾 Overview

This assignment demonstrates the use of **abstract base classes (ABCs)** in Python using the `abc` module. It explains how to define a base class that cannot be instantiated on its own and enforces the implementation of certain methods in derived classes.

---

## 🧠 Key Concepts

### 🔹 What is an Abstract Class?

An **abstract class** is a class that cannot be instantiated directly. It serves as a **blueprint for other classes**. Abstract classes are typically used when you want to define a common interface for a group of subclasses.

In Python, abstract classes are created by inheriting from `ABC` (Abstract Base Class) and defining at least one method with the `@abstractmethod` decorator.

---

### 🔹 What is `@abstractmethod`?

The `@abstractmethod` decorator is used to declare methods that must be implemented in any subclass. If a subclass does not override an abstract method, trying to instantiate it will result in an error.

---

## 🧪 Code Explanation

```python
from abc import ABC, abstractmethod

# Define abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

* `Shape` is an abstract class that contains one abstract method: `area()`.
* It defines a contract that any subclass of `Shape` **must** implement the `area()` method.

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

* `Rectangle` is a concrete class that inherits from `Shape`.
* It provides a specific implementation of the `area()` method.

---

## ✅ Summary

* Abstract classes define a **template** for subclasses.
* The `@abstractmethod` enforces **method overriding** in child classes.
* This ensures a consistent interface across different subclasses.

---

## 📌 Use Cases

Use abstract classes when:

* You want to define a common interface for all subclasses.
* You want to prevent direct instantiation of a general class.
* You want to force subclasses to provide specific implementations.

