import os
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

raw = Image.open('D:/Mayoohka_demo/assets/images/owner-orig.png').convert('RGB')
w, h = raw.size

def enhance_portrait_pipeline(img_pil, target_w=800, target_h=1000):
    # Upscale using Lanczos
    upscaled = img_pil.resize((target_w, target_h), Image.Resampling.LANCZOS)
    bgr = cv2.cvtColor(np.array(upscaled), cv2.COLOR_RGB2BGR)
    
    # 1. Bilateral filter for noise reduction & smooth skin
    denoised = cv2.bilateralFilter(bgr, d=7, sigmaColor=25, sigmaSpace=25)
    
    # 2. LAB enhancement: CLAHE on L channel
    lab = cv2.cvtColor(denoised, cv2.COLOR_BGR2LAB)
    l, a, b_ch = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    l_c = clahe.apply(l)
    l_blend = cv2.addWeighted(l, 0.5, l_c, 0.5, 0)
    lab_enh = cv2.merge([l_blend, a, b_ch])
    bgr_enh = cv2.cvtColor(lab_enh, cv2.COLOR_LAB2BGR)
    
    # 3. Frequency separation sharpening
    # High-pass filter for fine detail (eyes, jewelry, zari embroidery, jasmine flowers)
    low_freq = cv2.GaussianBlur(bgr_enh, (0, 0), sigmaX=1.8)
    high_freq = cv2.subtract(bgr_enh, low_freq)
    
    # Add subtle high-freq boost
    sharpened = cv2.addWeighted(bgr_enh, 1.0, high_freq, 0.65, 0)
    
    # 4. Color Vibrance & Warmth
    rgb = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)
    pil_res = Image.fromarray(rgb)
    pil_res = ImageEnhance.Color(pil_res).enhance(1.06)
    pil_res = ImageEnhance.Contrast(pil_res).enhance(1.03)
    
    # 5. Soft vignette
    arr = np.array(pil_res).astype(float)
    y, x = np.ogrid[:target_h, :target_w]
    cx, cy = target_w * 0.52, target_h * 0.32
    r = np.sqrt(((x - cx) / (target_w * 0.65))**2 + ((y - cy) / (target_h * 0.65))**2)
    vig = np.clip(1.02 - 0.15 * (r ** 1.6), 0.84, 1.02)
    arr = np.clip(arr * vig[:, :, np.newaxis], 0, 255).astype(np.uint8)
    
    final_pil = Image.fromarray(arr)
    final_pil = final_pil.filter(ImageFilter.UnsharpMask(radius=1.0, percent=80, threshold=2))
    return final_pil

# --- Option 1: Medium portrait (y=8 to y=223, ratio exactly 0.8) ---
crop1 = raw.crop((0, 8, w, 223))
res1 = enhance_portrait_pipeline(crop1, 800, 1000)
res1.save('D:/Mayoohka_demo/scratch/founder_opt1_medium.png', 'PNG')
print("Option 1 saved: founder_opt1_medium.png")

# --- Option 2: Slightly wider headroom & bust (y=0 to y=215, with 10px mirrored sides) ---
# Let's see: from y=0 to y=215
crop2 = raw.crop((0, 0, w, 215))
res2 = enhance_portrait_pipeline(crop2, 800, 1000)
res2.save('D:/Mayoohka_demo/scratch/founder_opt2_headroom.png', 'PNG')
print("Option 2 saved: founder_opt2_headroom.png")
