# Assignment: File Processing, Exception Handling, and Unit Testing

## Problem Statement

Generally, handling external files is a common source of runtime errors. Files might be missing, or they might contain corrupted data. For this assignment, you will create a simple data utility class that reads an integer value from a text file, performs a calculation, and ensures all system resources are properly closed afterward—even if something goes wrong.

Your program needs to read a numeric score from a file, multiply it by 10, and return the result. If the file does not exist, the system must catch that error and notify the user with a specific message. If the file exists but contains letters instead of a number, the system must handle that invalid data format gracefully. Finally, you must write basic automated tests to verify that your calculation works and that bad inputs are handled correctly.

## Implementation Rules

### If choosing Java:

Create a class named `ScoreProcessor`.

Write a method:

```java
public int processScoreFile(String filePath)
```

that uses a try-catch-finally block (or a try-with-resources block) to open and read a file.

Catch:

* `FileNotFoundException`
* `NumberFormatException`

specifically, logging or printing a clear error message for each.

Use the finally block to print a:

```text
File cleanup completed
```

message to the console.

Write a JUnit 5 test suite with at least two test cases:

1. One verifying a successful calculation with a valid file path.
2. One using `assertThrows` to check how the system reacts to a missing file.

---

### If choosing Python:

Create a class named `ScoreProcessor`.

Write a method:

```python
def process_score_file(self, file_path: str) -> int
```

that uses a try-except-else-finally block to open and read a file.

Catch:

* `FileNotFoundError`
* `ValueError`

specifically, printing a helpful error message for each.

Use the else block to print:

```text
Data processed successfully
```

and use the finally block to print:

```text
File cleanup completed
```

Write a pytest suite with at least two test functions:

1. One testing a successful calculation with a valid file.
2. One using `with pytest.raises` to verify that a missing file is handled correctly.

## You must have the followings:

### Exception Handling & Structure

* Correctly implementing the multi-catch structure (FileNotFound and Invalid Format/Value errors).
* Ensuring the cleanup block executes under all conditions.

### Core Logic & Input Validation

* Successfully reading the file content.
* Parsing the text into a usable integer.
* Executing the required multiplication calculation.

### Unit Testing

* Setting up a working test suite.
* Using correct framework assertions to validate both:

  * The happy path (successful calculation).
  * The error path (missing file).
