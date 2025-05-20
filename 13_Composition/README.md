
### 📄 Composition in Python Classes (HAS-A Relationship)

**Objective:**
Create two classes:

* `Engine`: represents an engine with a `horsepower` attribute and a method to start the engine.
* `Car`: has a `name` and uses an instance of the `Engine` class, demonstrating **composition**.

This example shows how a class can contain objects of another class, a concept known as **composition** or a **HAS-A relationship**.

---

## 🧠 Key Concepts

### 🔹 Composition (HAS-A Relationship)

Composition means one class contains another class as an attribute. In this example:

* A `Car` **has an** `Engine`
* The `Car` class is not inheriting from `Engine`, but is using it internally

```python
class Car:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()
```



## 📌 Summary

* **Composition** allows one class to use another as a component.
* The `Car` class does **not inherit** from `Engine`, but it **uses it internally**.
* This approach keeps the code modular and promotes reusability.

