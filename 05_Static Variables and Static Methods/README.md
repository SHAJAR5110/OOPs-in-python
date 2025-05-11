### 📘 Static Variable & Static Method


* A **static variable** (`static_var`) shared across all instances.
* A **constructor** that increments the static variable on each object creation.
* A **method** (`show_static_var`) to display the static variable.
* A **static method** (`add`) to return the sum of two values, callable without any object.

---

### 🔍 Overview:

This assignment demonstrates both a **static (class) variable** and a **static method** using the `MathUtils` class.

---

### 🧠 Key Concepts:

#### 🧮 Static Variable:

* `static_var` is declared **at the class level**, not inside any method.
* It is **shared among all instances** of the class.
* Each time an object is created, `static_var` is incremented in the constructor using `MathUtils.static_var += 1`.

#### 🧰 Static Method:

* `add(a, b)` is a static method, defined using the `@staticmethod` decorator.
* It performs a utility task (addition) and does **not access any class or instance data**.
* It can be called **directly using the class name** without creating an object.

---

### 🧪 How It Works:

1. When the program runs:

   * The `add()` method is called using `MathUtils.add(5, 10)` and prints the sum.
2. If you create objects using `MathUtils()`, each one increments `static_var`.
3. You can call `show_static_var()` on any object to see how many times the class has been instantiated.

---

### 💡 Example Flow:

```python
obj1 = MathUtils()
obj2 = MathUtils()
obj2.show_static_var() 
```

---

### 📊 Summary:

| Feature         | Purpose                                     |
| --------------- | ------------------------------------------- |
| `static_var`    | Tracks shared data (e.g., object count)     |
| `@staticmethod` | Provides logic unrelated to instance state  |
| `add()`         | Simple utility method, no self/cls required |
