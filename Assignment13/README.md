![C](https://img.shields.io/badge/language-C-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

# Assignment 13: Dynamic String Buffer in C

## Objective

Implement a Dynamic String Buffer in C that automatically expands its storage capacity as strings are appended. The goal is to practice safe dynamic memory management using `malloc`, `realloc`, and `free`, while avoiding common issues such as buffer overflows and memory leaks.

---

## Background

String handling in C requires manual memory management. Fixed-size character arrays can easily lead to buffer overflows when more data is written than the allocated space can hold. A dynamic string buffer solves this problem by automatically increasing its capacity whenever additional space is needed.

This assignment focuses on building a reusable string buffer that grows dynamically and properly releases all allocated memory when it is no longer needed.

---

## Requirements

### 1. Define the StringBuffer Structure

Create a structure named `StringBuffer` containing the following members:

* `char *data` – Pointer to the dynamically allocated character buffer.
* `size_t length` – Current length of the string stored in the buffer.
* `size_t capacity` – Total allocated capacity of the buffer.

---

### 2. Implement Initialization Function

Create a function:

```c
StringBuffer *sb_init(size_t initial_capacity);
```

Responsibilities:

* Allocate memory for the `StringBuffer` structure on the heap.
* Allocate memory for the internal character buffer using the provided initial capacity.
* Initialize all structure members appropriately.
* Handle memory allocation failures safely.
* Return `NULL` if allocation fails.

---

### 3. Implement Append Function

Create a function:

```c
void sb_append(StringBuffer *sb, const char *str);
```

Responsibilities:

* Append the given string to the existing buffer content.
* Update the current length accordingly.
* Ensure the buffer always remains properly null-terminated.

---

### 4. Automatic Buffer Growth

When appending data causes the required storage size to exceed the current capacity:

* Increase the capacity by doubling it.
* Use `realloc()` to resize the buffer.
* Handle `realloc()` safely:

  * Do not overwrite the original pointer until reallocation succeeds.
  * Prevent memory loss if `realloc()` returns `NULL`.

---

### 5. Implement Destructor Function

Create a function:

```c
void sb_free(StringBuffer *sb);
```

Responsibilities:

* Free the internal character buffer.
* Free the `StringBuffer` structure itself.
* Ensure all dynamically allocated memory is properly released.
* Prevent memory leaks.

---

## Demonstration Requirements

Write a test program that:

1. Creates a string buffer with a small initial capacity.
2. Appends multiple strings to the buffer.
3. Causes the buffer to grow dynamically at least **two times**.
4. Displays relevant information such as:

   * Current string content
   * Current length
   * Current capacity
5. Frees all allocated memory before program termination.

---

## Error Handling

Your implementation should:

* Check all memory allocation operations.
* Handle allocation failures gracefully.
* Avoid buffer overflows.
* Prevent memory leaks.
* Use safe memory management practices throughout the program.

---

## Learning Outcomes

After completing this assignment, you should be able to:

* Design and use dynamic data structures in C.
* Allocate and manage heap memory safely.
* Use `malloc`, `realloc`, and `free` correctly.
* Prevent buffer overflows through dynamic resizing.
* Implement safe resource cleanup using destructor-style functions.
* Understand common memory management pitfalls in C programs.

---

## Deliverables

Submit:

1. Source code implementing the `StringBuffer` structure and required functions.
2. A demonstration program showing dynamic growth of the buffer.
3. Evidence that all allocated memory is properly released.
4. Any necessary build and execution instructions.

---

## Expected Outcome

The final program should successfully:

* Store and append strings dynamically.
* Automatically expand capacity when needed.
* Grow the buffer at least twice during execution.
* Manage memory safely without leaks.
* Clean up all resources before exiting.
