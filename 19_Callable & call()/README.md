

### 📄 Using `__call__` to Make Objects Callable in Python


The goal of this assignment is to understand how the `__call__` method in Python allows instances of a class to behave like functions. This is part of Python's **dunder methods** (double underscore methods), which provide powerful ways to customize class behavior.

---

## 🧩 Code Overview

We define a class `Multiplier` that:

* Stores a `factor` upon initialization
* Implements the `__call__` method to multiply any given input value by that factor
* Allows the object to be used as a **callable** (i.e., like a function)

---

### ✅ How It Works

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
```

* The constructor stores a multiplier value (factor).
* Example: `Multiplier(5)` sets `factor = 5`.

---

### 🧠 Making the Object Callable

```python
def __call__(self, value):
    return value * self.factor
```

* This special method makes the object behave like a function.
* You can now use `object(value)` syntax instead of calling a method manually.
* For example: `m(10)` returns `50` if `factor = 5`.

---


* `callable(m)` returns `True` because the object has a `__call__` method.
* `m(10)` multiplies 10 by 5 and returns 50.

---

## 🧠 Key Takeaways

* The `__call__` method allows instances to be used like functions.
* Useful for cases like:

  * Function wrappers
  * Callbacks
  * Custom behaviors in class-based logic
* Objects with `__call__` can be passed to places expecting functions.


