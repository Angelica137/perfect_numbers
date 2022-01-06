from scripts.perfect_numbers import perfect_numbers


def test_perfect_numbers_15_returns_15sfactors():
    assert perfect_numbers(15) == 9


def test_nics_cat_15_deficient():
    assert nics_cat(15) == "Deficient"
