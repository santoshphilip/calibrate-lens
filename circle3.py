"""
draw circle size of radians sunpath
"""

from PIL import Image, ImageDraw

# Create a blank image (white background)
width, height = 3000, 3000
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw an outlined circle
draw.ellipse((0, 0, 3000, 3000), outline=(199, 199, 199), width=4)


image.save("b.png")
