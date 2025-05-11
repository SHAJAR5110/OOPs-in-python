
## 📘 Using `cls` and Class Variable

### 🔍 Overview:

This assignment defines a `Car` class that stores details like name, color, and model year for each car. It also keeps track of how many car objects have been created using a class-level variable. To access this count, a `@classmethod` is used.

---

### 🧠 Key Concepts Explained:

#### ✅ Instance Variables (`self`):

* Each car object stores its own unique `name`, `color`, and `year`.
* The `self` keyword refers to the specific object being created or used.
* It allows each object to maintain its own data, separate from other objects.

#### ✅ Class Variable (`count`):

* The `count` variable is shared among all car objects — it's not unique per object.
* Every time a new car is created, this counter increases by 1.
* It helps track the **total number of car instances** created so far.

#### ✅ Class Method (`@classmethod`):

* This method uses `cls` instead of `self`, which refers to the class itself.
* It is used to access or modify class-level data like `count`.
* In this case, it's used to display how many car objects have been created in total.

---

### 🧪 How It Works:

1. Before any car is created, the count is 0.
2. As new car objects are created, the count increases by 1 each time.
3. The `car_count` class method can be called at any time to display the total number of cars.

---

### 📊 Summary:

* `self` → Refers to the specific object (used for object-specific data).
* `cls` → Refers to the class itself (used for class-level data).
* `@classmethod` → A special method that works with the class, not with a single object.
* `count` → A class variable that tracks how many car objects have been created.


