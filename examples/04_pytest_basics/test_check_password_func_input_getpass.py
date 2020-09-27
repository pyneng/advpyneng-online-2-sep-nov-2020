from check_password_function_input import check_passwd
import pytest


@pytest.mark.parametrize(
    "user,passwd,min_len,result",
    [
        ("user1", "123456", 4, True),
        ("user1", "123456", 8, False),
        ("user1", "123456", 6, True),
    ]
)
def test_check_passwd(monkeypatch, user, passwd, min_len, result):
    monkeypatch.setattr("builtins.input", lambda x=None: user)
    monkeypatch.setattr("getpass.getpass", lambda x=None: passwd)
    assert check_passwd(min_length=min_len) == result
