"""Baut aus durbuy.html eine einzelne Datei, in der auch die Fotos und
   das Adressen-PDF stecken. Nutzt nur die 800px-Fassung der Fotos,
   damit die Datei nicht ausufert."""
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

# Auch die Fotos, die das Skript auf den Erlebnis-Karten setzt
karten = ["kanu", "zipline", "platz", "blick", "gasse"]
daten = ",".join('"%s":"%s"' % (k, hole(k)) for k in karten)
out = out.replace("const FOTO_DATA = {};", "const FOTO_DATA = {%s};" % daten)

# Das PDF, das beim Abschicken mitgeht — in der Einzeldatei liegt es
# als Data-URI drin, sonst wuerde es beim Verschicken fehlen.
if os.path.exists("Durbuy-Adressen.pdf"):
    with open("Durbuy-Adressen.pdf", "rb") as f:
        pdf = "data:application/pdf;base64," + base64.b64encode(f.read()).decode()
    out = out.replace('const PDF_DATA = "";', 'const PDF_DATA = "%s";' % pdf)
    print(f"  PDF eingebettet ({len(pdf)//1024} KB als Text)")
else:
    print("  Kein Durbuy-Adressen.pdf gefunden – Einzeldatei bleibt ohne Anhang")
open("einzeldatei.html", "w", encoding="utf-8").write(out)
print(f"  {len(cache)} Fotos eingebettet")
