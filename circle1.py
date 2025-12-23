"""just draw circle using pillow"""

from PIL import Image, ImageDraw

# Create a blank image (white background)
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw an outlined circle
draw.ellipse((100, 100, 400, 400), outline="blue", width=10)

# Draw a filled circle
draw.ellipse((150, 150, 350, 350), fill="red")

# You can also use center + radius style with a little math
center_x, center_y = 250, 250

image.save("a.png")
