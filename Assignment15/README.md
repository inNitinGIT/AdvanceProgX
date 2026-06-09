
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

# Multithreaded Counter Using POSIX Threads (Pthreads)

This project demonstrates how race conditions occur in multithreaded programs and how mutex synchronization solves the problem using POSIX threads (`pthread`) in C.

The project contains two programs:

- `race_condition.c`
- `mutex_counter.c`

---

# 📌 Project Objective

The purpose of this project is to understand:

- How multiple threads work
- What shared memory is
- Why race conditions occur
- What a critical section is
- How mutex synchronization prevents data corruption

---

# 📂 Project Files

| File | Description |
|---|---|
| `race_condition.c` | Demonstrates race condition without synchronization |
| `mutex_counter.c` | Solves race condition using mutex locking |

---

# 📌 What is Multithreading?

Multithreading means running multiple threads inside a single process simultaneously.

A thread is a lightweight unit of execution.

Instead of performing one task at a time, threads allow programs to execute multiple tasks concurrently.

In this project:

- Multiple threads update the same counter variable
- All threads run concurrently
- Shared data is accessed by multiple threads

---

# 📌 Shared Variable

Both programs use a shared global variable:

```c
long long counter = 0;
```

This variable is shared among all threads.

Every thread reads and modifies the same memory location.

---

# 1️⃣ Race Condition Program

## 📄 File
`race_condition.c`

---

# 📌 What Happens in This Program?

This program creates multiple threads.

Each thread increments the shared counter many times.

However, there is NO synchronization mechanism protecting the counter.

Because of this:

- Multiple threads access the counter simultaneously
- Updates overwrite each other
- Final output becomes incorrect

---

# 📌 Why Does Race Condition Occur?

The statement:

```c
counter++;
```

looks like a single operation, but internally it performs:

```text
1. Read counter value
2. Increment value
3. Write updated value back
```

These steps are not executed atomically.

---

# 📌 Example of the Problem

Suppose:

```text
counter = 100
```

Two threads execute together.

### Thread A
```text
Reads counter = 100
```

### Thread B
```text
Reads counter = 100
```

### Thread A
```text
Increments and writes 101
```

### Thread B
```text
Also writes 101
```

Expected value:

```text
102
```

Actual value:

```text
101
```

One increment is lost.

This problem is called a:

# ⚠️ Race Condition

A race condition occurs when multiple threads access shared data simultaneously and the program result depends on execution timing.

---

# 📌 Expected Output

Expected counter value:

```text
4000000
```

Actual output may look like:

```text
2573841
```

The output changes every run because thread scheduling changes every time.

---

# 2️⃣ Mutex Synchronization Program

## 📄 File
`mutex_counter.c`

---

# 📌 What is Different in This Program?

This program solves the race condition using a mutex.

A mutex ensures that only one thread can access the critical section at a time.

---

# 📌 What is a Critical Section?

A critical section is the part of code where shared data is accessed.

In this project:

```c
counter++;
```

is the critical section.

---

# 📌 How Mutex Works

Before updating the counter, the thread locks the mutex:

```c
pthread_mutex_lock(&lock);
```

This prevents other threads from entering the critical section.

After updating the counter, the mutex is unlocked:

```c
pthread_mutex_unlock(&lock);
```

Now another thread can access the shared variable safely.

---

# 📌 Why Mutex Solves the Problem

Without mutex:

- Multiple threads modify data simultaneously
- Updates are lost
- Data corruption occurs

With mutex:

- Only one thread accesses the shared variable at a time
- Operations become synchronized
- Final output becomes correct

---

# 📌 Expected Output

```text
Final Counter Value: 4000000
Expected Value: 4000000
```

The output remains correct every time.

---

# 📌 Pthread Functions Used

| Function | Purpose |
|---|---|
| `pthread_create()` | Creates a new thread |
| `pthread_join()` | Waits for thread completion |
| `pthread_mutex_init()` | Initializes mutex |
| `pthread_mutex_lock()` | Locks mutex |
| `pthread_mutex_unlock()` | Unlocks mutex |
| `pthread_mutex_destroy()` | Destroys mutex |

---

# 📌 Compilation

## Compile Race Condition Program

```bash
gcc race_condition.c -o race_condition -pthread
```

---

## Compile Mutex Program

```bash
gcc mutex_counter.c -o mutex_counter -pthread
```

---

# 📌 Execution

## Run Race Condition Program

```bash
./race_condition
```

---

## Run Mutex Program

```bash
./mutex_counter
```

---

# 📌 Key Concepts Learned

This project helps understand:

- Threads
- Multithreading
- Shared Memory
- Race Conditions
- Critical Sections
- Mutex Locks
- Synchronization
- Concurrency
- Parallel Processing

---

# 📌 Conclusion

This project demonstrates one of the most important problems in concurrent programming: race conditions.

The first program shows how unsynchronized access to shared data leads to incorrect results.

The second program solves the problem using mutex synchronization, ensuring safe access to shared resources.

Understanding synchronization is essential for developing reliable multithreaded applications.