### 📄 Use of `super()` 

---

## 🧾 Overview

In this assignment, we explore **inheritance** and how the `super()` function can be used to call the constructor of a base class. The example involves two classes:

* `Person` (Base Class) with attributes like `name`, `age`, and `height`.
* `Teacher` (Derived Class) that inherits from `Person` and adds an additional attribute `subject`.

---

## 🔑 Key Concepts

### 🔸 **Inheritance**:

Inheritance allows a class (child or derived class) to inherit properties and methods from another class (parent or base class).

```python
class Teacher(Person):
```

In this case, `Teacher` inherits from `Person`, which means the `Teacher` class has access to the attributes and methods of the `Person` class.

### 🔸 **Using `super()`**:

The `super()` function is used to call the constructor (`__init__`) or methods of the parent class within the child class. This is important for **reusing the functionality** of the parent class and avoiding code duplication.

In the code:

```python
super().__init__(name, age, height)
```

* `super()` is used inside the `Teacher` class to call the `__init__` method of the `Person` class and pass the required parameters (`name`, `age`, `height`).
* This allows the `Teacher` class to inherit the initialization logic from `Person` without having to duplicate it.

### 🔸 **Why Use `super()`**:

Using `super()` helps to maintain the **DRY (Don't Repeat Yourself)** principle in object-oriented programming. It makes sure that if the base class constructor changes in the future, it doesn’t require changes in all subclasses that inherit from it.

---

## 🧪 How It Works

1. The `Teacher` class inherits from the `Person` class.
2. In the constructor of `Teacher`, the `super().__init__(name, age, height)` line calls the constructor of the `Person` class, passing the `name`, `age`, and `height` arguments to it.
3. The `Teacher` class then initializes the additional attribute `subject`.
4. The `show()` method in `Teacher` displays all the details including the inherited attributes and the new `subject` attribute.

---

## 📌 **Conclusion**

* **Inheritance** allows a derived class to access attributes and methods from its base class.
* **`super()`** is an important function that helps in calling the constructor of the parent class, thus reusing code and preventing duplication.
* By using `super()`, you ensure that your child class maintains and inherits functionality from the parent class.

