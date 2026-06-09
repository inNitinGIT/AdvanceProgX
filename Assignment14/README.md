

![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

# Assignment 14: Garbage Collection and Circular References in Python

## Objective

Demonstrate how objects can become "dead" (no longer directly accessible from the program) while still having a reference count greater than zero due to a circular reference. Then, use Python's Garbage Collector to detect and clean up these unreachable objects.

---

## Background

Python primarily manages memory using **reference counting**. An object is normally destroyed when its reference count reaches zero.

However, circular references can create situations where objects reference each other, keeping their reference counts above zero even when all external references are removed. These objects become unreachable but remain in memory until Python's **Garbage Collector (GC)** identifies and removes them.

---

## Requirements

### 1. Create a `Node` Class

Create a class named `Node` with:

- A `name` attribute
- A `link` attribute (initialized to `None`)

Example structure:

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.link = None