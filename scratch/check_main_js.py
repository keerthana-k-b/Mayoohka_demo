with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('9000000000 occurrences:', text.count('9000000000'))
print('Your Brand occurrences:', text.count('Your Brand'))
print('yourbrand occurrences:', text.count('yourbrand'))

for i, line in enumerate(text.splitlines(), 1):
    if any(k in line for k in ['9000000000', 'Your Brand', 'yourbrand', 'M LOFT', 'Joel']):
        print(f'{i}: {line.strip()[:100]}')
