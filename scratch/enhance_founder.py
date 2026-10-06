import os
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

def enhance_portrait(input_path, output_path, target_size=(1000, 1250)):
    target_w, target_h = target_size
    
    # 1. Load original image
    raw = Image.open(input_path).convert('RGB')
    raw_w, raw_h = raw.size
    print(f"Original size: {raw_w} x {raw_h}")
    
    # Backup original if not already backed up
    backup_path = 'D:/Mayoohka_demo/assets/images/owner-orig.png'
    if not os.path.exists(backup_path):
        raw.save(backup_path)
        print(f"Backed up original to {backup_path}")
        
    # 2. Advanced Multi-step Upscaling & Denoising of the subject
    # Scale factor to make person fit comfortably in target_h
    # She should take up about 85-90% of the vertical height (leaving good headroom and room at bottom)
    scale_factor = (target_h * 0.94) / raw_h
    scaled_subject_w = int(raw_w * scale_factor)
    scaled_subject_h = int(raw_h * scale_factor)
    
    # High-quality Lanczos resampling
    upscaled = raw.resize((scaled_subject_w, scaled_subject_h), Image.Resampling.LANCZOS)
    
    # Convert to numpy/OpenCV for computational photography
    img_np = np.array(upscaled) # RGB
    bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    
    # Denoise using bilateral filter to smooth compression artifacts while keeping edges sharp
    # bilateralFilter(src, d, sigmaColor, sigmaSpace)
    denoised_bgr = cv2.bilateralFilter(bgr, d=7, sigmaColor=35, sigmaSpace=35)
    
    # Convert to LAB for luminance detail enhancement (CLAHE)
    lab = cv2.cvtColor(denoised_bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    # CLAHE on L channel for silk and jewelry micro-contrast
    clahe = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8))
    l_clahe = clahe.apply(l)
    
    # Blend CLAHE subtly with original L to keep it natural
    l_enhanced = cv2.addWeighted(l, 0.4, l_clahe, 0.6, 0)
    lab_enhanced = cv2.merge([l_enhanced, a, b])
    enhanced_bgr = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)
    
    # Unsharp Masking for crisp focus on face, jewelry, and saree texture
    gaussian = cv2.GaussianBlur(enhanced_bgr, (0, 0), sigmaX=1.5)
    unsharp = cv2.addWeighted(enhanced_bgr, 1.45, gaussian, -0.45, 0)
    
    # Convert back to PIL for color grading and background composition
    enhanced_pil = Image.fromarray(cv2.cvtColor(unsharp, cv2.COLOR_BGR2RGB))
    
    # Micro color vibrance & contrast polish
    enhancer_col = ImageEnhance.Color(enhanced_pil)
    enhanced_pil = enhancer_col.enhance(1.08) # Rich jewel tone saree
    
    enhancer_con = ImageEnhance.Contrast(enhanced_pil)
    enhanced_pil = enhancer_con.enhance(1.05)
    
    # 3. Create Studio Background Canvas (1000 x 1250)
    # The original background has a warm golden-beige textured wallpaper with ambient boutique lighting
    # Top wall color: ~RGB(236, 184, 118), Left wall: ~RGB(188, 131, 71), Right wall: ~RGB(160, 96, 53)
    # Let's create an elegant luxury boutique studio backdrop matching the tone
    canvas = np.zeros((target_h, target_w, 3), dtype=np.float32)
    
    # Base warm gradient: warmer at top/center, richer golden-bronze at edges
    y_coords, x_coords = np.ogrid[:target_h, :target_w]
    
    # Center of radial light near the founder's head / upper body
    cx, cy = target_w / 2.0, target_h * 0.35
    dist_sq = ((x_coords - cx) / (target_w * 0.6)) ** 2 + ((y_coords - cy) / (target_h * 0.55)) ** 2
    radial_falloff = np.clip(1.0 - 0.38 * np.sqrt(dist_sq), 0.55, 1.0)
    
    # Base warm studio colors (matching the wallpaper in the photo)
    # Warm cream-gold center, rich terracotta-bronze perimeter
    center_color = np.array([238, 192, 135], dtype=np.float32)
    edge_color = np.array([175, 118, 68], dtype=np.float32)
    
    for c in range(3):
        canvas[:, :, c] = edge_color[c] + (center_color[c] - edge_color[c]) * radial_falloff
        
    # Sample real wallpaper texture from the top of the original image
    wall_sample = np.array(raw.crop((0, 0, raw_w, int(raw_h * 0.12))))
    wall_sample_upscaled = cv2.resize(wall_sample, (target_w, int(target_h * 0.15)), interpolation=cv2.INTER_CUBIC)
    
    # Add subtle organic noise/texture to avoid flat digital look
    np.random.seed(42)
    grain = np.random.normal(0, 3.5, (target_h, target_w, 3))
    canvas = np.clip(canvas + grain, 0, 255).astype(np.uint8)
    
    canvas_pil = Image.fromarray(canvas)
    
    # 4. Seamless Composite
    # Position the enhanced subject in center
    pos_x = (target_w - scaled_subject_w) // 2
    pos_y = int(target_h * 0.04) # Good headroom
    
    # Create smooth edge blending mask for the left and right borders of the subject
    # The subject photo includes the wall behind her. By softly feathering the left/right edges of the subject crop,
    # it melts into the extended studio backdrop.
    subject_np = np.array(enhanced_pil)
    sh, sw, _ = subject_np.shape
    
    # Blend mask
    mask = np.ones((sh, sw), dtype=np.float32)
    feather_w = int(sw * 0.12)
    for i in range(feather_w):
        val = np.sin((i / feather_w) * (np.pi / 2)) ** 2
        mask[:, i] = val
        mask[:, sw - 1 - i] = val
        
    # Feather top as well
    feather_h = int(sh * 0.05)
    for j in range(feather_h):
        val = np.sin((j / feather_h) * (np.pi / 2)) ** 2
        mask[j, :] = np.minimum(mask[j, :], val)
        
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    
    # Extract canvas region
    canvas_crop = np.array(canvas_pil.crop((pos_x, pos_y, pos_x + sw, pos_y + sh))).astype(np.float32)
    
    # Alpha blend subject onto canvas
    blended_region = (subject_np.astype(np.float32) * mask_3d + canvas_crop * (1.0 - mask_3d)).astype(np.uint8)
    
    canvas_pil.paste(Image.fromarray(blended_region), (pos_x, pos_y))
    
    # 5. Final Master Polish (Vignette & Micro-sharpness)
    final_np = np.array(canvas_pil)
    
    # Soft luxury vignette
    y_idx, x_idx = np.ogrid[:target_h, :target_w]
    vig_dist = np.sqrt(((x_idx - target_w/2) / (target_w * 0.65))**2 + ((y_idx - target_h/2) / (target_h * 0.65))**2)
    vignette = np.clip(1.0 - 0.22 * (vig_dist ** 1.8), 0.72, 1.0)
    for c in range(3):
        final_np[:, :, c] = np.clip(final_np[:, :, c] * vignette, 0, 255)
        
    final_img = Image.fromarray(final_np.astype(np.uint8))
    
    # Apply subtle final sharpness
    final_img = final_img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=2))
    
    # Save optimized PNG
    final_img.save(output_path, 'PNG', optimize=True)
    print(f"Saved enhanced portrait to {output_path} (size: {final_img.size})")
    
    # Also save WebP version for maximum web performance
    webp_path = output_path.replace('.png', '.webp')
    final_img.save(webp_path, 'WEBP', quality=92, method=6)
    print(f"Saved WebP version to {webp_path}")

if __name__ == '__main__':
    enhance_portrait('D:/Mayoohka_demo/assets/images/owner.png', 'D:/Mayoohka_demo/assets/images/owner.png')
