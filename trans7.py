from PIL import Image, ImageDraw

base = Image.open("m.png").convert("RGBA")

overlay = Image.new("RGBA", base.size, (255, 255, 255, 0))
od = ImageDraw.Draw(overlay)

# translucent yellow polygon
od.polygon([(100, 100), (1300, 1150), (50, 1300)], fill=(255, 255, 0, 100))

# fuse overlay on top of base
result = Image.alpha_composite(base, overlay)

result.save("overlay_result.png")
