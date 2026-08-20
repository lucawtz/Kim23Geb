#!/bin/zsh
# Startet einen kleinen lokalen Webserver für die Durbuy-Seite
# und öffnet sie im Browser. Zum Beenden: Fenster schließen oder Strg+C.

cd "$(dirname "$0")" || exit 1

PORT=8080
while lsof -nP -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; do
  PORT=$((PORT+1))
  if [ $PORT -gt 8100 ]; then echo "Kein freier Port gefunden."; exit 1; fi
done

IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)

echo ""
echo "  Route 23 läuft."
echo ""
echo "    Auf diesem Rechner:  http://localhost:$PORT/durbuy.html"
[ -n "$IP" ] && echo "    Im selben WLAN:      http://$IP:$PORT/durbuy.html"
echo ""
echo "  (Beenden mit Strg+C)"
echo ""

( sleep 1; open "http://localhost:$PORT/durbuy.html" ) &
python3 -m http.server "$PORT" --bind 0.0.0.0 2>/dev/null
