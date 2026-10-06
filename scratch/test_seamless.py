import os
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

# Load original raw image
raw = Image.open('D:/Mayoohka_demo/assets/images/owner-orig.png').convert('RGB')
raw_w, raw_h = raw.size

# --- TEST 1: Seamless Studio Portrait with High-End Background Inpainting/Extension ---
# Instead of a simple feather, let's use OpenCV seamless clone or inpainting, or replicate the authentic wall pattern!
# Let's inspect the wall on the right and the architectural molding on the left.

def create_seamless_full_length(target_w=1000, target_h=1250):
    # Scale subject so height is ~1160 (leaving ~50px top headroom, ~40px bottom)
    scale = 1160.0 / raw_h
    sw = int(raw_w * scale)
    sh = int(raw_h * scale)
    
    # Advanced upscale of raw image
    # Step 1: Lanczos resize
    sub_large = raw.resize((sw, sh), Image.Resampling.LANCZOS)
    sub_np = np.array(sub_large)
    
    # Step 2: Denoise and enhance subject
    bgr = cv2.cvtColor(sub_np, cv2.COLOR_RGB2BGR)
    
    # Bilateral filter for smooth skin while preserving sharp edges
    b_filt = cv2.bilateralFilter(bgr, d=7, sigmaColor=30, sigmaSpace=30)
    
    # Detail enhancement on L channel
    lab = cv2.cvtColor(b_filt, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.8, tileGridSize=(8, 8))
    l_c = clahe.apply(l)
    l_enh = cv2.addWeighted(l, 0.45, l_c, 0.55, 0)
    lab_enh = cv2.merge([l_enh, a, b])
    bgr_enh = cv2.cvtColor(lab_enh, cv2.COLOR_LAB2BGR)
    
    # Unsharp mask for jewelry, eyes, and embroidery
    blur = cv2.GaussianBlur(bgr_enh, (0, 0), sigmaX=1.3)
    sharp = cv2.addWeighted(bgr_enh, 1.4, blur, -0.4, 0)
    
    sub_enhanced = cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB)
    
    # Now let's create the background:
    # Notice: the left side of the photo has a vertical window/door architectural frame: warm wood / molding.
    # The right side has a gorgeous warm golden damask/mottled boutique wallpaper!
    # Let's synthesize the background by seamlessly extending the left architectural element to the left canvas edge,
    # and extending the golden boutique wallpaper across the right canvas edge!
    
    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    
    # Subject position in canvas
    px = (target_w - sw) // 2
    py = (target_h - sh) // 2
    
    # Sample the wallpaper column on the right edge of the subject (e.g. rightmost 30 pixels)
    right_wall = sub_enhanced[:, int(sw * 0.88):, :]
    rw_h, rw_w, _ = right_wall.shape
    
    # Sample the architectural column on the left edge of the subject (e.g. leftmost 30 pixels)
    left_wall = sub_enhanced[:, :int(sw * 0.15), :]
    lw_h, lw_w, _ = left_wall.shape
    
    # Place subject on canvas
    canvas[py:py+sh, px:px+sw] = sub_enhanced
    
    # Fill left canvas region (from 0 to px) by tiling/reflecting and mirroring the left architectural tone
    for x in range(px - 1, -1, -1):
        sample_x = (px - 1 - x) % lw_w
        canvas[py:py+sh, x] = left_wall[:, sample_x]
        
    # Fill right canvas region (from px + sw to target_w) by blending & tiling the textured golden boutique wallpaper
    for x in range(px + sw, target_w):
        offset = x - (px + sw)
        sample_x = rw_w - 1 - (offset % rw_w)
        canvas[py:py+sh, x] = right_wall[:, sample_x]
        
    # Fill top headroom (from 0 to py)
    for y in range(py - 1, -1, -1):
        canvas[y, :] = canvas[py, :]
        
    # Fill bottom floor (from py + sh to target_h)
    for y in range(py + sh, target_h):
        canvas[y, :] = canvas[py + sh - 1, :]
        
    # Apply soft Gaussian blend along the seam lines x=px and x=px+sw to make them completely invisible
    # Create seam transition zones
    seam_w = 40
    # Left seam blend
    for i in range(seam_w * 2):
        x = px - seam_w + i
        if 0 <= x < target_w:
            alpha = i / (seam_w * 2.0)
            # smoothstep
            alpha = alpha * alpha * (3 - 2 * alpha)
            # blend with blurred column
            col_blur = cv2.GaussianBlur(canvas[:, x:x+1], (1, 15), 0)
            canvas[:, x:x+1] = (canvas[:, x:x+1].astype(float) * (1 - 0.3 * (1 - abs(2*alpha - 1))) + col_blur.astype(float) * 0.3 * (1 - abs(2*alpha - 1))).astype(np.uint8)

    # Right seam blend
    for i in range(seam_w * 2):
        x = (px + sw) - seam_w + i
        if 0 <= x < target_w:
            alpha = i / (seam_w * 2.0)
            alpha = alpha * alpha * (3 - 2 * alpha)
            col_blur = cv2.GaussianBlur(canvas[:, x:x+1], (1, 15), 0)
            canvas[:, x:x+1] = (canvas[:, x:x+1].astype(float) * (1 - 0.3 * (1 - abs(2*alpha - 1))) + col_blur.astype(float) * 0.3 * (1 - abs(2*alpha - 1))).astype(np.uint8)

    # Apply studio lighting gradient overlay (soft warm vignette centered on Aiswarya)
    y_idx, x_idx = np.ogrid[:target_h, :target_w]
    vig_dist = np.sqrt(((x_idx - target_w*0.5) / (target_w * 0.65))**2 + ((y_idx - target_h*0.35) / (target_h * 0.55))**2)
    vignette = np.clip(1.04 - 0.18 * (vig_dist ** 1.5), 0.78, 1.05)
    
    final = np.clip(canvas.astype(float) * vignette[:, :, np.newaxis], 0, 255).astype(np.uint8)
    
    # Subtle boutique warmth grade
    final_pil = Image.fromarray(final)
    final_pil = ImageEnhance.Color(final_pil).enhance(1.06)
    final_pil = ImageEnhance.Contrast(final_pil).enhance(1.04)
    final_pil = final_pil.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    
    final_pil.save('D:/Mayoohka_demo/scratch/test_seamless_full.png', 'PNG')
    print("Saved test_seamless_full.png")

create_seamless_full_length()
