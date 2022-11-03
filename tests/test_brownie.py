import pytest

import my_package.brownie as brownie

@pytest.mark.xfail
def test_zero_brownie():
    a = brownie.brownie(12)
    assert False

def test_one_brownie():
    pass

def test_more_brownies():
    pass

def test_negative_brownies():
    pass
