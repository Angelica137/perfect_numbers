from scripts.perfect_numbers import *

import pytest


def test_nics_cat_6_perfect():
    assert nics_cat(6) == "perfect"


def test_nics_cat_28_perfect():
    assert nics_cat(28) == "perfect"


def test_nics_cat_12_abundant():
    assert nics_cat(12) == "abundant"


def test_nics_cat_24_abundant():
    assert nics_cat(24) == "abundant"


def test_nics_cat_0_exception():
    with pytest.raises(ValueError, match=r"Classification is only possible for positive integers."):
        nics_cat(0)


def test_nics_cat_neg1_exception():
    with pytest.raises(ValueError, match=r"Classification is only possible for positive integers."):
        nics_cat(-1)
