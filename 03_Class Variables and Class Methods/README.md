## 📘 Using Class Method and Class Variable

### 🔍 Overview:

This assignment defines a `Bank` class with a shared class variable called `bank_name`. The main goal is to demonstrate how a `@classmethod` can be used to change this variable and reflect the update across all instances of the class.

---

### 🧠 Key Concepts:

#### ✅ Class Variable (`bank_name`):

* A class variable is shared among all objects created from the class.
* In this case, `bank_name` represents the name of the bank and is common to every `Bank` object.
* If it's changed, the new value becomes visible to **all instances**, whether existing or new.

#### ✅ Instance Variable (`self.name`):

* This is unique to each object and stores data specific to that object only.
* It doesn't affect or get affected by class variables.

#### ✅ Class Method (`@classmethod`):

* A class method is defined using the `@classmethod` decorator.
* It takes `cls` (the class itself) as the first parameter instead of `self`.
* It can access and modify class-level data like `bank_name`.
* When the method `change_bank_name` is called, it updates the class variable for all objects.

---

### 🧪 How It Works:

1. The class starts with a default bank name.
2. An object is created and displays this default name.
3. The `change_bank_name` method is used to update the bank name.
4. The same object (and any others) now reflect the new bank name, showing that the change applied globally.

---

### 📊 Summary:

* `self` → Refers to the individual object and its unique data.
* `cls` → Refers to the class and is used in class methods.
* `@classmethod` → Used when you want to modify or work with class-level data.
* `bank_name` → A shared variable, updated through the class method, affects all instances.

