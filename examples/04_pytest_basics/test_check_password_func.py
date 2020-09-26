from check_password_function import check_passwd


def test_min_len():
    assert check_passwd("user1", "12345", min_length=3) == True
    assert check_passwd("user1", "12345", min_length=8) == False
    assert check_passwd("user1", "12345", min_length=5) == True


def test_passwd_contains_username():
    assert check_passwd("user1", "12345", min_length=5, check_username=True) == True
    assert (
        check_passwd("user1", "12345user1345", min_length=5, check_username=True)
        == False
    )
