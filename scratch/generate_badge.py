from PIL import Image, ImageDraw, ImageFont
import math

S = 512
im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(im)

gold = "#C9A24B"
teal = "#0F3B3A"
dark_teal = "#0A2827"
cream = "#FAF7F2"

# Outer gold ring
d.ellipse((8, 8, S - 8, S - 8), fill=gold)
# Inner teal circle
d.ellipse((22, 22, S - 22, S - 22), fill=teal)
# Delicate inner gold ring
d.ellipse((36, 36, S - 36, S - 36), outline=gold, width=3)
# Additional fine gold inner accent ring
d.ellipse((48, 48, S - 48, S - 48), outline="#E5C77A", width=1)

# Load fonts
try:
    font_large = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 68)
    font_bold = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 46)
    font_sub = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 20)
    font_tiny = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 16)
except OSError:
    font_large = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_tiny = ImageFont.load_default()

# Stylized 'M' with butterfly wings emblem or artistic monogram
# Center M
d.text((S / 2, S / 2 - 60), "M", font=font_large, fill=gold, anchor="mm")

# Tiny butterfly accent / stars
d.line([(S/2 - 50, S/2 - 120), (S/2 + 50, S/2 - 120)], fill="#E5C77A", width=2)
d.ellipse((S/2 - 4, S/2 - 124, S/2 + 4, S/2 - 116), fill=gold)

# Brand Name: MAYOOKHA
d.text((S / 2, S / 2 + 25), "MAYOOKHA", font=font_bold, fill=cream, anchor="mm")

# Subtext: THE BRIDAL STUDIO
d.text((S / 2, S / 2 + 75), "THE BRIDAL STUDIO", font=font_sub, fill=gold, anchor="mm")

# Location: CHERTHALA
d.text((S / 2, S / 2 + 115), "CHERTHALA  ·  KERALA", font=font_tiny, fill="#D1C2A5", anchor="mm")

im.save("assets/images/logo-badge.png", "PNG")
print("Saved assets/images/logo-badge.png")
