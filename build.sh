#!/bin/zsh
# Kopiert die Seite an beide Stellen, die GitHub Pages veröffentlichen kann.
# Egal ob du beim Einrichten "root" oder "/docs" auswählst – es funktioniert.
cd "$(dirname "$0")" || exit 1
cp durbuy.html index.html
cp durbuy.html docs/index.html
cp docs/robots.txt robots.txt 2>/dev/null
echo "index.html und docs/index.html aktualisiert ($(du -h index.html | cut -f1))"
