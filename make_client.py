# import json, shutil, sys, pathlib

# TEMPLATE = pathlib.Path(r"D:\Clothing_Template")
# CLIENTS  = pathlib.Path(r"D:\Clients")
# SKIP = ("make_client.py", "client.json", "PLAN.md", "RENAME_MAP.csv", "*.md")

# # dummy value in template  ->  key in client.json "fields"
# # longest first, so "Your Brand" doesn't break longer strings
# DUMMY = {
#     "123 Main Street, Your City, Your State 000000": "ADDRESS",
#     "hello@yourbrand.com": "EMAIL",
#     "instagram.com/yourbrand": "INSTAGRAM_URL",   # e.g. instagram.com/rose_boutique
#     "+91 90000 00000": "PHONE_DISPLAY",
#     "+919000000000": "PHONE_TEL",
#     "919000000000": "WHATSAPP",                   # digits with country code
#     "Fashion & Apparel": "TAGLINE",
#     "Your Brand": "BRAND_NAME",
# }

# def main(cfg_path):
#     cfg = json.loads(pathlib.Path(cfg_path).read_text(encoding="utf-8"))
#     out = CLIENTS / cfg["folder"]
#     if out.exists():
#         shutil.rmtree(out)
#     shutil.copytree(TEMPLATE, out, ignore=shutil.ignore_patterns(*SKIP))

#     for f in out.rglob("*"):
#         if f.suffix in {".html", ".css", ".js"}:
#             t = f.read_text(encoding="utf-8")
#             for dummy, key in DUMMY.items():
#                 if key in cfg["fields"]:
#                     t = t.replace(dummy, cfg["fields"][key])
#             f.write_text(t, encoding="utf-8")

#     # client's own images/reels override placeholders by same file name
#     src = cfg.get("assets_folder")
#     if src:
#         shutil.copytree(src, out / "assets", dirs_exist_ok=True)

#     shutil.make_archive(str(CLIENTS / cfg["folder"]), "zip", out)
#     print("Done:", out, "+ zip")

# main(sys.argv[1])

import json, re, shutil, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

TEMPLATE = pathlib.Path(r"D:\Clothing_Template")
CLIENTS  = pathlib.Path(r"D:\Clients")
SKIP = ("*.py", "*.md", "*.csv", "client*.json", "_tools", ".git")

# dummy string in template -> key in client.json "fields". ORDER MATTERS (longest first).
DUMMY = {
    "https://maps.google.com/?q=123+Main+Street+Your+City": "MAP_URL",
    "123 Main Street, Your City, Your State 000000": "ADDRESS",
    "hello@yourbrand.com": "EMAIL",
    "https://instagram.com/yourbrand": "INSTAGRAM_URL",
    "@yourbrand": "INSTAGRAM_HANDLE",
    "+91 90000 00000": "PHONE_DISPLAY",
    "+919000000000": "PHONE_TEL",
    "919000000000": "WHATSAPP",
    "Fashion & Apparel": "TAGLINE",
    "Your Brand": "BRAND_NAME",
}
LEFTOVER = re.compile(r"Your Brand|yourbrand|9000000000|Your City|Your\+City|Your State", re.I)

def make_badge(path, initials, gold="#C9A24B", teal="#0F3B3A"):
    S = 512
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((8, 8, S - 8, S - 8), fill=gold)
    d.ellipse((28, 28, S - 28, S - 28), fill=teal)
    d.ellipse((44, 44, S - 44, S - 44), outline=gold, width=4)
    try:
        f = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 200)
    except OSError:
        f = ImageFont.load_default()
    d.text((S / 2, S / 2), initials, font=f, fill=gold, anchor="mm")
    im.save(path)

def main(cfg_path):
    cfg = json.loads(pathlib.Path(cfg_path).read_text(encoding="utf-8"))
    out = CLIENTS / cfg["folder"]
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(TEMPLATE, out, ignore=shutil.ignore_patterns(*SKIP))

    missing = [k for k in DUMMY.values() if k not in cfg["fields"]]
    if missing:
        print("WARNING: not provided (dummy text will remain):", missing)

    for f in out.rglob("*"):
        if f.suffix in {".html", ".css", ".js"}:
            t = f.read_text(encoding="utf-8")
            for dummy, key in DUMMY.items():
                if key in cfg["fields"]:
                    t = t.replace(dummy, cfg["fields"][key])
            f.write_text(t, encoding="utf-8")

    # client's own images/reels override the sample ones by file name
    assets = cfg.get("assets_folder")
    if assets:
        shutil.copytree(assets, out / "assets", dirs_exist_ok=True)

    # logo: client file > file in assets_folder > auto monogram badge
    logo_dst = out / "assets" / "images" / "logo-badge.png"
    if cfg.get("logo"):
        shutil.copy(cfg["logo"], logo_dst)
    elif not (assets and (pathlib.Path(assets) / "images" / "logo-badge.png").exists()):
        initials = "".join(w[0] for w in cfg["fields"]["BRAND_NAME"].split()[:2]).upper()
        make_badge(logo_dst, initials)

    for f in out.rglob("*"):
        if f.suffix in {".html", ".css", ".js"}:
            for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                if LEFTOVER.search(line):
                    print(f"LEFTOVER {f.relative_to(out)}:{n}: {line.strip()[:90]}")

    shutil.make_archive(str(CLIENTS / cfg["folder"]), "zip", out)
    print("Done:", out, "+ zip")

main(sys.argv[1])