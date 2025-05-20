

### 📄 Custom Iterator: `Countdown` Class



Create a class that implements Python’s iterator protocol using `__iter__()` and `__next__()` methods. The iterator should count down from a given number to 0.

---

## 💡 What is an Iterator?

In Python, an **iterator** is an object that allows you to traverse through all the elements of a collection (like a list or a range) one at a time.

To create a custom iterator:

* Implement the `__iter__()` method that returns the iterator object itself.
* Implement the `__next__()` method that returns the next value in the sequence or raises `StopIteration` when done.

---

## 🧱 Code Explanation

```python
class Countdown:
    def __init__(self, start):
        self.current = start
```

* Initializes the iterator with a starting value.

---

```python
    def __iter__(self):
        return self
```

* Makes the object itself an iterator.

---

```python
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
```

* Returns the current number and decreases it by 1.
* If the value goes below 0, `StopIteration` is raised to signal the end of the loop.

---

## 🔁 Example Usage

```python
countdown = Countdown(5)

for number in countdown:
    print(number)
```




## ✅ Key Concepts

* `__iter__()` returns the iterator object.
* `__next__()` provides the next value each time it's called.
* `StopIteration` is used to stop the iteration.

---

## 📌 Use Case

Custom iterators like `Countdown` are useful when:

* You want to model behavior similar to a loop but with **custom logic**.
* You want to **control the state** of iteration manually.


