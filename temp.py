"""develop pleijel projections"""

import math
from pygeometry2d import XY, Line
import pytest
from pytest_helpers import almostequal


ang = 30


def pleijel(ang):
    """return the pleijel projection for a unit circle"""
    ang_r = math.radians(ang)
    cart_x = math.cos(ang_r)
    cart_y = math.sin(ang_r)

    l1 = Line(XY(0, 0), XY(1, 0))
    l2 = Line(XY(0, -1), XY(cart_x, cart_y))
    pt = l1.intersection(l2, True)
    return pt.x


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
    result = pleijel(ang)
    print(result, expected)
    assert almostequal(result, expected, 4)
