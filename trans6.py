from PIL import Image, ImageDraw

# load your existing drawing
base = Image.open("m.png").convert("RGBA")

# create a drawing layer
draw = ImageDraw.Draw(base, "RGBA")

# draw a semi-transparent rectangle
# A=80 means about 30% opacity
draw.rectangle([50, 50, 1300, 1250], fill=(255, 0, 0, 80))

base.save("with_translucent_fill.png")
