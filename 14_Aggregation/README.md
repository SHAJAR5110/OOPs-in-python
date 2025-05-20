
### 📄 Aggregation in Python 


**Objective:**
Create a class `Employee` and a class `Department`. Demonstrate **aggregation** by having a `Department` object store a reference to an already existing `Employee` object.

---

## 🧠 Key Concept: Aggregation

**Aggregation** is a type of relationship in object-oriented programming where:

* One class **has-a** reference to another class.
* The associated object (e.g., `Employee`) is **created independently** and **can exist without** the container object (e.g., `Department`).
* This allows for **reusability and loose coupling** between classes.

In this example:

* The `Department` class is **not responsible** for creating the `Employee` object.
* It simply **uses** an already existing instance.

---

## 🧱 Code Structure

* `Employee` class:

  * Has instance variables `name` and `emp_id`.
  * Has a method `display_info()` to show employee details.

* `Department` class:

  * Has a `dept_name` and holds a reference to an `Employee` object via aggregation.
  * Uses the `employee` object's method to display information.

---

This output shows that the `Department` is displaying its own information along with details of the **independent `Employee` object**.

---

## 📌 Summary

* Aggregation is used to build complex structures by linking objects.
* The lifetime of the aggregated object (`Employee`) is **not dependent** on the container (`Department`).
* Promotes flexibility, reusability, and clean separation of concerns.

