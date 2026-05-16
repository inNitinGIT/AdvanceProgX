# Multithreaded Producer–Consumer System Using POSIX Threads

## Overview

This project demonstrates a classic **Producer–Consumer Problem** using **POSIX Threads (pthreads)** in the C programming language.

The program uses:

- Threads for concurrent execution
- Mutex locks for safe shared-memory access
- Condition variables for thread communication and synchronization

It simulates a system where:

- A Producer Thread generates data and inserts it into a shared buffer
- A Consumer Thread removes and processes data from the buffer
- Threads wait correctly when resources are unavailable

---

# Objectives

The main goals of this project are:

- Understand multithreading in C
- Learn synchronization techniques
- Prevent race conditions
- Demonstrate thread communication
- Safely manage shared resources

---

# Concepts Used

## 1. POSIX Threads (pthread)

POSIX threads allow multiple threads to execute concurrently inside the same process.

Functions used:

```c
pthread_create()
pthread_join()
pthread_exit()
```

---

## 2. Shared Resource

The producer and consumer share a common buffer:

```c
int buffer[BUFFER_SIZE];
```

Both threads access this buffer simultaneously, so synchronization is required.

---

## 3. Mutex (Mutual Exclusion)

A mutex ensures that only one thread accesses the critical section at a time.

Functions used:

```c
pthread_mutex_lock()
pthread_mutex_unlock()
```

### Why Mutex Is Needed

Without a mutex:
- Multiple threads may modify shared data together
- Data corruption may occur
- Output becomes unpredictable

With a mutex:
- Shared data remains consistent
- Only one thread enters the critical section

---

## 4. Condition Variables

Condition variables help threads wait until a condition becomes true.

Functions used:

```c
pthread_cond_wait()
pthread_cond_signal()
```

### Conditions Used

| Condition | Action |
|---|---|
| Buffer Full | Producer waits |
| Buffer Empty | Consumer waits |

This avoids:
- Busy waiting
- CPU wastage
- Invalid buffer access

---

# Producer–Consumer Problem

The Producer–Consumer Problem is a classic Operating System synchronization problem.

## Producer
- Produces items
- Inserts items into buffer

## Consumer
- Removes items from buffer
- Consumes items

## Shared Buffer
Acts as temporary storage between producer and consumer.

---

# Program Workflow

## Step 1: Producer Creates Item

```txt
Producer produced item
```

Item is inserted into buffer.

---

## Step 2: Consumer Removes Item

```txt
Consumer consumed item
```

Item is removed from buffer.

---

## Step 3: Synchronization

### If buffer becomes full:
```txt
Producer waiting... Buffer FULL
```

### If buffer becomes empty:
```txt
Consumer waiting... Buffer EMPTY
```

Threads continue execution only after receiving a signal.

---

# Critical Section

A critical section is the part of code where shared resources are accessed.

Example:

```c
pthread_mutex_lock(&mutex);

/* Critical Section */

pthread_mutex_unlock(&mutex);
```

Only one thread can execute this section at a time.

---

# How Synchronization Prevents Inconsistent Behavior

Without synchronization:

- Producer and consumer may access buffer together
- Data may be overwritten
- Consumer may read invalid data
- Race conditions occur

Synchronization solves this by:
- Controlling thread access
- Ensuring ordered execution
- Protecting shared memory

Result:
- Correct output
- Stable execution
- Safe thread communication

---

# Data Structure Concepts Used

This project also demonstrates several DSA concepts.

## Circular Queue

The buffer behaves like a circular queue.

Variables:
```c
in
out
```

Used to:
- Track insertion position
- Track removal position

---

## FIFO (First In First Out)

Items are consumed in the same order they are produced.

Example:
```txt
Produced: 1 2 3
Consumed: 1 2 3
```

---

# Compilation

Compile using GCC:

```bash
gcc producer_consumer.c -o producer_consumer -lpthread
```

---

# Execution

Run the program:

```bash
./producer_consumer
```

---

# Sample Output

```txt
Producer produced: 1 at index 0
Buffer count after produce: 1

Consumer consumed: 1 from index 0
Buffer count after consume: 0

Producer produced: 2 at index 1
Buffer count after produce: 1

Producer produced: 3 at index 2
Buffer count after produce: 2
```

---

# Advantages of Synchronization

- Prevents race conditions
- Maintains data consistency
- Avoids corruption
- Improves thread coordination
- Enables safe concurrent programming

---

# Applications

This concept is widely used in:

- Operating Systems
- Database Systems
- Web Servers
- Task Scheduling
- Parallel Computing
- Real-Time Systems
- Networking Systems

---

# Related OS and DSA Topics

- Multithreading
- Thread Scheduling
- Critical Section Problem
- Mutex Locks
- Semaphores
- Monitors
- Deadlock
- Circular Queue
- FIFO Scheduling
- Concurrent Programming

---

# Conclusion

This project demonstrates how synchronization mechanisms such as mutexes and condition variables help multiple threads safely share resources in a concurrent environment.

The Producer–Consumer model is one of the most important concepts in:
- Operating Systems
- Multithreaded Programming
- Concurrent System Design

By using proper synchronization:
- Race conditions are avoided
- Shared data remains safe
- Threads cooperate efficiently
- Program execution becomes reliable and predictable