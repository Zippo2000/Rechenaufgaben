# 📱 Rechenaufgaben App für iPhone

Eine Progressive Web App (PWA) für Rechenaufgaben der 1. Klasse - optimiert für iPhone!

## 📋 Funktionen

✅ Zahlenraum bis 10 oder 20 wählbar
✅ Plus-, Minus- oder gemischte Aufgaben
✅ Sofortige Rückmeldung mit Vibration
✅ Statistik-Tracking
✅ Offline-Funktionalität
✅ Installierbar auf dem Home-Bildschirm
✅ Touch-optimierte Bedienung
✅ Speichert Fortschritt automatisch

## 🚀 So nutzt du die App auf deinem iPhone

### Methode 1: Über Python HTTP Server (Empfohlen für lokales Testen)

1. **Alle Dateien in einen Ordner kopieren**
   - Stelle sicher, dass alle 7 Dateien im gleichen Ordner sind:
     - index.html
     - style.css
     - app.js
     - sw.js
     - manifest.json
     - icon-192.png
     - icon-512.png

2. **Öffne die Kommandozeile/Terminal**
   - Windows: Eingabeaufforderung
   - Mac: Terminal

3. **Navigiere zum Ordner**
   ```bash
   cd Pfad/zum/App-Ordner
   ```

4. **Starte einen lokalen Webserver**
   ```bash
   python -m http.server 8000
   ```

   Du solltest sehen: "Serving HTTP on 0.0.0.0 port 8000..."

5. **Finde deine lokale IP-Adresse**

   **Windows:**
   ```bash
   ipconfig
   ```
   Suche nach "IPv4-Adresse" (z.B. 192.168.1.100)

   **Mac/Linux:**
   ```bash
   ifconfig | grep inet
   ```
   Suche nach einer Adresse wie 192.168.1.100

6. **Öffne Safari auf deinem iPhone**
   - Gib ein: http://DEINE-IP-ADRESSE:8000
   - Beispiel: http://192.168.1.100:8000
   - **WICHTIG:** iPhone und Computer müssen im gleichen WLAN sein!

7. **Installiere die App auf dem Home-Bildschirm**
   - Tippe auf das "Teilen"-Symbol (Quadrat mit Pfeil nach oben)
   - Scrolle runter und wähle "Zum Home-Bildschirm"
   - Bestätige mit "Hinzufügen"
   - Die App erscheint jetzt als Icon auf deinem Bildschirm!

### Methode 2: Über GitHub Pages (Online verfügbar machen)

1. **Erstelle ein GitHub-Konto** (falls noch nicht vorhanden)
   - Gehe zu github.com und registriere dich

2. **Erstelle ein neues Repository**
   - Klicke auf "New Repository"
   - Name: rechenaufgaben-app
   - Wähle "Public"
   - Klicke "Create repository"

3. **Lade alle Dateien hoch**
   - Klicke "uploading an existing file"
   - Ziehe alle 7 Dateien in das Fenster
   - Klicke "Commit changes"

4. **Aktiviere GitHub Pages**
   - Gehe zu "Settings" → "Pages"
   - Wähle "main" als Branch
   - Klicke "Save"
   - Nach 1-2 Minuten ist die App unter https://dein-username.github.io/rechenaufgaben-app erreichbar

5. **Öffne die URL auf dem iPhone**
   - Öffne Safari und gib die GitHub Pages URL ein
   - Installiere wie in Methode 1, Schritt 7 beschrieben

### Methode 3: Mit lokalem Webserver (für Fortgeschrittene)

Falls du bereits einen Webserver wie Apache oder Nginx nutzt:

1. Kopiere alle Dateien in dein Web-Verzeichnis
2. Greife über Safari auf die URL zu
3. Installiere die App auf dem Home-Bildschirm

## 🎮 Bedienung der App

1. **Einstellungen wählen**
   - Zahlenraum: bis 10 oder bis 20
   - Rechenart: Plus, Minus oder Gemischt

2. **Aufgabe erstellen**
   - Tippe auf "🎲 Neue Aufgabe erstellen"

3. **Antwort eingeben**
   - Gib die Lösung ins Eingabefeld ein
   - Die Zahlentastatur öffnet sich automatisch

4. **Prüfen**
   - Tippe auf "✓ Prüfen" oder drücke Enter
   - Du bekommst sofort Feedback mit Vibration

5. **Statistik verfolgen**
   - Am unteren Bildschirmrand siehst du deine Erfolgsquote
   - Die Statistik wird automatisch gespeichert

## 🔧 Technische Details

- **Technologie:** Progressive Web App (PWA)
- **Kompatibilität:** iOS 11.3 und höher
- **Browser:** Safari (erforderlich für Installation)
- **Offline:** Funktioniert auch ohne Internet
- **Speicher:** Verwendet localStorage für Statistiken
- **Vibration:** Nutzt die Vibration API für Feedback

## ✅ Vorteile der PWA gegenüber nativer App

✅ Keine App Store Installation nötig
✅ Kein Mac für Entwicklung erforderlich
✅ Sofort aktualisierbar (einfach Dateien ändern)
✅ Funktioniert auch im Browser
✅ Deutlich einfacher zu entwickeln und zu warten
✅ Plattformübergreifend (funktioniert auch auf Android)

## 🆘 Fehlerbehebung

**Problem: App lädt nicht**
- Prüfe, ob Computer und iPhone im gleichen WLAN sind
- Überprüfe die IP-Adresse
- Stelle sicher, dass der Python-Server läuft

**Problem: Keine Vibration**
- Vibration funktioniert nur auf echten Geräten, nicht im Simulator
- Prüfe, ob "Vibration" in den iPhone-Einstellungen aktiviert ist

**Problem: Statistik verschwindet**
- Die Statistik wird im Browser-Speicher gespeichert
- Wenn du den Safari-Cache löschst, wird auch die Statistik gelöscht

**Problem: Icons werden nicht angezeigt**
- Stelle sicher, dass icon-192.png und icon-512.png vorhanden sind
- Leere den Safari-Cache und lade die Seite neu

## 📝 Anpassungen

Du kannst die App einfach anpassen:

- **Farben ändern:** Bearbeite `style.css`
- **Zahlenraum erweitern:** Ändere die Optionen in `index.html` und `app.js`
- **Neue Rechenarten:** Ergänze die Logik in `app.js`
- **Design anpassen:** Modifiziere `style.css` und `index.html`

## 👨‍👩‍👧‍👦 Für deine Kinder

Diese App wurde speziell für Kinder der 1. Klasse entwickelt und entspricht dem 
Lehrplan für Mathematik im Zahlenraum bis 20. Sie bietet:

- Große, kindgerechte Buttons
- Sofortiges Feedback
- Motivierende Erfolgsmeldungen
- Fortschritts-Tracking ohne Druck
- Einfache, intuitive Bedienung

Viel Spaß beim Üben! 🎓📱
