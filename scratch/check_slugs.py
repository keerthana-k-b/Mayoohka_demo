import glob

slugs = [
    'ethnic-wear',
    'western-wear',
    'occasion-wear',
    'festive-collection',
    'casual-wear',
    'new-arrivals',
    'artisanal-craft',
    'signature-series'
]

html_files = sorted(glob.glob('*.html'))
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    found = [s for s in slugs if s in text]
    print(f, 'found slugs:', found)
