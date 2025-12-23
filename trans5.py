from PIL import ImageFont, ImageDraw, Image

img = Image.new("RGBA", (400, 100), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

# translucent box behind text
draw.rectangle([10, 10, 390, 90], fill=(0, 0, 0, 120))
draw.text(
    (20, 30), "Hello translucent background", font=font, fill=(255, 255, 255, 255)
)
img.save("text_translucent.png")
