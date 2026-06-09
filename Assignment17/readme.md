# Assignment 17: User Onboarding Validation Module

## Objective

Build a user onboarding validation module for a platform. Your objective is to create a core validation class that processes incoming application data—specifically a user's email address and age—and enforces strict business constraints before allowing a registration to complete.

## Requirements

The system must ensure that the email string is neither null nor empty, and that it conforms to a standard email format matching the regular expression patterns outlined in the slides (containing a valid identifier, an @ symbol, and a domain name).

Additionally, the system must enforce a strict age restriction where applicants must be at least 18 years old to create an account.

## Implementation Rules

### If choosing Java

You must implement a checked exception named `InvalidEmailException` and an unchecked (`RuntimeException`) exception named `UnderageException`.

Create a `RegistrationService` class containing a method:

```java
public boolean registerUser(String email, int age) throws InvalidEmailException
```

You must include an internal assert statement to guarantee that the inputs are not processed if the system context is invalid.

Finally, write a JUnit 5 test suite named `RegistrationServiceTest` that:

* Uses a `@BeforeEach` setup method
* Validates successful registrations
* Uses `assertThrows` to verify that both custom exceptions are thrown under incorrect conditions

### If choosing Python

You must implement a custom exception named `InvalidEmailError` and another named `UnderageError`, both inheriting from the appropriate built-in exception classes.

Create a `RegistrationService` class containing a method:

```python
def register_user(self, email: str, age: int) -> bool
```

Use an internal assert statement to verify basic state invariants.

Finally, write a pytest suite:

* Using a shared `@pytest.fixture` for configuration
* Validating successful workflows
* Utilizing `pytest.raises` to assert that your custom errors are raised appropriately during invalid inputs

## You must have the followings

### Custom Exception Design

* Correctly establishing checked vs. unchecked hierarchies (Java) or appropriate base class inheritance (Python)
* With descriptive, dynamic error messages

### Core Service Validation

* Implementing the regex parsing
* Age boundary checks
* Invariant assertions
* Proper exception triggering

### Unit Testing Suite

* Writing comprehensive test cases using the correct framework assertions
* Proper test lifecycle setup (fixtures/before-each)
* Targeted exception testing
