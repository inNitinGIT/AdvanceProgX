import re


# =========================================================
# CUSTOM EXCEPTIONS
# =========================================================

class InvalidEmailError(ValueError):
    """
    Raised when email format is invalid.
    """

    def __init__(self, email):
        super().__init__(
            f"Invalid email format: {email}"
        )


class UnderageError(Exception):
    """
    Raised when user's age is below minimum age.
    """

    def __init__(self, age):
        super().__init__(
            f"User age {age} is below 18."
        )


# =========================================================
# REGISTRATION SERVICE
# =========================================================

class RegistrationService:

    # Valid Email Pattern
    EMAIL_PATTERN = (
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def register_user(self, email: str, age: int) -> bool:

        # =================================================
        # ASSERTIONS / INVARIANTS
        # =================================================

        assert isinstance(email, str), \
            "Email must be string"

        assert isinstance(age, int), \
            "Age must be integer"

        assert age >= 0, \
            "Age cannot be negative"

        # =================================================
        # EMAIL VALIDATION
        # =================================================

        if not re.fullmatch(self.EMAIL_PATTERN, email):
            raise InvalidEmailError(email)

        # =================================================
        # AGE VALIDATION
        # =================================================

        if age < 18:
            raise UnderageError(age)

        # =================================================
        # SUCCESS
        # =================================================

        return True


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    service = RegistrationService()

    try:

        # User Input
        email = input("Enter Email: ")
        age = int(input("Enter Age: "))

        # Validation
        result = service.register_user(email, age)

        if result:
            print("Registration Successful!")

    # =====================================================
    # EXCEPTION HANDLING
    # =====================================================

    except InvalidEmailError as e:
        print("Email Error:", e)

    except UnderageError as e:
        print("Age Error:", e)

    except AssertionError as e:
        print("Assertion Error:", e)

    except ValueError:
        print("Age must be a valid integer.")

    except Exception as e:
        print("Unexpected Error:", e)