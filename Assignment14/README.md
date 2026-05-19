 # Core Learning Outcome

### This assignment teaches:

1. Memory Management

- How Python stores and deletes objects.

2. Reference Counting

- Python’s primary cleanup method.

3. Circular Reference Problem

- Why reference counting alone is insufficient.

4. Garbage Collection

- How Python solves unreachable cycles.

5. Memory Leak Prevention

- Important for large software systems.



 # Real life analogy
 Imagine:

- Two people holding each other’s hands on an island.

Everyone else leaves.

- Even though nobody can reach them anymore,
they are still connected to each other.

Garbage Collector is like a rescue team that checks:

“Can anyone from the outside reach these people?”

- If not: remove them from memory.


# Output Shown : 
===== Creating Nodes =====

===== Circular Reference Created =====

Reference Count of A: 3
Reference Count of B: 3

===== Deleting A and B =====
Variables A and B deleted

===== Investigating Garbage =====

===== Running Garbage Collector =====

Node A is being garbage collected
Node B is being garbage collected

Unreachable objects collected: 24

Total tracked objects after gc.collect() :5452 