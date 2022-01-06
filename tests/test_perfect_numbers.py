from scripts.perfect_numbers import *


def test_find_factrors_15():
    assert find_factors(15) == [1, 3, 5]


def test_perfect_numbers_15_returns_15sfactors():
    assert aliquot_sum(15) == 9


def test_nics_cat_6_perfect():
    assert nics_cat(6) == "Perfect"


def test_nics_cat_28_perfect():
    assert nics_cat(28) == "Perfect"
