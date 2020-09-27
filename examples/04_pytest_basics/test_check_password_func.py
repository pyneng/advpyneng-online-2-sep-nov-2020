from check_password_function import check_passwd
import pytest


@pytest.mark.parametrize(
    ("user", "passwd", "min_len", "result"),
    [
        ("user1", "123456", 4, True),
        ("user1", "123456", 8, False),
        ("user1", "123456", 6, True),
    ],
)
def test_min_len_param(user, passwd, min_len, result):
    assert check_passwd(user, passwd, min_length=min_len) == result


def test_stdout(capsys):
    assert check_passwd("user1", "12345", min_length=5, check_username=True) == True
    out, err = capsys.readouterr()
    assert "Пароль для пользователя прошел все проверки" in out
