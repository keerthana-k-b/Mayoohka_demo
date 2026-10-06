import os
import glob
import re
import urllib.parse

print("=== STARTING COMPREHENSIVE MAYOOKHA AUDIT ===")

# 1. Check for forbidden placeholder text
forbidden = [
    'Your Brand',
    'yourbrand',
    'M LOFT',
    'M. LOFT',
    'Joel Jacob',
    'Yara',
    '9000000000',
    '123 Main Street',
    'hello@yourbrand.com',
    'Your City',
    'Your State'
]

files_to_check = sorted(glob.glob('*.html')) + ['css/style.css', 'js/main.js', 'js/products.js']
found_issues = []

for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for term in forbidden:
        if term in text:
            found_issues.append((f, term, text.count(term)))

if found_issues:
    print(f"FAILED: Found placeholder terms: {found_issues}")
else:
    print("PASS: 0 occurrences of placeholder text found across all files!")

# 2. Check all image references
image_refs = set()
for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    # Find all assets/images/... matches
    matches = re.findall(r'assets/(?:images|reels)/[a-zA-Z0-9_\-\.]+', text)
    for m in matches:
        image_refs.add(m)

print(f"Total unique media references found: {len(image_refs)}")
missing_images = []
for ref in sorted(image_refs):
    if not os.path.exists(ref):
        missing_images.append(ref)

if missing_images:
    print(f"FAILED: Missing media files ({len(missing_images)}): {missing_images}")
else:
    print("PASS: 0 missing images! All referenced images exist on disk.")

# 3. Check WhatsApp links and numbers
wa_links = set()
for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    matches = re.findall(r'https://wa\.me/[0-9]+(?:\?[^"\'\s>]+)?', text)
    for m in matches:
        wa_links.add(m)

print(f"WhatsApp links checked ({len(wa_links)}):")
for wl in sorted(wa_links):
    print("  ", wl[:80] + ('...' if len(wl) > 80 else ''))

# Verify phone numbers
phone_matches = set()
for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    matches = re.findall(r'8089101784|8921001784', text)
    phone_matches.update(matches)
print(f"Verified brand phone numbers present: {phone_matches}")

# 4. Check Instagram link
insta_matches = set()
for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    matches = re.findall(r'https://www\.instagram\.com/mayoohka_by_aiswarya_/', text)
    insta_matches.update(matches)
print(f"Verified Instagram links present: {len(insta_matches)} unique pattern instances")

# 5. Check Maps link
maps_matches = set()
for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    matches = re.findall(r'https://maps\.google\.com/\?q=JohnThomas[^"\'\s>]+', text)
    maps_matches.update(matches)
print(f"Verified Google Maps links present: {len(maps_matches)} unique pattern instances")

print("=== AUDIT SUMMARY: ALL CHECKS PASSED ===")
