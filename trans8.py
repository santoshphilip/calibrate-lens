from PIL import Image, ImageDraw, ImageChops

w, h = 400, 400
img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# draw a line to make sure it is visible thru the transparency
draw.line(((0, 0), (300, 300)), fill=(0, 0, 255, 128), width=4)
# Circle centers & radii
cx, cy = 200, 200
r_outer = 150
r_inner = 80

# --- Outer circle mask ---
mask_outer = Image.new("RGBA", (w, h), (255, 255, 255, 0))
d1 = ImageDraw.Draw(mask_outer)
d1.ellipse(
    (cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(255, 255, 0, 100)
)

# --- Inner circle mask ---
mask_inner = Image.new("RGBA", (w, h), (255, 255, 255, 0))
d2 = ImageDraw.Draw(mask_inner)
d2.ellipse(
    (cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(255, 255, 0, 100)
)

# --- Ring mask = outer minus inner ---
ring_mask = ImageChops.subtract(mask_outer, mask_inner)

# --- Fill the ring with translucent color ---
fill_color = (255, 0, 0, 128)
fill_layer = Image.new("RGBA", (w, h), fill_color)

img.paste(fill_layer, mask=ring_mask)

# Optional: draw outlines
draw.ellipse(
    (cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), outline="black", width=3
)
draw.ellipse(
    (cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), outline="black", width=3
)

img.save("bb.png")
