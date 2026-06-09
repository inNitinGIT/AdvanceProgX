import pytest

from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


# =========================================================
# FIXTURE
# =========================================================

@pytest.fixture
def service():
    return RegistrationService()


# =========================================================
# VALID REGISTRATION TESTS
# =========================================================

def test_valid_registration_1(service):

    result = service.register_user(
        "nitin@gmail.com",
        22
    )

    assert result is True


def test_valid_registration_2(service):

    result = service.register_user(
        "alphaNumber@gmail.com",
        25
    )

    assert result is True


# =========================================================
# INVALID EMAIL TESTS
# =========================================================

@pytest.mark.parametrize("bad_email", [

    "nitin@gmail",
    "nitin.com",
    "@gmail.com",
    "nitin@",
    "nitin@.com",
    "nitin gmail.com",
    "plainaddress"

])
def test_invalid_email(service, bad_email):

    with pytest.raises(InvalidEmailError):

        service.register_user(
            bad_email,
            22
        )


# =========================================================
# UNDERAGE TEST
# =========================================================

def test_underage_user(service):

    with pytest.raises(UnderageError):

        service.register_user(
            "nitin@gmail.com",
            15
        )


# =========================================================
# NEGATIVE AGE TEST
# =========================================================

def test_negative_age(service):

    with pytest.raises(AssertionError):

        service.register_user(
            "nitin@gmail.com",
            -1
        )


# =========================================================
# INVALID AGE TYPE TEST
# =========================================================

def test_invalid_age_type(service):

    with pytest.raises(AssertionError):

        service.register_user(
            "nitin@gmail.com",
            "twenty"
        )


# =========================================================
# INVALID EMAIL TYPE TEST
# =========================================================

def test_invalid_email_type(service):

    with pytest.raises(AssertionError):

        service.register_user(
            12345,
            22
        )