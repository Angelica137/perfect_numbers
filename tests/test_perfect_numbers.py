from scripts.perfect_numbers import perfect_numbers


def test_perfect_numbers_1_returns_1():
    assert perfect_numbers(1) == 1


def test_perfect_numbers_15_returns_15sfactors():
    assert perfect_numbers(15) == [1, 3, 5]
