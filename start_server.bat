@echo off
echo ===============================================
echo  Rechenaufgaben App - Server starten
echo ===============================================
echo.
echo Der Server wird auf Port 8000 gestartet...
echo.

python -m http.server 8000

echo.
echo Server wurde beendet.
pause
