import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's take full-page screenshots or use a simple HTML test page that anchors directly to #site-footer
# or inject JS via a simple wrapper or open with URL hash #siteFooter
for res_name, w, h in [('390', 390, 844), ('768', 768, 1024)]:
    out_shot = f"D:/Mayoohka_demo/scratch/footer_{res_name}px.png"
    # index.html has footer with class .site-footer
    # We can create a 1-line script or test url
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--window-size={w},2000', # larger vertical window to see footer
        '--hide-scrollbars',
        '--virtual-time-budget=2000',
        f'--screenshot={out_shot}',
        'http://localhost:8080/404.html' # 404 is shorter so footer is immediately visible!
    ]
    subprocess.run(cmd, capture_output=True, timeout=10)
    print(f"Captured {out_shot} ({os.path.getsize(out_shot) if os.path.exists(out_shot) else 0} bytes)")

