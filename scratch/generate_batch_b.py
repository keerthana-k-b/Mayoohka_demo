from PIL import Image, ImageEnhance
import os

REFS = 'assets/mayoohka_refs'
OUT = 'assets/images'

def crop_exact(img_path, box, target_size=(600, 800)):
    """
    box: (left_frac, top_frac, right_frac, bottom_frac)
    Crops specific sub-region and resizes to target_size.
    """
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

def generate_batch_b():
    print("Generating Batch B: 34 Product Images (600x800, 3:4 ratio)...")

    # Specifications: (filename, ref_image, (left_f, top_f, right_f, bottom_f))
    prod_specs = [
        # Sarees (prod-01 to prod-08)
        ('product-01.webp', 'Screenshot 2026-10-06 181221.png', (0.05, 0.05, 0.95, 0.95)),  # Charulata Kasavu Weave Saree
        ('product-02.webp', 'Screenshot 2026-10-06 180854.png', (0.05, 0.02, 0.95, 0.95)),  # Aadya Handloom Rust Silk Saree
        ('product-03.webp', 'Screenshot 2026-10-06 180929.png', (0.45, 0.35, 1.0, 0.95)),   # Kalyani Black Temple Saree
        ('product-04.webp', 'Screenshot 2026-10-06 181716.png', (0.05, 0.15, 0.95, 0.95)),  # Veda Painted Tussar Organza
        ('product-05.webp', 'Screenshot 2026-10-06 180810.png', (0.0, 0.05, 0.45, 0.95)),   # Souparnika Emerald Saree / Skirt
        ('product-06.webp', 'Screenshot 2026-10-06 181015.png', (0.05, 0.05, 0.95, 0.95)),  # Meera Pastel Lilac / Orange Silk
        ('product-07.webp', 'Screenshot 2026-10-06 181028.png', (0.1, 0.25, 0.9, 0.95)),   # Anamika Copper Silk Drape
        ('product-08.webp', 'Screenshot 2026-10-06 181003.png', (0.1, 0.3, 0.9, 0.98)),    # Devika Antique Gold Tissue

        # Bridal Sarees (prod-09 to prod-14)
        ('product-09.webp', 'Screenshot 2026-10-06 180946.png', (0.05, 0.02, 0.95, 0.98)),  # Samvrutha Crimson Bridal Kanchipuram
        ('product-10.webp', 'Screenshot 2026-10-06 181003.png', (0.05, 0.02, 0.95, 0.95)),  # Swarnamukhi Antique Gold Muhurtham
        ('product-11.webp', 'Screenshot 2026-10-06 181240.png', (0.05, 0.02, 0.95, 0.95)),  # Aparna Royal Violet Kanchipuram
        ('product-12.webp', 'Screenshot 2026-10-06 180810.png', (0.28, 0.05, 0.68, 0.95)),  # Mythili Scarlet Red Bridal Silk
        ('product-13.webp', 'Screenshot 2026-10-06 180840.png', (0.05, 0.02, 0.95, 0.95)),  # Samyuktha Rani Pink Bridal Silk
        ('product-14.webp', 'Screenshot 2026-10-06 181136.png', (0.5, 0.15, 1.0, 0.98)),   # Vaishnavi Ivory & Gold Bridal Kasavu

        # Lehengas (prod-15 to prod-18)
        ('product-15.webp', 'Screenshot 2026-10-06 181148.png', (0.05, 0.05, 0.95, 0.95)),  # Nila Ivory Chevron Zari Lehenga
        ('product-16.webp', 'Screenshot 2026-10-06 180759.png', (0.05, 0.05, 0.95, 0.95)),  # Haritha Emerald & Kasavu Dhavani
        ('product-17.webp', 'Screenshot 2026-10-06 180840.png', (0.05, 0.1, 0.95, 0.98)),   # Ragini Rani Pink Dhavani Ensemble
        ('product-18.webp', 'Screenshot 2026-10-06 180810.png', (0.55, 0.05, 0.98, 0.95)),  # Manjari Royal Indigo Festive Lehenga

        # Bridal Blouses (prod-19 to prod-22)
        ('product-19.webp', 'Screenshot 2026-10-06 180827.png', (0.08, 0.1, 0.92, 0.85)),   # Aiswarya Signature Zardozi Blouse Back
        ('product-20.webp', 'Screenshot 2026-10-06 180946.png', (0.2, 0.15, 0.88, 0.65)),   # Padmapriya Temple Maggam Sleeve
        ('product-21.webp', 'Screenshot 2026-10-06 180759.png', (0.2, 0.15, 0.85, 0.55)),   # Vanathi Emerald Brocade Puff Blouse
        ('product-22.webp', 'Screenshot 2026-10-06 181028.png', (0.15, 0.15, 0.85, 0.65)),  # Surabhi Golden Beige Cutwork Blouse

        # Custom Dresses (prod-23 to prod-26)
        ('product-23.webp', 'Screenshot 2026-10-06 181336.png', (0.05, 0.02, 0.95, 0.95)),  # Seraphina Blush Pink Mermaid Gown
        ('product-24.webp', 'Screenshot 2026-10-06 181043.png', (0.05, 0.02, 0.95, 0.95)),  # Nocturne Off-Shoulder Evening Dress
        ('product-25.webp', 'Screenshot 2026-10-06 181320.png', (0.05, 0.02, 0.95, 0.95)),  # Evangeline Schiffli Embroidered Dress
        ('product-26.webp', 'Screenshot 2026-10-06 181344.png', (0.05, 0.02, 0.95, 0.95)),  # Celeste Champagne Bridal Gown

        # Ready-mades (prod-27 to prod-29)
        ('product-27.webp', 'Screenshot 2026-10-06 181221.png', (0.15, 0.1, 0.85, 0.65)),   # Tara Hand-Embroidered Kurta Set
        ('product-28.webp', 'Screenshot 2026-10-06 181716.png', (0.25, 0.25, 0.85, 0.85)),  # Gayatri Floral Organza Coord Set
        ('product-29.webp', 'Screenshot 2026-10-06 180854.png', (0.1, 0.1, 0.9, 0.8)),     # Rithanya Mulberry Silk Tunic

        # Kids Wear (prod-30 to prod-31)
        ('product-30.webp', 'Screenshot 2026-10-06 180759.png', (0.1, 0.1, 0.9, 0.9)),     # Chinnu Heritage Kasavu Pavadai
        ('product-31.webp', 'Screenshot 2026-10-06 180840.png', (0.15, 0.15, 0.85, 0.9)),   # Nandhana Silk Pavadai Set

        # Gents Wear (prod-32 to prod-34)
        ('product-32.webp', 'Screenshot 2026-10-06 181136.png', (0.15, 0.05, 0.68, 0.75)),  # Madhav Off-White Raw Silk Kurta Set
        ('product-33.webp', 'Screenshot 2026-10-06 180929.png', (0.05, 0.1, 0.55, 0.95)),   # Aravind Black Shirt & Kasavu Mundu
        ('product-34.webp', 'Screenshot 2026-10-06 181136.png', (0.1, 0.05, 0.65, 0.95)),   # Keshav Golden Kasavu Wedding Mundu
    ]

    for fname, ref, box in prod_specs:
        ref_path = os.path.join(REFS, ref)
        out_path = os.path.join(OUT, fname)
        img = crop_exact(ref_path, box, target_size=(600, 800))
        img.save(out_path, 'WEBP', quality=88, method=6)
        print(f"Created {fname} ({os.path.getsize(out_path)} bytes)")

    print(f"Batch B complete: 34 product images generated in {OUT}!")

if __name__ == '__main__':
    generate_batch_b()
