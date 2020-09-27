from check_password_function_input import check_passwd
import pytest


def monkey_input(prompt):
    if "Username" in prompt:
        return "user1"
    else:
        return "12345"


def test_check_passwd(monkeypatch):
    monkeypatch.setattr("builtins.input", monkey_input)
    assert check_passwd(min_length=4) == True


