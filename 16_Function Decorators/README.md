
### 📄 Decorators in Python 


This assignment demonstrates the use of a **decorator inside a class** in Python.
It also combines the use of a **`@staticmethod`** with a **custom decorator**.

---

## 🧩 What is a Decorator?

A **decorator** in Python is a function that wraps another function to **add extra behavior** without modifying the original function’s code.

Think of it like putting an extra layer of logic around a function — before or after it runs.

---

## 💡 How the Code Works

```python
class Main:
    
    def decorator(func):
        def wrapper():
            func()
            print("Function is being called")
        return wrapper
    
    @decorator
    @staticmethod
    def say_hello():
        print("Hello, World!")        

Main.say_hello()
```

### Breakdown:

1. `decorator(func)` is a **custom decorator** defined inside the `Main` class.
2. `@decorator` wraps the `say_hello()` method with additional logic.
3. `@staticmethod` makes `say_hello()` callable from the class directly without an instance.
4. When `Main.say_hello()` is called:

   * It first runs `say_hello()` → prints `"Hello, World!"`
   * Then it prints `"Function is being called"` from the decorator.

---

### Why?

* The function `say_hello()` is wrapped by `wrapper()` inside the `decorator`.
* The wrapper first calls the original function, then adds a custom message.

---

## ⚠️ Notes:

* **Decorator must be defined before it’s used**, even if it’s inside a class.
* The order of decorators matters:
  Here, `@staticmethod` is **decorated first**, and then wrapped by `@decorator`.

---

## ✅ Summary

* Decorators let you add reusable logic around functions.
* You can define and apply decorators inside classes.
* Static methods can be decorated as long as you manage the order properly.


