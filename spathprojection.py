"""
functions to convert alt, azm to particular projections
"""

import pytest
import math
from pygeometry2d import XY, Line

# radians_projection
# calibrated_projection
# pleijel_projection


def radians_proj(radius, azm, alt):
    """radiance function"""
    pass


def spathprojection(radius, azm, alt, proj_func):
    """does the projection based on proj_func"""
    pass


def radians_alt_projfunc(radius, alt):
    """return the dist from center of diagram for al in radiaans projection"""
    return radius - (radius / 2.0 / 45.0 * alt)


def pleijel(ang):
    """return the pleijel projection for a unit circle"""
    ang_r = math.radians(ang)
    cart_x = math.cos(ang_r)
    cart_y = math.sin(ang_r)

    l1 = Line(XY(0, 0), XY(1, 0))
    l2 = Line(XY(0, -1), XY(cart_x, cart_y))
    pt = l1.intersection(l2, True)
    return pt.x


def pleijel_p(circle_r, alt):
    """return the pleijel projection for a circle of radius circle_r"""
    return circle_r * pleijel(alt)
    pass


def neilslens(circle_r, alt):
    """Return Pleijel projection for Neil's fisheye lens"""
    #     x' = x * 0.359 - 0.968
    reverse_dist = alt * 0.359 - 0.968
    #     if reverse_dist < 0:
    #         reverse_dist = 0
    dist = 31.8076 - reverse_dist  # 31.8076 is the radius using Neil's lens
    unit_dist = dist / 31.8076  # 31.8076 is the radius using Neil's lens
    return circle_r * unit_dist
