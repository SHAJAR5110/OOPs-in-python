

### 📄Using `@property`, `@setter`, and `@deleter` in Python


This assignment demonstrates how to use Python's built-in **property decorators** — `@property`, `@<property>.setter`, and `@<property>.deleter` — to control access to a class attribute with **encapsulation and validation**.

---

## 🧩 Code Overview

We define a class `Product` with a private variable `_price`.
We then use **property decorators** to:

* **Access** the price using `@property`
* **Update** the price with validation using `@price.setter`
* **Delete** the price using `@price.deleter`

---

### ✅ Functional Description

```python
class Product:
    def __init__(self, price):
        self._price = price
```

* The constructor initializes the price.
* The variable `_price` is a **conventionally private** attribute (not meant to be accessed directly).

---

### 🏷️ Getter

```python
@property
def price(self):
    return self._price
```

* This allows `p.price` to work like an attribute, even though it's calling a method.
* Enables **read-only** style access to `_price`.

---

### ✏️ Setter

```python
@price.setter
def price(self, value):
    if value < 0:
        raise ValueError("Price cannot be negative.")
    self._price = value
```

* Allows **updating** the price (`p.price = 150`).
* Includes **validation**: raises an error if a negative value is provided.

---

### ❌ Deleter

```python
@price.deleter
def price(self):
    del self._price
```

* Allows **deleting** the `_price` attribute with `del p.price`.

---

## 🔍 Example Usage

```python
p = Product(100)
print(p.price)   

p.price = 150
print(p.price)   

del p.price        
```

---

## 🧠 Key Takeaways

* `@property` allows defining **getter methods** that can be accessed like attributes.
* `@<property>.setter` adds **controlled writing** to attributes.
* `@<property>.deleter` defines **custom delete logic**.
* These decorators help with **data encapsulation**, **validation**, and **cleaner API design**.


