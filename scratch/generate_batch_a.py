from PIL import Image, ImageEnhance, ImageFilter
import os

REFS = 'assets/mayoohka_refs'
OUT = 'assets/images'

def smart_crop_resize(img_path, target_size, crop_focus='center', enhance_contrast=1.05, enhance_color=1.05):
    """
    Intelligently crops and resizes an image to target (width, height)
    maintaining high quality, proper framing, and optimal aspect ratio.
    crop_focus: 'top', 'center', 'top_center', 'bottom', or (x_frac, y_frac)
    """
    im = Image.open(img_path).convert('RGB')
    target_w, target_h = target_size
    target_ratio = target_w / target_h
    orig_w, orig_h = im.size
    orig_ratio = orig_w / orig_h

    if orig_ratio > target_ratio:
        # Original is wider than target -> crop left/right
        new_w = int(orig_h * target_ratio)
        if crop_focus == 'center':
            left = (orig_w - new_w) // 2
        elif crop_focus == 'left':
            left = 0
        elif crop_focus == 'right':
            left = orig_w - new_w
        elif isinstance(crop_focus, tuple):
            left = int((orig_w - new_w) * crop_focus[0])
        else:
            left = (orig_w - new_w) // 2
        top = 0
        box = (left, top, left + new_w, orig_h)
    else:
        # Original is taller than target -> crop top/bottom
        new_h = int(orig_w / target_ratio)
        if crop_focus == 'top':
            top = 0
        elif crop_focus == 'top_center':
            top = int((orig_h - new_h) * 0.15)
        elif crop_focus == 'center':
            top = (orig_h - new_h) // 2
        elif crop_focus == 'bottom':
            top = orig_h - new_h
        elif isinstance(crop_focus, tuple):
            top = int((orig_h - new_h) * crop_focus[1])
        else:
            top = int((orig_h - new_h) * 0.1)
        left = 0
        box = (left, top, orig_w, top + new_h)

    cropped = im.crop(box)
    resized = cropped.resize(target_size, Image.Resampling.LANCZOS)

    # Subtle premium contrast & color enhancement for editorial look
    if enhance_contrast != 1.0:
        enh_con = ImageEnhance.Contrast(resized)
        resized = enh_con.enhance(enhance_contrast)
    if enhance_color != 1.0:
        enh_col = ImageEnhance.Color(resized)
        resized = enh_col.enhance(enhance_color)

    return resized

def generate_batch_a():
    os.makedirs(OUT, exist_ok=True)
    print("Generating Batch A: Hero panels (720x1080) & Collection cards (600x840)...")

    # --- 1. HERO PANELS (720x1080) ---
    hero_specs = [
        ('hero-01.webp', 'Screenshot 2026-10-06 180946.png', 'top_center'), # Crimson bridal Kanchipuram
        ('hero-02.webp', 'Screenshot 2026-10-06 181336.png', 'top_center'), # Blush pink mermaid gown
        ('hero-03.webp', 'Screenshot 2026-10-06 181221.png', 'top_center'), # Kerala Kasavu with lime accents
        ('hero-04.webp', 'Screenshot 2026-10-06 181003.png', 'top_center'), # Antique gold tissue Muhurtham silk
        ('hero-05.webp', 'Screenshot 2026-10-06 181240.png', 'top_center'), # Aiswarya Baiju in royal violet silk
    ]

    for fname, ref, focus in hero_specs:
        ref_path = os.path.join(REFS, ref)
        out_path = os.path.join(OUT, fname)
        img = smart_crop_resize(ref_path, (720, 1080), crop_focus=focus)
        img.save(out_path, 'WEBP', quality=88, method=6)
        print(f"Created {fname} ({os.path.getsize(out_path)} bytes)")

    # --- 2. COLLECTION CARDS (600x840) Primary & Hover ---
    coll_specs = [
        # Col 1: Sarees
        ('collection-01.webp', 'Screenshot 2026-10-06 180854.png', 'top_center'),       # Rust orange silk saree
        ('collection-01-hover.webp', 'Screenshot 2026-10-06 181716.png', 'center'),       # Painted tussar silk border
        # Col 2: Bridal Sarees
        ('collection-02.webp', 'Screenshot 2026-10-06 180946.png', 'top_center'),       # Coral crimson bridal silk
        ('collection-02-hover.webp', 'Screenshot 2026-10-06 181003.png', (0.5, 0.2)),    # Antique gold tissue bridal
        # Col 3: Lehengas
        ('collection-03.webp', 'Screenshot 2026-10-06 181148.png', 'top_center'),       # Ivory chevron zari lehenga
        ('collection-03-hover.webp', 'Screenshot 2026-10-06 180759.png', 'top_center'), # Emerald Kasavu half-saree
        # Col 4: Bridal Blouses
        ('collection-04.webp', 'Screenshot 2026-10-06 180827.png', (0.5, 0.15)),        # Rani pink brocade blouse back
        ('collection-04-hover.webp', 'Screenshot 2026-10-06 181028.png', (0.5, 0.2)),   # Golden beige cutout blouse
        # Col 5: Custom Dresses
        ('collection-05.webp', 'Screenshot 2026-10-06 181344.png', 'top_center'),       # Blush pink mermaid gown
        ('collection-05-hover.webp', 'Screenshot 2026-10-06 181043.png', (0.5, 0.1)),   # Black off-shoulder gown
        # Col 6: Ready-mades
        ('collection-06.webp', 'Screenshot 2026-10-06 180840.png', 'top_center'),       # Rani pink pleated festive
        ('collection-06-hover.webp', 'Screenshot 2026-10-06 181320.png', 'top_center'), # Schiffli embroidered dress
        # Col 7: Kids Wear
        ('collection-07.webp', 'Screenshot 2026-10-06 180759.png', (0.5, 0.05)),        # Puffed blouse Kasavu festive
        ('collection-07-hover.webp', 'Screenshot 2026-10-06 180810.png', (0.1, 0.1)),   # Group festive celebration
        # Col 8: Gents Wear
        ('collection-08.webp', 'Screenshot 2026-10-06 181136.png', (0.3, 0.1)),         # Groom raw silk kurta
        ('collection-08-hover.webp', 'Screenshot 2026-10-06 180929.png', (0.2, 0.1)),   # Black shirt & silver mundu
    ]

    for fname, ref, focus in coll_specs:
        ref_path = os.path.join(REFS, ref)
        out_path = os.path.join(OUT, fname)
        img = smart_crop_resize(ref_path, (600, 840), crop_focus=focus)
        img.save(out_path, 'WEBP', quality=88, method=6)
        print(f"Created {fname} ({os.path.getsize(out_path)} bytes)")

    print("Batch A complete: 5 hero panels + 16 collection cards (8 primary + 8 hover) generated!")

if __name__ == '__main__':
    generate_batch_a()
