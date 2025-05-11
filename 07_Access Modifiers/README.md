
### 📄  Access Modifiers in Python 

---

## 🧾 Overview

This assignment demonstrates the concept of **access modifiers** in Python using a class called `Employee`.
The class includes:

* A **public** variable: `name`
* A **protected** variable: `_salary`
* A **private** variable: `__ssn`

We create an object of the class and try accessing all three types of variables from outside the class to observe their behavior.

---

## 🧪 Code Explanation

```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


obj1 = Employee("Shajar Abbas", 50000, "123-45-6789")

public = obj1.name
protected = obj1._salary
private = obj1.__ssn  # This will raise an AttributeError
private_that_works = obj1._Employee__ssn

print(f"Private variable that works: {private_that_works}")
print(f"Public variable: {public} \nProtected variable: {protected} \nPrivate variable: {private}")
```

---

## 🔍 Access Modifiers Explained

### ✅ Public Variable (`name`)

* Defined without any underscore: `self.name`
* Can be accessed and modified **freely** from anywhere.
* Accessing: `obj1.name` → ✅ Works

### ⚠️ Protected Variable (`_salary`)

* Defined with a **single underscore**: `self._salary`
* Intended to be **used within the class or its subclasses**.
* Can still be accessed from outside the class, but **it's discouraged by convention**.
* Accessing: `obj1._salary` → ✅ Works

### 🔒 Private Variable (`__ssn`)

* Defined with **double underscores**: `self.__ssn`
* Python performs **name mangling**, changing the variable name internally to `_ClassName__varname`.
* Direct access like `obj1.__ssn` → ❌ **Raises `AttributeError`**
* Correct access: `obj1._Employee__ssn` → ✅ Works

---

## 🧨 What Happens on Direct Private Access?

In the line:

```python
private = obj1.__ssn  # This will raise an AttributeError
```

You’ll get an error like:

```bash
AttributeError: 'Employee' object has no attribute '__ssn'
```

This is because Python changes `__ssn` internally to `_Employee__ssn`, making it **inaccessible by its original name from outside**.

---

## ✅ Output (If You Comment Out the Error Line)

If the line causing the error is removed or commented, the output will be:

```
Private variable that works: 123-45-6789
Public variable: Shajar Abbas 
Protected variable: 50000 
Private variable: 123-45-6789
```

---

## 📌 Conclusion

This exercise shows how Python handles variable access control:

| Type      | Syntax    | Accessible Outside? | Notes                               |
| --------- | --------- | ------------------- | ----------------------------------- |
| Public    | `name`    | ✅ Yes               | Freely accessible                   |
| Protected | `_salary` | ⚠️ Yes              | Accessible but discouraged          |
| Private   | `__ssn`   | ❌ No (directly)     | Use name mangling: `_Employee__ssn` |


