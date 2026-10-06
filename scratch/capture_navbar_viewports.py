import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
resolutions = [
    ('1280', 1280, 800),
    ('768', 768, 1024),
    ('430', 430, 932),
    ('390', 390, 844),
    ('360', 360, 800)
]

out_dir = 'D:/Mayoohka_demo/scratch'

for res_name, w, h in resolutions:
    out_shot = f"{out_dir}/header_{res_name}px.png"
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--window-size={w},{h}',
        '--hide-scrollbars',
        '--virtual-time-budget=2000',
        f'--screenshot={out_shot}',
        'http://localhost:8080/index.html'
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, timeout=10)
        if os.path.exists(out_shot):
            print(f"  [OK] header_{res_name}px.png captured ({os.path.getsize(out_shot)} bytes)")
        else:
            print(f"  [FAIL] header_{res_name}px.png")
    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] header_{res_name}px.png")
