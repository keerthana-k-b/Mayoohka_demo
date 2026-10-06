import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def render_ultra_crisp_logo():
    # Load original reference logo
    ref = Image.open('D:/Mayoohka_demo/assets/mayoohka_refs/logo.png').convert('RGBA')
    w, h = ref.size
    
    # We want high-res master: 800 x 520 px (approx 5x resolution of 168x109)
    # Let's inspect the butterfly M in original:
    # Top mark is located at x: 60..108, y: 15..65 in the 168x109 image
    # Let's extract the butterfly M mask with high precision
    arr = np.array(ref)
    gray = cv2.cvtColor(arr[:, :, :3], cv2.COLOR_RGB2GRAY)
    
    # Invert and threshold to get clean binary mask of original mark
    # In the reference, black mark is < 70
    _, mark_bin = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
    
    # Isolate only the M butterfly (y: 0..72)
    m_mask_small = mark_bin.copy()
    m_mask_small[72:, :] = 0
    
    # Find contours to get smooth vector-like shapes
    contours, hierarchy = cv2.findContours(m_mask_small, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
    
    # Upscale canvas
    scale = 6
    target_w, target_h = w * scale, h * scale # 1008 x 654
    
    # Draw smoothed antialiased contours on upscaled mask
    upscaled_mask = np.zeros((target_h, target_w), dtype=np.uint8)
    
    # Scale contours
    scaled_contours = []
    for cnt in contours:
        scaled_cnt = (cnt.astype(np.float32) * scale).astype(np.int32)
        scaled_contours.append(scaled_cnt)
        
    # Draw hierarchy (fill outer, cut out inner butterfly holes)
    cv2.drawContours(upscaled_mask, scaled_contours, -1, 255, -1, cv2.LINE_AA, hierarchy=hierarchy)
    
    # Subtle blur and threshold for smooth curved bezier-like edges
    smooth = cv2.GaussianBlur(upscaled_mask, (5, 5), 1.0)
    _, m_clean = cv2.threshold(smooth, 128, 255, cv2.THRESH_BINARY)
    m_clean_aa = cv2.GaussianBlur(m_clean, (3, 3), 0.5)
    
    # Now create the typography with PIL:
    # "Mayookha" and "BY AISWARYA BAIJU"
    # Let's create an RGBA image:
    # Header version: deep royal emerald / dark teal RGB(15, 59, 58)
    # Footer version: rich heritage gold RGB(201, 162, 75)
    
    # Find system fonts or fallback fonts for clean modern sans
    font_candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf"
    ]
    font_title_path = None
    for p in font_candidates:
        if os.path.exists(p):
            font_title_path = p
            break
            
    print("Using font:", font_title_path)
    
    # Bounds of M mark
    coords = np.argwhere(m_clean_aa > 30)
    my0, mx0 = coords.min(axis=0)
    my1, mx1 = coords.max(axis=0)
    mw, mh = mx1 - mx0, my1 - my0
    
    # Build complete logo composition on clean canvas (600 x 480)
    for theme, col in [('header', (15, 59, 58)), ('footer', (201, 162, 75)), ('white', (255, 255, 255))]:
        canvas = Image.new('RGBA', (600, 480), (0, 0, 0, 0))
        draw = ImageDraw.Draw(canvas)
        
        # 1. Place M mark in center
        # Scale M mark to width ~220px
        m_crop = m_clean_aa[my0:my1, mx0:mx1]
        m_dest_w = 200
        m_dest_h = int(mh * (m_dest_w / mw))
        m_resized = cv2.resize(m_crop, (m_dest_w, m_dest_h), interpolation=cv2.INTER_AREA)
        
        mx = (600 - m_dest_w) // 2
        my = 40
        
        # Paste M mark with color
        m_rgba = np.zeros((m_dest_h, m_dest_w, 4), dtype=np.uint8)
        for c in range(3):
            m_rgba[:, :, c] = col[c]
        m_rgba[:, :, 3] = m_resized
        canvas.paste(Image.fromarray(m_rgba), (mx, my), Image.fromarray(m_rgba))
        
        # 2. Draw "Mayookha"
        font_title = ImageFont.truetype(font_title_path, 54) if font_title_path else ImageFont.load_default()
        title_text = "Mayookha"
        bbox_t = draw.textbbox((0, 0), title_text, font=font_title)
        tw = bbox_t[2] - bbox_t[0]
        tx = (600 - tw) // 2
        ty = my + m_dest_h + 24
        draw.text((tx, ty), title_text, fill=(col[0], col[1], col[2], 255), font=font_title)
        
        # 3. Horizontal dividing rule
        line_y = ty + (bbox_t[3] - bbox_t[1]) + 14
        line_w = 240
        lx0 = (600 - line_w) // 2
        lx1 = lx0 + line_w
        draw.line([(lx0, line_y), (lx1, line_y)], fill=(col[0], col[1], col[2], 230), width=3)
        
        # 4. "BY AISWARYA BAIJU"
        font_sub = ImageFont.truetype(font_title_path, 21) if font_title_path else ImageFont.load_default()
        sub_text = "BY AISWARYA BAIJU"
        # Letter spacing simulation
        spaced_text = "  ".join(sub_text.split(" "))
        spaced_text = " ".join(list(spaced_text))
        bbox_s = draw.textbbox((0, 0), spaced_text, font=font_sub)
        sw = bbox_s[2] - bbox_s[0]
        sx = (600 - sw) // 2
        sy = line_y + 14
        draw.text((sx, sy), spaced_text, fill=(col[0], col[1], col[2], 240), font=font_sub)
        
        # Crop tight with 10px margin
        bbox_all = canvas.getbbox()
        canvas_cropped = canvas.crop((bbox_all[0]-10, bbox_all[1]-10, bbox_all[2]+10, bbox_all[3]+10))
        
        out_name = f'D:/Mayoohka_demo/assets/images/logo-{theme}.png'
        canvas_cropped.save(out_name, 'PNG')
        if theme == 'header':
            canvas_cropped.save('D:/Mayoohka_demo/assets/images/logo.png', 'PNG')
        print(f"Saved {out_name} (size: {canvas_cropped.size})")

    # Favicon: 256x256 circular emerald badge with gold butterfly M
    fav_size = 256
    fav_img = Image.new('RGBA', (fav_size, fav_size), (0, 0, 0, 0))
    fav_draw = ImageDraw.Draw(fav_img)
    
    # Outer circle
    margin = 8
    fav_draw.ellipse([(margin, margin), (fav_size - margin, fav_size - margin)], fill=(15, 59, 58, 255), outline=(201, 162, 75, 255), width=5)
    
    # Inner gold butterfly M
    m_fav_w = 140
    m_fav_h = int(mh * (m_fav_w / mw))
    m_fav_resized = cv2.resize(m_crop, (m_fav_w, m_fav_h), interpolation=cv2.INTER_AREA)
    
    fx = (fav_size - m_fav_w) // 2
    fy = (fav_size - m_fav_h) // 2
    
    fav_m_rgba = np.zeros((m_fav_h, m_fav_w, 4), dtype=np.uint8)
    fav_m_rgba[:, :, 0] = 201
    fav_m_rgba[:, :, 1] = 162
    fav_m_rgba[:, :, 2] = 75
    fav_m_rgba[:, :, 3] = m_fav_resized
    
    fav_img.paste(Image.fromarray(fav_m_rgba), (fx, fy), Image.fromarray(fav_m_rgba))
    fav_img.save('D:/Mayoohka_demo/assets/images/favicon.png', 'PNG')
    fav_img.save('D:/Mayoohka_demo/favicon.png', 'PNG')
    fav_img.save('D:/Mayoohka_demo/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("Saved ultra-crisp favicon.png & favicon.ico")

render_ultra_crisp_logo()
