from scripts.perfect_numbers import *


def test_find_factrors_15():
    assert find_factors(15) == [1, 3, 5]


def test_perfect_numbers_15_returns_15sfactors():
    assert aliquot_sum(15) == 9


def test_nics_cat_15_deficient():
    assert nics_cat(15) == "Deficient"


def test_nics_cat_6_perfect():
    assert nics_cat(6) == "Perfect"
