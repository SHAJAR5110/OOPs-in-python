

### 📄 Class Methods 


## 🧠 Key Concepts

### 🔹 Class Variable

A **class variable** is shared across all instances of the class. In this example:

```python
total_books = 0
```

This keeps track of how many `Book` objects have been created, and it's incremented inside the constructor (`__init__()` method).

### 🔹 Class Method

A **class method** is defined using the `@classmethod` decorator and takes `cls` as its first argument (instead of `self`). It can access and modify class-level data.

```python
@classmethod
def increment_book_count(cls):
    print(f"Total books: {cls.total_books}")
```

---

## 🧪 How It Works

```python
book1 = Book("Book 1")
book2 = Book("Book 2")
book3 = Book("Book 3")
```

Each time a book is created, the `total_books` variable is increased by 1.

```python
Book.increment_book_count()
```

This prints the total number of books created.

---



## 📌 Summary

* `total_books` is a class variable shared by all instances.
* The `increment_book_count()` method uses the `cls` parameter to access that shared variable.
* This pattern is useful for tracking the number of instances or maintaining class-level state.


