import glob

for f in sorted(glob.glob('*.html')) + ['js/main.js', 'js/products.js', 'css/style.css']:
    with open(f, 'r', encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            if 'Your Brand' in line or 'yourbrand' in line:
                print(f'{f}:{i}: {line.strip()[:100]}')
