import subprocess
import json
import os

urls = [
    ('index', 'http://localhost:8080/index.html'),
    ('collections', 'http://localhost:8080/collections.html'),
    ('about', 'http://localhost:8080/about.html')
]

results = {}

for name, url in urls:
    json_path = f"D:/Mayoohka_demo/scratch/lh_{name}_baseline.json"
    print(f"Running Lighthouse for {name} ({url})...")
    cmd = [
        "npx", "lighthouse", url,
        "--only-categories=performance",
        "--form-factor=mobile",
        "--screenEmulation.mobile=true",
        "--output=json",
        f"--output-path={json_path}",
        '--chrome-flags="--headless=new --no-sandbox"'
    ]
    res = subprocess.run(" ".join(cmd), shell=True, capture_output=True, text=True)
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        score = int(data['categories']['performance']['score'] * 100)
        lcp = data['audits'].get('largest-contentful-paint', {}).get('displayValue', 'N/A')
        cls = data['audits'].get('cumulative-layout-shift', {}).get('displayValue', 'N/A')
        tbt = data['audits'].get('total-blocking-time', {}).get('displayValue', 'N/A')
        weight = data['audits'].get('total-byte-weight', {}).get('displayValue', 'N/A')
        results[name] = {
            'Performance': score,
            'LCP': lcp,
            'CLS': cls,
            'TBT': tbt,
            'PageWeight': weight
        }
        print(f"  {name}: Score={score}, LCP={lcp}, CLS={cls}, TBT={tbt}, Weight={weight}")
    else:
        print(f"  FAILED to generate report for {name}! Error: {res.stderr[:200]}")

print("\n=== BASELINE RESULTS ===")
print(json.dumps(results, indent=2))
with open('D:/Mayoohka_demo/scratch/baseline_summary.json', 'w') as f:
    json.dump(results, f, indent=2)
