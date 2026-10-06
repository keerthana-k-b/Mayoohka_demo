with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'[^\n]*\.collection-card[^\n]*\{[^}]*\}', text)
for m in matches[:10]:
    print(m)

print('--- hover on collection ---')
for line in text.splitlines():
    if 'collection-card' in line and 'hover' in line:
        print(line)

print('--- hover on product ---')
for line in text.splitlines():
    if 'product-card' in line and 'hover' in line:
        print(line)
