"""Baut aus durbuy.html eine einzelne Datei, in der auch die Fotos stecken.
   Nutzt nur die 800px-Fassung, damit die Datei nicht ausufert."""
import base64, re, os

src = open("durbuy.html", encoding="utf-8").read()

def datauri(path):
    with open(path, "rb") as f:
        return "data:image/webp;base64," + base64.b64encode(f.read()).decode()

cache = {}
def hole(name):
    if name not in cache:
        cache[name] = datauri(f"img/{name}-800.webp")
    return cache[name]

# srcset entfernen und src durch die eingebettete Fassung ersetzen
def ersetze(m):
    tag = m.group(0)
    name = re.search(r'src="img/([a-z0-9]+)-800\.webp"', tag)
    if not name:
        return tag
    tag = re.sub(r'\s*srcset="[^"]*"', "", tag)
    tag = re.sub(r'\s*sizes="[^"]*"', "", tag)
    tag = tag.replace(f'src="img/{name.group(1)}-800.webp"', f'src="{hole(name.group(1))}"')
    return tag

out = re.sub(r"<img\b[^>]*>", ersetze, src)
open("einzeldatei.html", "w", encoding="utf-8").write(out)
print(f"  {len(cache)} Fotos eingebettet")
