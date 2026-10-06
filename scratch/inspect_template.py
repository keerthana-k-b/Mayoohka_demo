import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="collections"')
if pos != -1:
    print('=== id="collections" section ===')
    print(text[pos:pos+2500])
else:
    print('id="collections" not found')
