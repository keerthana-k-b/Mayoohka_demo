import subprocess
import os
import time

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pages = [
    ('index', 'http://localhost:8080/index.html'),
    ('collections', 'http://localhost:8080/collections.html'),
    ('about', 'http://localhost:8080/about.html'),
    ('contact', 'http://localhost:8080/contact.html'),
    ('reels', 'http://localhost:8080/reels.html'),
    ('product_detail', 'http://localhost:8080/product-detail.html?id=prod-bs-1'),
    ('page404', 'http://localhost:8080/404.html')
]

resolutions = [
    ('390', 390, 844),
    ('768', 768, 1024)
]

out_dir = 'D:/Mayoohka_demo/scratch'

for res_name, w, h in resolutions:
    print(f"\n=== Testing {res_name}px ({w}x{h}) ===")
    for name, url in pages:
        out_shot = f"{out_dir}/{name}_{res_name}px.png"
        cmd = [
            chrome_path,
            '--headless=new',
            f'--window-size={w},{h}',
            '--hide-scrollbars',
            f'--screenshot={out_shot}',
            url
        ]
        res = subprocess.run(cmd, capture_output=True, timeout=15)
        if os.path.exists(out_shot):
            size = os.path.getsize(out_shot)
            print(f"  [OK] {name}_{res_name}px.png captured ({size} bytes)")
        else:
            print(f"  [FAIL] {name}_{res_name}px.png failed to capture! Return code: {res.returncode}")

print("\nFinished all responsive screenshot tests.")
