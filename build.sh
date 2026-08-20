#!/bin/zsh
# Erzeugt aus durbuy.html alle Auslieferungsformen:
#   index.html / docs/index.html  → für GitHub Pages und localhost (Fotos als Dateien, lädt schnell)
#   einzeldatei.html              → alles eingebettet, zum Verschicken oder für Claude
cd "$(dirname "$0")" || exit 1
cp durbuy.html index.html
cp durbuy.html docs/index.html
cp docs/robots.txt robots.txt 2>/dev/null
python3 einbetten.py
echo "index.html ($(du -h index.html | cut -f1)) · einzeldatei.html ($(du -h einzeldatei.html | cut -f1))"
