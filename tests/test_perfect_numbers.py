from scripts.perfect_numbers import *

import pytest


def test_perfect_numbers_15_returns_15sfactors():
    assert aliquot_number(15) == 9


def test_nics_cat_6_perfect():
    assert nics_cat(6) == "Perfect"


def test_nics_cat_28_perfect():
    assert nics_cat(28) == "Perfect"


def test_nics_cat_12_abundant():
    assert nics_cat(12) == "Abundant"


def test_nics_cat_24_abundant():
    assert nics_cat(24) == "Abundant"


def test_nics_cat_0_exception():
    with pytest.raises(ValueError, match=r"Classification is only possible for positive integers."):
        nics_cat(0)


def test_nics_cat_neg1_exception():
    with pytest.raises(ValueError, match=r"Classification is only possible for positive integers."):
        nics_cat(-1)
