#!/bin/bash

echo "==============================================="
echo " Rechenaufgaben App - Server starten"
echo "==============================================="
echo ""
echo "Der Server wird auf Port 8000 gestartet..."
echo ""
echo "Deine IP-Adressen:"
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "Keine IP gefunden"
else
    # Linux
    hostname -I | awk '{print $1}'
fi
echo ""
echo "Öffne auf dem iPhone: http://DEINE-IP:8000"
echo ""
echo "Drücke Ctrl+C zum Beenden"
echo ""

python3 -m http.server 8000
