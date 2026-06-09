![C](https://img.shields.io/badge/language-C-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
# Assignment10: Student Management System Using Composition, Properties, and Inheritance

Design a student system in Python with:

* `Address` class (`street`, `city`, `zipCode`)
* `Student` class with `name`, `age`, `Address`, and course list
* Store age as a protected attribute and control it using `@property`
* Methods: `add_course()` and `display()`

Extend it with:

* `ScholarshipStudent` (add `scholarshipAmount` and override `display()`)

Your implementation should clearly show:

### 1. Composition

* `Student` HAS-A `Address`

### 2. Proper Data Validation Using `@property`

* Age must be valid

### 3. Inheritance and Method Overriding

* Override `display()` in `ScholarshipStudent`
* Use `super()` in `display()`

### 4. Understanding of Mutable Behavior

* Course list updates persist across operations
