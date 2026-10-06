import os
import shutil
import pathlib

DEPLOY = pathlib.Path('deploy')
if DEPLOY.exists():
    shutil.rmtree(DEPLOY)
DEPLOY.mkdir(parents=True, exist_ok=True)

# Files to copy to root of deploy
root_files = [
    'index.html',
    'collections.html',
    'about.html',
    'contact.html',
    'reels.html',
    'product-detail.html',
    '404.html',
    'client.json',
    'favicon.ico',
    'favicon.png'
]

for rf in root_files:
    if os.path.exists(rf):
        shutil.copy2(rf, DEPLOY / rf)
        print(f"Copied {rf} to deploy/")

# Directories to copy
dirs_to_copy = ['css', 'js', 'assets']
for d in dirs_to_copy:
    if os.path.exists(d):
        shutil.copytree(d, DEPLOY / d, dirs_exist_ok=True)
        print(f"Copied directory {d} to deploy/{d}")

print("=== DEPLOY MIRROR COMPLETE ===")
# Verify files in deploy
deploy_files = list(DEPLOY.rglob('*'))
print(f"Total items in deploy: {len(deploy_files)}")
