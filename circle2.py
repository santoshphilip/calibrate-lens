"""just draw circle using pillow"""

from PIL import Image, ImageDraw

# Create a blank image (white background)
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw an outlined circle
draw.ellipse((100, 100, 400, 400), outline="black", width=1)


image.save("b.png")
