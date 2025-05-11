
### 📄 Instance Method

---

## 🧾 Assignment Description

**Objective:**
Create a class `Dog` that includes:

* Two instance variables: `name` and `breed`
* An instance method: `bark()` that prints a message including the dog's name

This assignment helps reinforce the concept of **instance variables** and **instance methods** in object-oriented programming using Python.

---

## 🧠 Key Concepts

### 🐾 Instance Variables

Instance variables are specific to each object created from a class. In this case:

* `self.name` stores the name of the dog.
* `self.breed` stores the breed of the dog.

Each object (`dog1`, `dog2`) maintains its own values.

### 🐾 Instance Method

The method `bark()` is defined to simulate the dog barking. It uses the instance variable `self.name` to personalize the message.

```python
def bark(self):
    print(f"{self.name} says Woof!")
```

---

## 🔧 How It Works

```python
dog1 = Dog("Candy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
```

* Two objects are created from the `Dog` class.
* Each has its own `name` and `breed`.

```python
dog1.bark()  
dog2.bark()  
```

Calling the `bark()` method on each instance prints a message including the specific dog's name.

---


## 📌 Summary

This example shows how to:

* Create multiple instances of a class
* Assign and use instance-specific data
* Define behavior using instance methods




