import pytest
from p11_6_calc import calc_str

class TestCalc():
    def test_calc1(self):
        assert calc_str("5 - 3 * 4/2") == -1

    def test_calc2(self):
        assert calc_str("5.0 - (2 * 2^(4-2))^2") == -59

    def test_calc3(self):
        assert calc_str("1.0 - 2 * 2^2-2") == -9