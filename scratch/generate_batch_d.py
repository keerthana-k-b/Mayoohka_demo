from PIL import Image, ImageEnhance
import os

REFS = 'assets/mayoohka_refs'
OUT = 'assets/images'

def crop_exact(img_path, box, target_size=(540, 960)):
    im = Image.open(img_path).convert('RGB')
    w, h = im.size
    crop_box = (
        int(box[0] * w),
        int(box[1] * h),
        int(box[2] * w),
        int(box[3] * h)
    )
    cropped = im.crop(crop_box)
    resized = cropped.resize(target_size, Image.Resampling.LANCZOS)
    enh_con = ImageEnhance.Contrast(resized)
    resized = enh_con.enhance(1.04)
    return resized

def generate_batch_d():
    print("Generating Batch D: 7 Reel Posters (540x960, 9:16 ratio)...")

    specs = [
        # Reel 1: Samvrutha Crimson Bridal Kanchipuram
        ('reel-poster-01.webp', 'Screenshot 2026-10-06 180946.png', (0.05, 0.02, 0.95, 0.98)),
        # Reel 2: Seraphina Blush Pink Mermaid Bridal Gown
        ('reel-poster-02.webp', 'Screenshot 2026-10-06 181336.png', (0.05, 0.02, 0.95, 0.98)),
        # Reel 3: Charulata Kasavu Weave Saree
        ('reel-poster-03.webp', 'Screenshot 2026-10-06 181221.png', (0.05, 0.02, 0.95, 0.98)),
        # Reel 4: Aiswarya Signature Zardozi Bridal Blouse
        ('reel-poster-04.webp', 'Screenshot 2026-10-06 180827.png', (0.02, 0.02, 0.98, 0.98)),
        # Reel 5: Nila Ivory Chevron Zari Lehenga Set
        ('reel-poster-05.webp', 'Screenshot 2026-10-06 181148.png', (0.05, 0.02, 0.95, 0.98)),
        # Reel 6: Aadya Handloom Rust Silk Saree
        ('reel-poster-06.webp', 'Screenshot 2026-10-06 180854.png', (0.05, 0.02, 0.95, 0.98)),
        # Reel 7: Aravind Black Shirt & Kasavu Mundu Set
        ('reel-poster-07.webp', 'Screenshot 2026-10-06 180929.png', (0.02, 0.02, 0.98, 0.98)),
    ]

    for fname, ref, box in specs:
        ref_path = os.path.join(REFS, ref)
        out_path = os.path.join(OUT, fname)
        img = crop_exact(ref_path, box, target_size=(540, 960))
        img.save(out_path, 'WEBP', quality=88, method=6)
        print(f"Created {fname} ({os.path.getsize(out_path)} bytes)")

    print("Batch D complete: 7 reel posters generated!")

if __name__ == '__main__':
    generate_batch_d()
