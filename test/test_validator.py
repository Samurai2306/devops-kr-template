# tests/test_validator.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone():
    assert validate_phone("+79991234567") == True
    assert validate_phone("89991234567") == False
    assert validate_phone("+7999123") == False


if __name__ == "__main__":
    test_validate_email()
    test_validate_phone()
    print("ok")
