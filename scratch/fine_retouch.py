import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

# Load option 2
img = cv2.imread('D:/Mayoohka_demo/scratch/founder_opt2_headroom.png')
h, w, _ = img.shape
# h=1000, w=800

# Let's inspect coordinates on this 800x1000 image:
# Face region is approximately:
# y: 220 to 450
# x: 340 to 570
# Eyes are approximately at y: 290 to 330, x: 380 to 540
# Mouth is at y: 360 to 410, x: 410 to 510

# Create a skin mask in YCrCb color space
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# Skin range in CrCb: Cr: 133 to 173, Cb: 77 to 127
skin_mask = cv2.inRange(ycrcb, np.array([0, 135, 80]), np.array([255, 175, 125]))

# Restrict skin mask strictly to face and neck (y: 200..500, x: 320..580)
face_region_mask = np.zeros_like(skin_mask)
face_region_mask[220:480, 340:580] = 255
skin_face_mask = cv2.bitwise_and(skin_mask, face_region_mask)

# Exclude eyes, eyebrows and mouth from skin smoothing so they stay sharp
# Eyes/brows: y: 260..340, x: 370..550
# Mouth: y: 360..415, x: 410..520
feature_mask = np.zeros_like(skin_mask)
feature_mask[260:340, 370:550] = 255
feature_mask[365:420, 410:525] = 255
# Dark pixels in feature region are brows, pupils, lips
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dark_features = (gray < 110) & (feature_mask == 255)
# Also red lips
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
lips = (lab[:, :, 1] > 145) & (feature_mask == 255)

exclude_features = (dark_features | lips).astype(np.uint8) * 255
# Dilate features slightly
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
exclude_features = cv2.dilate(exclude_features, kernel)

# Final smoothable skin mask
smooth_skin_mask = cv2.bitwise_and(skin_face_mask, cv2.bitwise_not(exclude_features))
smooth_skin_mask = cv2.GaussianBlur(smooth_skin_mask, (15, 15), 0) / 255.0

# Apply gentle bilateral smoothing to skin
skin_smooth = cv2.bilateralFilter(img, d=9, sigmaColor=35, sigmaSpace=35)

# Blend smoothed skin
skin_blended = np.zeros_like(img, dtype=np.float32)
for c in range(3):
    skin_blended[:, :, c] = img[:, :, c] * (1.0 - smooth_skin_mask * 0.65) + skin_smooth[:, :, c] * (smooth_skin_mask * 0.65)
skin_blended = np.clip(skin_blended, 0, 255).astype(np.uint8)

# Now enhance clarity and sharpness of eyes, smile, jewelry and saree
# Subtle unsharp mask focused on features
high_pass = cv2.subtract(img, cv2.GaussianBlur(img, (0, 0), 1.5))
enhanced = skin_blended.copy()

# Add detail to eyes/brows/mouth
feat_float = (feature_mask / 255.0)[:, :, np.newaxis]
enhanced = np.clip(enhanced.astype(float) + high_pass.astype(float) * 0.45 * feat_float, 0, 255).astype(np.uint8)

# Saree zari enhancement (y: 450..1000)
saree_float = np.zeros((h, w, 1), dtype=float)
saree_float[450:, :] = 1.0
enhanced = np.clip(enhanced.astype(float) + high_pass.astype(float) * 0.35 * saree_float, 0, 255).astype(np.uint8)

# Convert to PIL for subtle color richness
pil_final = Image.fromarray(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))
pil_final = ImageEnhance.Color(pil_final).enhance(1.05)
pil_final = ImageEnhance.Contrast(pil_final).enhance(1.03)

# Save
pil_final.save('D:/Mayoohka_demo/scratch/founder_retouched.png', 'PNG')
print("Saved founder_retouched.png")
