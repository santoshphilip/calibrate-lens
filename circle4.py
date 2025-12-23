"""
draw circle size of radians sunpath
use a circle funtion
unit test the function
make a main
"""

from PIL import Image, ImageDraw
import pytest


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

    # Draw an outlined circle
    cx, cy, cr = 1500, 1500, 1500
    bbox = circle2box(cx, cy, cr)
    draw.ellipse(bbox, outline=(199, 199, 199), width=4)

    cx, cy, cr = 1000, 1000, 500
    bbox = circle2box(cx, cy, cr)
    draw.ellipse(bbox, outline=(199, 199, 199), width=4)

    image.save("d.png")


if __name__ == "__main__":
    width, height = 3000, 3000
    main(width, height)
