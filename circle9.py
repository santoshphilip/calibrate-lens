"""
draw a non-smooth analema and non-smooth sunpath
"""

from PIL import Image, ImageDraw
import pytest
import spathprojection
from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
import math
from pytest_helpers import almostequal
import sunpositions


def circle2box(center_x, center_y, radius):
    """return box from circle data"""
    bbox = (center_x - radius, center_y - radius, center_x + radius, center_y + radius)
    return bbox


@pytest.mark.parametrize(
    "center_x, center_y, radius, bbox",
    [
        (100, 100, 50, (50, 50, 150, 150)),  # center_x, center_y, radius, bbox
    ],
)
def test_circle2box(center_x, center_y, radius, bbox):
    """docstring for fname"""
    result = circle2box(center_x, center_y, radius)
    assert result == bbox


def main(width, height):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # draw concentric circles for altitude angles
    circle_r = 1500
    cx, cy = 1500, 1500
    for alt in range(0, 90, 10):
        alt_r = spathprojection.radians_alt_projfunc(circle_r, alt)
        bbox = circle2box(cx, cy, alt_r)
        draw.ellipse(bbox, outline=(199, 199, 199), width=4)

    lat = 41.51606330662579
    lon = 81.39308916058894
    tz = 5.5

    for thehour in range(1, 24):
        sunposs = sunpositions.analemasunpos(thehour, lat, lon, tz)
        # sunposs = sunpositions.smooth_analemasunpos(thehour, lat, lon, tz)
        xys = []
        for _, azm, alt in sunposs:
            pillowx, pillowy = azmalt2pillowcoords(circle_r, azm, alt)
            # draw the point on projection.
            bbox = circle2box(pillowx, pillowy, 9)
            draw.ellipse(bbox, outline=(199, 199, 199), width=1, fill="black")
            xys.append((pillowx, pillowy))
        draw.line(xys, fill="black", width=2)

    thetime = datetime(2025, 6, 21, 7)
    for theday in range(1, 13):
        thedate = datetime(2025, theday, 21, 0)
        # sunposs = sunpositions.smooth_hourlysunpos(thedate, lat, lon, tz)
        sunposs = sunpositions.hourlysunpos(thedate, lat, lon, tz)

        xys = []
        for _, azm, alt in sunposs:
            pillowx, pillowy = azmalt2pillowcoords(circle_r, azm, alt)
            # draw the point on projection.
            bbox = circle2box(pillowx, pillowy, 9)
            draw.ellipse(bbox, outline=(199, 199, 199), width=1, fill="black")
            xys.append((pillowx, pillowy))
        draw.line(xys, fill="black", width=2)

    image.save("h.png")


def azmalt2pillowcoords(circle_r, azm, alt):
    """convert azm, alt to pillow coordinates for drawing"""

    alt_r = spathprojection.radians_alt_projfunc(circle_r, alt)

    # shift into math space and do calcs.
    math_azm = math.radians((azm - 90) * -1)  # x axes is 0 and counterclockise
    # x = rcos(theta)
    # y = rsin(theta)
    cart_x = alt_r * math.cos(math_azm)
    cart_y = alt_r * math.sin(math_azm)

    # Done with math space
    # math space 0,0 is at center of image
    # Pillow 0,0 is on topleft
    pillowx = circle_r + cart_x
    pillowy = circle_r - cart_y
    return pillowx, pillowy


@pytest.mark.parametrize(
    "circle_r, azm, alt, expected",
    [
        (1500, 180, 45, (1500.0, 2250.0)),  # circle_r, azm, alt, expected
        (
            1500,
            45,
            45,
            (2030.3300858899106, 969.6699141100894),
        ),  # circle_r, azm, alt, expected
        (
            1500,
            -45,
            45,
            (969.6699141100894, 969.6699141100893),
        ),  # circle_r, azm, alt, expected
        (1500, 180, 60, (1500.0, 2000.0)),  # circle_r, azm, alt, expected
    ],
)
def test_azmalt2pillowcoords(circle_r, azm, alt, expected):
    """docstring for fname"""
    pass
    result = azmalt2pillowcoords(circle_r, azm, alt)
    assert almostequal(result[0], expected[0])
    assert almostequal(result[1], expected[1])
    assert result == expected


if __name__ == "__main__":
    width, height = 3000, 3000
    main(width, height)
