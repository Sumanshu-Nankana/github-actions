from src import app


def test_addition_with_two_numbers():
    result = app.addition(2, 3)
    assert result == 5


def test_addition_with_negative_numbers():
    result = app.addition(-1, 3, -2)
    assert result == 0


def test_addition_with_single_number():
    result = app.addition(-1)
    assert result == -1


# Forcing this Test to Fail
def test_addition_with_zero_number():
    result = app.addition()
    assert result == 1
