import pytest
import random

import my_package.brownie as brownie


def test_zero_brownie():
    res = brownie.brownie(0)
    exp = f"0 brownie!"
    assert res == exp


def test_one_brownie():
    res = brownie.brownie(1)
    exp = f"1 brownie!"
    assert res == exp


def test_more_brownies():
    number = random.randint(2, 1000)
    res = brownie.brownie(number)
    exp = f"{str(number)} brownies!"
    assert res == exp


def test_negative_brownies():
    pytest.xfail("TODO")

def test_non_int_brownies():
    pytest.xfail("TODO")
