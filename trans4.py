from PIL import Image, ImageDraw

base = Image.new("RGBA", (400, 300), (30, 30, 30, 255))  # opaque dark base
overlay = Image.new("RGBA", base.size, (255, 255, 255, 0))
od = ImageDraw.Draw(overlay)

# draw on overlay (semi-transparent blue circle)
od.ellipse([75, 25, 325, 275], fill=(0, 100, 255, 150))

# composite (overlay on top of base)
result = Image.alpha_composite(base, overlay)
result.save("overlay_circle.png")

overlay = Image.new("RGBA", base.size, (255, 255, 255, 0))
od = ImageDraw.Draw(overlay)
od.polygon([(50, 50), (350, 100), (300, 250), (100, 220)], fill=(0, 255, 0, 120))

# paste overlay onto base using overlay itself as mask
base.paste(overlay, (0, 0), overlay)
base.save("pasted_polygon.png")

overlay = Image.new("RGBA", base.size, (255, 255, 255, 0))
od = ImageDraw.Draw(overlay)
od.polygon([(50, 50), (350, 100), (300, 250), (100, 220)], fill=(0, 255, 0, 120))

# paste overlay onto base using overlay itself as mask
base.paste(overlay, (0, 0), overlay)
base.save("pasted_polygon.png")
