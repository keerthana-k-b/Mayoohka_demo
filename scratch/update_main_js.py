with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Your Brand — Main Client Logic', 'MAYOOKHA – The Bridal Studio — Main Client Logic')
text = text.replace('Hi Your Brand', 'Hi Mayookha')
text = text.replace('Hello Your Brand', 'Hello Mayookha')
text = text.replace('919000000000', '918089101784')
text = text.replace("card.dataset.category || 'Your Brand'", "card.dataset.category || 'MAYOOKHA'")
text = text.replace('Handcrafted contemporary apparel by Your Brand.', 'Bespoke bridal couture and designer apparel by MAYOOKHA.')
text = text.replace("c.dataset.title || 'Your Brand Showcase'", "c.dataset.title || 'MAYOOKHA Bridal Studio'")
text = text.replace('Your Brand', 'MAYOOKHA')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated js/main.js successfully')
