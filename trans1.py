from PIL import Image, ImageDraw

# create an RGBA image (transparent background)
img = Image.new("RGBA", (400, 300), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# translucent red rectangle (alpha 128 of 255)
draw.rectangle([50, 50, 350, 250], fill=(255, 0, 0, 128))

img.save("translucent_rect.png")
