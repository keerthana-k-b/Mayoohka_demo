from PIL import Image, ImageEnhance
import os

REFS = 'assets/mayoohka_refs'
OUT = 'assets/images'

def crop_exact(img_path, box, target_size):
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

def generate_batch_c():
    print("Generating Batch C: Mosaic, Social Strip, About Story...")

    specs = [
        # Story Mosaic:
        # story-01: Left tall (600x870) - 3 women in Kerala courtyard
        ('story-01.webp', 'Screenshot 2026-10-06 180810.png', (0.02, 0.02, 0.98, 0.98), (600, 870)),
        # story-02: Center top (800x560) - Aiswarya Baiju at studio
        ('story-02.webp', 'Screenshot 2026-10-06 181240.png', (0.05, 0.05, 0.95, 0.75), (800, 560)),
        # story-03: Center bottom (800x560) - Hand-painted tussar organza boutique display
        ('story-03.webp', 'Screenshot 2026-10-06 181716.png', (0.05, 0.15, 0.95, 0.85), (800, 560)),
        # story-04: Right tall (600x870) - Blush pink bridal gown
        ('story-04.webp', 'Screenshot 2026-10-06 181336.png', (0.05, 0.02, 0.95, 0.98), (600, 870)),

        # Social / Instagram strip (600x750, 4:5 ratio):
        ('social-01.webp', 'Screenshot 2026-10-06 181716.png', (0.05, 0.05, 0.95, 0.95), (600, 750)),
        ('social-02.webp', 'Screenshot 2026-10-06 181136.png', (0.05, 0.05, 0.95, 0.95), (600, 750)),
    ]

    for fname, ref, box, target_size in specs:
        ref_path = os.path.join(REFS, ref)
        out_path = os.path.join(OUT, fname)
        img = crop_exact(ref_path, box, target_size)
        img.save(out_path, 'WEBP', quality=88, method=6)
        print(f"Created {fname} ({target_size[0]}x{target_size[1]}, {os.path.getsize(out_path)} bytes)")

    print("Batch C complete: 4 story mosaic + 2 social strip images generated!")

if __name__ == '__main__':
    generate_batch_c()
