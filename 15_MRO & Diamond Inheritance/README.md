### 📄 MRO & Diamond Inheritance in Python

* **Multiple inheritance**
* The concept of **diamond inheritance**
* Python’s **MRO (Method Resolution Order)** using the `mro()` method

---

## 🔷 Diamond Inheritance

In **diamond inheritance**, a subclass inherits from two classes that both inherit from a common base class.
This creates a **diamond-shaped hierarchy** like this:

```
       A
      / \
     B   C
      \ /
       D
```

* Class `D` inherits from both `B` and `C`
* Both `B` and `C` inherit from `A`
* This can create ambiguity if not managed properly (e.g., which `show()` method to call?)

---

## 🧠 What is MRO?

**MRO (Method Resolution Order)** is the order in which Python looks for a method in a hierarchy involving multiple inheritance.

Python uses the **C3 Linearization Algorithm** to resolve this.

You can see the MRO using:

```python
print(D.mro())
```

---

## 📦 Code Breakdown

```python
class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    def show(self):
        print("D's show method")

d = D()
d.show()    
print(D.mro())
```
---

## 🔍 Explanation

1. `d.show()` calls the `show()` method from class `D`, because it's defined there.
2. The MRO shows the search path Python follows:

   * First in `D`
   * Then in `B`
   * Then in `C`
   * Then in `A`
   * Finally, the base `object` class

This resolves the ambiguity caused by diamond inheritance **automatically and safely**.

---

## 🧠 Summary

* Python uses **C3 Linearization** to resolve method calls in complex hierarchies.
* Diamond inheritance can be tricky, but Python handles it using **MRO**.
* `D.mro()` gives the exact lookup path, ensuring predictable behavior.

