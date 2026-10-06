import os
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

raw = Image.open('D:/Mayoohka_demo/assets/images/owner-orig.png').convert('RGB')
w, h = raw.size

# Medium portrait crop:
# Let's crop from y=10 to y=225 (height=215, width=172 -> ratio is 172/215 = 0.8, which is exactly 4:5!)
crop_box = (0, 10, w, 225)
crop_img = raw.crop(crop_box)
print("Crop size:", crop_img.size, "Aspect ratio:", crop_img.size[0] / crop_img.size[1])

# Target size: 800 x 1000 (standard 4:5 for .about-story-media, retina 2x for a 400-500px container)
target_w, target_h = 800, 1000

# Super-resolution pipeline:
# 1. Multi-pass Lanczos upscaling
upscaled = crop_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
bgr = cv2.cvtColor(np.array(upscaled), cv2.COLOR_RGB2BGR)

# 2. Edge-preserving bilateral filter to remove noise & pixel blockiness
denoised = cv2.bilateralFilter(bgr, d=7, sigmaColor=28, sigmaSpace=28)

# 3. LAB space enhancement: CLAHE on luminance
lab = cv2.cvtColor(denoised, cv2.COLOR_BGR2LAB)
l, a, b_ch = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8))
l_c = clahe.apply(l)
l_blend = cv2.addWeighted(l, 0.45, l_c, 0.55, 0)
lab_enh = cv2.merge([l_blend, a, b_ch])
bgr_enh = cv2.cvtColor(lab_enh, cv2.COLOR_LAB2BGR)

# 4. Multi-frequency sharpening
# Fine detail pass (radius 1.0)
blur_fine = cv2.GaussianBlur(bgr_enh, (0, 0), sigmaX=1.1)
sharp_fine = cv2.addWeighted(bgr_enh, 1.35, blur_fine, -0.35, 0)

# Medium contour pass
blur_med = cv2.GaussianBlur(sharp_fine, (0, 0), sigmaX=2.2)
sharp_med = cv2.addWeighted(sharp_fine, 1.25, blur_med, -0.25, 0)

# 5. Color vibrancy and contrast
rgb_enh = cv2.cvtColor(sharp_med, cv2.COLOR_BGR2RGB)
pil_enh = Image.fromarray(rgb_enh)

# Enhance color to make saree pink and blouse green pop luxuriously
pil_enh = ImageEnhance.Color(pil_enh).enhance(1.08)
pil_enh = ImageEnhance.Contrast(pil_enh).enhance(1.04)

# 6. Gentle studio vignette to focus attention on Aiswarya's smile
np_final = np.array(pil_enh).astype(float)
y, x = np.ogrid[:target_h, :target_w]
# center around face (x~0.5, y~0.3)
cx, cy = target_w * 0.54, target_h * 0.28
vig_r = np.sqrt(((x - cx) / (target_w * 0.6)) ** 2 + ((y - cy) / (target_h * 0.6)) ** 2)
vig = np.clip(1.02 - 0.16 * (vig_r ** 1.6), 0.82, 1.02)
np_final = np.clip(np_final * vig[:, :, np.newaxis], 0, 255).astype(np.uint8)

res = Image.fromarray(np_final)
res = res.filter(ImageFilter.UnsharpMask(radius=1.1, percent=100, threshold=2))
res.save('D:/Mayoohka_demo/scratch/test_medium_portrait.png', 'PNG')
print("Saved test_medium_portrait.png")
