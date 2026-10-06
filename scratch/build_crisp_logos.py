import os
import cv2
import numpy as np
from PIL import Image, ImageFilter

def build_crisp_logos():
    # 1. Load original 168x109 reference logo
    ref_path = 'D:/Mayoohka_demo/assets/mayoohka_refs/logo.png'
    raw = Image.open(ref_path).convert('RGB')
    w, h = raw.size
    
    # 2. Extract normalized alpha mask
    # Background has slight gradient/leaf shadow:
    # Estimate background illumination using morphological opening or large blur
    gray = cv2.cvtColor(np.array(raw), cv2.COLOR_RGB2GRAY)
    
    # Background estimation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    bg_est = cv2.morphologyEx(gray, cv2.MORPH_DILATE, kernel)
    bg_est = cv2.GaussianBlur(bg_est, (31, 31), 0).astype(float)
    
    # Contrast difference: (bg_est - gray)
    diff = np.clip(bg_est - gray.astype(float), 0, 255)
    
    # Normalize: where diff is high, it is black text/mark; where diff is low, background
    # Normalize diff to [0, 1]
    diff_norm = np.clip((diff - 25.0) / 90.0, 0.0, 1.0)
    
    # 3. Super-sample 4x (4x resolution = 672 x 436) for ultra-crisp display
    scale = 4
    target_w, target_h = w * scale, h * scale
    
    # Upscale alpha mask using Lanczos/Cubic
    alpha_large = cv2.resize(diff_norm, (target_w, target_h), interpolation=cv2.INTER_CUBIC)
    
    # Threshold/tighten slightly while preserving antialiasing
    alpha_large = np.clip((alpha_large - 0.12) / (0.88 - 0.12), 0.0, 1.0)
    # Smooth antialiased edges
    alpha_large = cv2.GaussianBlur(alpha_large, (3, 3), 0.5)
    alpha_u8 = (alpha_large * 255).astype(np.uint8)
    
    # Trim unnecessary outer padding
    # Find bounding box of logo
    coords = np.argwhere(alpha_u8 > 30)
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)
    
    # Add comfortable padding (e.g. 15px at 4x)
    pad = 16
    y0 = max(0, y0 - pad)
    y1 = min(target_h, y1 + pad)
    x0 = max(0, x0 - pad)
    x1 = min(target_w, x1 + pad)
    
    alpha_cropped = alpha_u8[y0:y1, x0:x1]
    ch, cw = alpha_cropped.shape
    print(f"Cropped logo dimensions: {cw} x {ch}")
    
    # --- A. Header Logo (Dark Teal / Charcoal #0F3B3A on transparent) ---
    header_img = np.zeros((ch, cw, 4), dtype=np.uint8)
    # Royal emerald/teal: RGB(15, 59, 58)
    header_img[:, :, 0] = 15
    header_img[:, :, 1] = 59
    header_img[:, :, 2] = 58
    header_img[:, :, 3] = alpha_cropped
    Image.fromarray(header_img).save('D:/Mayoohka_demo/assets/images/logo-header.png', 'PNG')
    # Also save as main logo.png
    Image.fromarray(header_img).save('D:/Mayoohka_demo/assets/images/logo.png', 'PNG')
    print("Saved logo-header.png and logo.png")
    
    # --- B. Footer Logo (Warm Gold #C9A24B on transparent) ---
    footer_img = np.zeros((ch, cw, 4), dtype=np.uint8)
    # Heritage gold: RGB(201, 162, 75)
    footer_img[:, :, 0] = 201
    footer_img[:, :, 1] = 162
    footer_img[:, :, 2] = 75
    footer_img[:, :, 3] = alpha_cropped
    Image.fromarray(footer_img).save('D:/Mayoohka_demo/assets/images/logo-footer.png', 'PNG')
    print("Saved logo-footer.png")
    
    # --- C. Clean Favicon (Butterfly M mark alone) ---
    # In the logo, the butterfly M is in the top portion!
    # Let's find butterfly M bounds:
    # The text "Mayookha" starts around 58% of the height.
    # So top 55% of the logo contains the butterfly M!
    m_h = int(ch * 0.58)
    m_alpha = alpha_cropped[:m_h, :]
    m_coords = np.argwhere(m_alpha > 30)
    my0, mx0 = m_coords.min(axis=0)
    my1, mx1 = m_coords.max(axis=0)
    
    m_cropped = m_alpha[my0:my1, mx0:mx1]
    mh, mw = m_cropped.shape
    print(f"Butterfly M mark dimensions: {mw} x {mh}")
    
    # Create a square canvas (e.g. 256x256)
    fav_size = 256
    fav_canvas = np.zeros((fav_size, fav_size, 4), dtype=np.uint8)
    
    # Fit butterfly inside square with 20% margin
    target_mark_size = int(fav_size * 0.72)
    scale_m = target_mark_size / max(mw, mh)
    smw, smh = int(mw * scale_m), int(mh * scale_m)
    
    m_resized = cv2.resize(m_cropped, (smw, smh), interpolation=cv2.INTER_CUBIC)
    
    # Center position
    off_x = (fav_size - smw) // 2
    off_y = (fav_size - smh) // 2
    
    # Option: Butterfly M in deep teal/gold emblem circle or transparent
    # Let's make an elegant circular gold emblem favicon with butterfly inside, as well as transparent!
    # 1. Transparent gold butterfly
    fav_gold = np.zeros((fav_size, fav_size, 4), dtype=np.uint8)
    fav_gold[off_y:off_y+smh, off_x:off_x+smw, 0] = 201
    fav_gold[off_y:off_y+smh, off_x:off_x+smw, 1] = 162
    fav_gold[off_y:off_y+smh, off_x:off_x+smw, 2] = 75
    fav_gold[off_y:off_y+smh, off_x:off_x+smw, 3] = m_resized
    
    # 2. Rich luxury circular badge: Deep Royal Emerald circle with Gold border and Gold Butterfly M
    # This renders with high visibility in ANY browser tab (dark mode or light mode tab bars)!
    badge_circle = np.zeros((fav_size, fav_size, 4), dtype=np.uint8)
    center = (fav_size // 2, fav_size // 2)
    radius = int(fav_size * 0.46)
    
    # Draw circle in deep teal
    cv2.circle(badge_circle, center, radius, (15, 59, 58, 255), -1, cv2.LINE_AA)
    # Draw gold border ring
    cv2.circle(badge_circle, center, radius, (201, 162, 75, 255), 6, cv2.LINE_AA)
    
    # Composite gold butterfly in center
    m_mask = m_resized.astype(float) / 255.0
    for c, val in enumerate([201, 162, 75]):
        badge_crop = badge_circle[off_y:off_y+smh, off_x:off_x+smw, c].astype(float)
        badge_circle[off_y:off_y+smh, off_x:off_x+smw, c] = (badge_crop * (1.0 - m_mask) + val * m_mask).astype(np.uint8)
        
    fav_pil = Image.fromarray(badge_circle)
    fav_pil.save('D:/Mayoohka_demo/assets/images/favicon.png', 'PNG')
    fav_pil.save('D:/Mayoohka_demo/favicon.png', 'PNG')
    
    # Also save standard .ico with multiple sizes (16, 32, 48, 64)
    fav_pil.save('D:/Mayoohka_demo/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("Saved favicon.png and favicon.ico")

build_crisp_logos()
