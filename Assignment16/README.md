
![C](https://img.shields.io/badge/language-C-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

# Multithreaded Producer–Consumer System Using POSIX Threads and Semaphores

## Overview

This project demonstrates the classic **Producer–Consumer Problem** using:

- POSIX Threads (`pthread`)
- Semaphores (`semaphore.h`)
- Mutex Locks

The program simulates a concurrent system where:

- A Producer Thread generates items
- A Consumer Thread consumes items
- A shared buffer is used for communication
- Threads synchronize safely using semaphores

The implementation ensures:

- Safe shared-memory access
- Proper thread synchronization
- Correct waiting and signaling mechanism
- Prevention of race conditions

---

# Objectives

The main objectives of this project are:

- Understand multithreading in C
- Learn thread synchronization
- Implement semaphores in concurrent programming
- Prevent inconsistent behavior
- Coordinate producer and consumer execution
- Safely manage shared resources

---

# Concepts Used

## 1. POSIX Threads (pthread)

POSIX threads allow multiple threads to execute concurrently within the same process.

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

Shared variables:

```c
int in;
int out;
```

Because multiple threads access these variables simultaneously, synchronization is necessary.

---

## 3. Mutex (Mutual Exclusion)

A mutex protects the critical section from simultaneous access.

Functions used:

```c
pthread_mutex_lock()
pthread_mutex_unlock()
```

### Why Mutex Is Needed

Without a mutex:
- Threads may modify shared memory together
- Data corruption may occur
- Output becomes unpredictable

With a mutex:
- Only one thread enters the critical section
- Shared data remains safe and consistent

---

# 4. Semaphores

Semaphores are synchronization tools used to control access to shared resources.

Header file used:

```c
#include <semaphore.h>
```

Functions used:

```c
sem_init()
sem_wait()
sem_post()
sem_destroy()
```

---

## Types of Semaphores Used

### 1. Empty Semaphore

```c
sem_t empty;
```

Tracks available empty slots in the buffer.

Initially:

```txt
BUFFER_SIZE
```

Producer waits if buffer becomes full.

---

### 2. Full Semaphore

```c
sem_t full;
```

Tracks filled slots in the buffer.

Initially:

```txt
0
```

Consumer waits if buffer becomes empty.

---

# Producer–Consumer Problem

The Producer–Consumer Problem is a classic synchronization problem in Operating Systems.

## Producer
- Produces data/items
- Inserts items into shared buffer

## Consumer
- Removes items from buffer
- Consumes the produced data

## Shared Buffer
Acts as temporary storage between producer and consumer threads.

---

# Program Workflow

## Step 1: Producer Waits for Empty Slot

```c
sem_wait(&empty);
```

If no empty slot exists:
- Producer thread waits

---

## Step 2: Producer Produces Item

```txt
Producer produced item
```

Item is inserted into buffer safely.

---

## Step 3: Producer Signals Consumer

```c
sem_post(&full);
```

Indicates:
- New item is available for consumption

---

## Step 4: Consumer Waits for Filled Slot

```c
sem_wait(&full);
```

If buffer is empty:
- Consumer thread waits

---

## Step 5: Consumer Consumes Item

```txt
Consumer consumed item
```

Item is removed from buffer safely.

---

## Step 6: Consumer Signals Producer

```c
sem_post(&empty);
```

Indicates:
- Empty slot is available again

---

# Critical Section

A critical section is the portion of code where shared resources are accessed.

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

- Producer and consumer may access buffer simultaneously
- Data may be overwritten
- Consumer may read invalid data
- Race conditions occur

Synchronization prevents these problems by:
- Controlling thread access
- Managing resource availability
- Ensuring safe execution order

Result:
- Correct program execution
- Safe shared-memory access
- Predictable output

---

# Semaphore Working Example

Suppose:

```txt
BUFFER_SIZE = 5
```

Initially:

```txt
empty = 5
full = 0
```

---

## Producer Inserts One Item

```txt
sem_wait(empty)
empty = 4
```

After producing:

```txt
sem_post(full)
full = 1
```

Meaning:
- One item is available

---

## Consumer Removes One Item

```txt
sem_wait(full)
full = 0
```

After consuming:

```txt
sem_post(empty)
empty = 5
```

Meaning:
- One empty slot becomes available

---

# Data Structure Concepts Used

This project also demonstrates several DSA concepts.

---

## Circular Queue

The buffer behaves like a circular queue.

Variables used:

```c
in
out
```

Purpose:
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
gcc producer_consumer_semaphore.c -o producer_consumer_semaphore -lpthread
```

---

# Execution

Run the program:

```bash
./producer_consumer_semaphore
```

---

# Sample Output

```txt
Producer produced: 1 at index 0
Consumer consumed: 1 from index 0

Producer produced: 2 at index 1
Producer produced: 3 at index 2

Consumer consumed: 2 from index 1
Consumer consumed: 3 from index 2
```

---

# Advantages of Semaphores

- Prevent race conditions
- Coordinate thread execution
- Manage resource allocation
- Avoid busy waiting
- Improve concurrent processing
- Enable safe communication between threads

---
