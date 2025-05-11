
## 📘 Constructor & Destructor

### 🔍 Overview:

This assignment focuses on understanding **constructors** and **destructors** in Python through a class named `Logger`.

---

### 🧠 Key Concepts:

#### ✅ Constructor (`__init__`):

* The constructor is a special method that runs **automatically** when an object is created.
* It's often used for initialization tasks.
* In this example, it prints a message: `"Constructor called, object created"`.

#### ✅ Destructor (`__del__`):

* The destructor runs **automatically** when an object is destroyed or goes out of scope.
* It's useful for cleanup tasks like closing files or releasing resources.
* Here, it prints: `"Destructor called, object destroyed"`.

---

### 🧪 How It Works:

1. An object of the `Logger` class is created, which triggers the constructor.
2. The `hello()` method is called to perform an action.
3. When the program ends or the object is deleted, the destructor is triggered and shows the destruction message.

---

### 📊 Summary:

* `__init__()` → Called at **object creation**
* `__del__()` → Called at **object destruction**
* These special methods help manage the lifecycle of an object in a class.

