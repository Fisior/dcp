from Exercises import binary_addition
from Exercises.binary_addition import add_binary


def test_add_binary():
    assert add_binary(1, 1) == "10"
    assert add_binary(1, 0) == "1"
    assert add_binary(2, 2) == "100"
    assert add_binary(51, 12) == "111111"
