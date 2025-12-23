"""pytest for spathprojection.py"""

import spathprojection
import pytest
from pytest_helpers import almostequal


@pytest.mark.parametrize(
    "radius, alt, expected",
    [
        (3000, 45, 1500),  # radius, alt, expected
        (3000, 90, 0),  # radius, alt, expected
        (3000, 0, 3000),  # radius, alt, expected
        (3000, 9, 2700),  # radius, alt, expected
    ],
)
def testradians_alt_projfunc(radius, alt, expected):
    """pytest for radians_alt_projfunc"""
    result = spathprojection.radians_alt_projfunc(radius, alt)
    assert result == expected


@pytest.mark.parametrize(
    "ang, expected",
    [
        (30, 0.57735),  # ang, expected
        (45, 0.41421),  # ang, expected
        (60, 0.26795),  # ang, expected
        (0, 1),  # ang, expected
        (90, 0),  # ang, expected
    ],
)
def test_pleijel(ang, expected):
    """pytest for pleijel"""
    result = spathprojection.pleijel(ang)
    print(result, expected)
    assert almostequal(result, expected, 4)
