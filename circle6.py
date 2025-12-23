"""
put known alt azm on the sunpath diagram
Draw a few datetimes on the sunpath and see if they match the radians output
"""

from PIL import Image, ImageDraw
import pytest
import spathprojection
from pyephem_sunpath.sunpath import sunpos
from datetime import datetime
import math


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
    alt = 45
    for alt in range(0, 90, 10):
        alt_r = spathprojection.radians_alt_projfunc(circle_r, alt)
        bbox = circle2box(cx, cy, alt_r)
        draw.ellipse(bbox, outline=(199, 199, 199), width=4)

    # draw a few sun positions
    thetime = datetime(2025, 6, 21, 7)
    lat = 41.51606330662579
    lon = 81.39308916058894
    tz = 5.5

    alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
    # print(alt, azm)

    #     azm, alt = 180, 45
    #     azm, alt = 45, 45
    #     azm, alt = -45, 45
    #     azm, alt = 180, 60

    alt_r = spathprojection.radians_alt_projfunc(circle_r, alt)
    print(f"in polar space {azm=}, {alt=}, {alt_r=}")

    # shift into math space and do calcs.
    math_azm = math.radians((azm - 90) * -1)  # x axes is 0 and counterclockise
    # x = rcos(theta)
    # y = rsin(theta)
    cart_x = alt_r * math.cos(math_azm)
    cart_y = alt_r * math.sin(math_azm)
    print(f"in math space: {cart_x=}, {cart_y=}")

    # Done with math space
    # math space 0,0 is at center of image
    # Pillow 0,0 is on topleft
    pillowx = circle_r + cart_x
    pillowy = circle_r - cart_y
    print(f"in pillow space: {pillowx=}, {pillowy=}")

    # draw the point on projection.
    bbox = circle2box(pillowx, pillowy, 9)
    draw.ellipse(bbox, outline=(199, 199, 199), width=1, fill="black")

    image.save("f.png")


if __name__ == "__main__":
    width, height = 3000, 3000
    main(width, height)
