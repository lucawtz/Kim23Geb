#!/bin/zsh
# Kopiert die Seite in den Ordner, den GitHub Pages veröffentlicht.
# Nach jeder Änderung an durbuy.html einmal ausführen.
cd "$(dirname "$0")" || exit 1
cp durbuy.html docs/index.html
echo "docs/index.html aktualisiert ($(du -h docs/index.html | cut -f1))"
