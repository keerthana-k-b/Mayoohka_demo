import glob

patterns = [
    'Your Brand',
    'yourbrand',
    '9000000000',
    '123 Main Street',
    'hello@yourbrand.com',
    'M LOFT',
    'M. LOFT',
    'Joel Jacob',
    'Yara',
    'Changanassery',
    'Kottayam'
]

html_files = sorted(glob.glob('*.html'))
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    counts = {p: text.count(p) for p in patterns if p in text}
    if counts:
        print(f, counts)
