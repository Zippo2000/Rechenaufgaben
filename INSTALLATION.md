# 📋 Schnell-Anleitung: App auf iPhone installieren

## Voraussetzungen
- [ ] iPhone mit iOS 11.3 oder neuer
- [ ] Computer und iPhone im gleichen WLAN
- [ ] Python 3 installiert
- [ ] Alle 8 Dateien in einem Ordner

## Schritt-für-Schritt

### 1️⃣ Server starten (Computer)

**Windows:**
- Doppelklick auf `start_server.bat`

**Mac/Linux:**
- Öffne Terminal im Ordner
- `chmod +x start_server.sh`
- `./start_server.sh`

**Manuell:**
```bash
cd Pfad/zum/Ordner
python -m http.server 8000
```

### 2️⃣ IP-Adresse finden (Computer)

**Windows:**
```bash
ipconfig
```
→ Suche "IPv4-Adresse" (z.B. 192.168.1.100)

**Mac:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**Linux:**
```bash
hostname -I
```

### 3️⃣ App öffnen (iPhone)

1. Öffne **Safari** (nicht Chrome!)
2. Gib ein: `http://DEINE-IP:8000`
   - Beispiel: `http://192.168.1.100:8000`
3. App sollte laden ✅

### 4️⃣ Zum Home-Bildschirm hinzufügen (iPhone)

1. Tippe auf das **Teilen**-Symbol (Quadrat mit Pfeil ⬆️)
2. Scrolle runter
3. Wähle **"Zum Home-Bildschirm"**
4. Tippe **"Hinzufügen"**
5. Fertig! 🎉

### 5️⃣ App verwenden

- App startet jetzt wie eine normale App
- Funktioniert auch **offline**
- Statistiken werden gespeichert
- Keine Internet-Verbindung mehr nötig!

## ⚠️ Häufige Probleme

| Problem | Lösung |
|---------|--------|
| "Seite kann nicht geöffnet werden" | Prüfe ob Computer und iPhone im gleichen WLAN sind |
| IP-Adresse funktioniert nicht | Verwende die richtige Netzwerk-IP (nicht 127.0.0.1) |
| Server startet nicht | Prüfe ob Python installiert ist: `python --version` |
| Icons fehlen | Stelle sicher dass icon-192.png und icon-512.png vorhanden sind |

## 🎯 Alternativen

### Option A: GitHub Pages (Online)
1. Erstelle GitHub-Account
2. Neues Repository anlegen
3. Alle Dateien hochladen
4. In Settings → Pages aktivieren
5. URL teilen und auf iPhone öffnen

### Option B: Ngrok (von extern erreichbar)
```bash
# Installiere ngrok
brew install ngrok  # Mac
choco install ngrok # Windows

# Starte Server
python -m http.server 8000

# In neuem Terminal:
ngrok http 8000

# Verwende die ngrok-URL auf dem iPhone
```

## ✅ Checkliste Erfolg

- [ ] Server läuft auf Computer
- [ ] IP-Adresse herausgefunden
- [ ] App öffnet sich in Safari
- [ ] "Zum Home-Bildschirm" funktioniert
- [ ] App-Icon erscheint auf Homescreen
- [ ] App funktioniert auch offline

**Viel Erfolg! 🚀**
