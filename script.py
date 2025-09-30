
# Erstelle eine Progressive Web App (PWA) für iPhone
# Diese kann direkt im Browser genutzt und auf dem Homescreen installiert werden

# 1. HTML-Datei erstellen
html_code = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Rechenaufgaben">
    <link rel="apple-touch-icon" href="icon-192.png">
    <link rel="manifest" href="manifest.json">
    <title>Rechenaufgaben - 1. Klasse</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🎓 Rechenaufgaben</h1>
            <p class="subtitle">1. Klasse</p>
        </header>

        <div class="settings-card">
            <h2>⚙️ Einstellungen</h2>
            
            <div class="setting-group">
                <label>Zahlenraum:</label>
                <div class="radio-group">
                    <button class="radio-btn active" data-value="10" data-group="zahlenraum">bis 10</button>
                    <button class="radio-btn" data-value="20" data-group="zahlenraum">bis 20</button>
                </div>
            </div>

            <div class="setting-group">
                <label>Rechenart:</label>
                <div class="radio-group">
                    <button class="radio-btn" data-value="plus" data-group="rechenart">Plus</button>
                    <button class="radio-btn" data-value="minus" data-group="rechenart">Minus</button>
                    <button class="radio-btn active" data-value="gemischt" data-group="rechenart">Gemischt</button>
                </div>
            </div>
        </div>

        <button class="new-task-btn" id="neueAufgabe">
            🎲 Neue Aufgabe erstellen
        </button>

        <div class="task-card" id="taskCard">
            <div class="task-display" id="taskDisplay">
                Drücke den Button, um eine Aufgabe zu erstellen!
            </div>

            <div class="answer-section" id="answerSection" style="display: none;">
                <label for="answer">Deine Antwort:</label>
                <input type="number" id="answer" inputmode="numeric" pattern="[0-9]*">
                <button class="check-btn" id="checkBtn">✓ Prüfen</button>
            </div>

            <div class="result" id="result"></div>
        </div>

        <div class="stats" id="stats">
            Richtig: 0 | Gesamt: 0 | Erfolgsquote: 0%
        </div>

        <div class="install-prompt" id="installPrompt" style="display: none;">
            <p>📱 Tipp: Füge diese App zum Home-Bildschirm hinzu!</p>
            <small>Safari → Teilen → Zum Home-Bildschirm</small>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>'''

# 2. CSS-Datei erstellen
css_code = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 500px;
    margin: 0 auto;
}

header {
    text-align: center;
    color: white;
    margin-bottom: 30px;
    padding-top: env(safe-area-inset-top);
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 5px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.subtitle {
    font-size: 1.2em;
    opacity: 0.9;
}

.settings-card, .task-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.settings-card h2 {
    margin-bottom: 20px;
    color: #667eea;
    font-size: 1.3em;
}

.setting-group {
    margin-bottom: 20px;
}

.setting-group label {
    display: block;
    margin-bottom: 10px;
    font-weight: 600;
    color: #555;
}

.radio-group {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.radio-btn {
    flex: 1;
    min-width: 80px;
    padding: 12px 20px;
    border: 2px solid #e0e0e0;
    background: white;
    border-radius: 12px;
    font-size: 1em;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    color: #666;
}

.radio-btn.active {
    background: #667eea;
    border-color: #667eea;
    color: white;
    transform: scale(1.05);
}

.new-task-btn {
    width: 100%;
    padding: 20px;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border: none;
    border-radius: 15px;
    color: white;
    font-size: 1.3em;
    font-weight: bold;
    cursor: pointer;
    margin-bottom: 20px;
    box-shadow: 0 5px 15px rgba(245, 87, 108, 0.4);
    transition: transform 0.2s ease;
}

.new-task-btn:active {
    transform: scale(0.95);
}

.task-display {
    font-size: 3em;
    font-weight: bold;
    text-align: center;
    color: #667eea;
    padding: 40px 20px;
    min-height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.answer-section {
    text-align: center;
    margin-top: 20px;
}

.answer-section label {
    display: block;
    margin-bottom: 10px;
    font-weight: 600;
    color: #555;
}

.answer-section input {
    width: 120px;
    padding: 15px;
    font-size: 2em;
    text-align: center;
    border: 3px solid #e0e0e0;
    border-radius: 12px;
    margin-bottom: 15px;
    font-weight: bold;
}

.answer-section input:focus {
    outline: none;
    border-color: #667eea;
}

.check-btn {
    width: 100%;
    padding: 15px;
    background: #4CAF50;
    border: none;
    border-radius: 12px;
    color: white;
    font-size: 1.2em;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.2s ease;
}

.check-btn:active {
    transform: scale(0.95);
}

.result {
    margin-top: 20px;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-size: 1.1em;
    font-weight: bold;
    min-height: 50px;
}

.result.correct {
    background: #d4edda;
    color: #155724;
}

.result.incorrect {
    background: #f8d7da;
    color: #721c24;
}

.stats {
    background: rgba(255,255,255,0.2);
    color: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: 600;
    backdrop-filter: blur(10px);
}

.install-prompt {
    background: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.install-prompt p {
    font-weight: bold;
    color: #667eea;
    margin-bottom: 10px;
}

.install-prompt small {
    color: #666;
}

/* iOS Safari spezifische Anpassungen */
@supports (-webkit-touch-callout: none) {
    body {
        padding-bottom: env(safe-area-inset-bottom);
    }
}'''

# 3. JavaScript-Datei erstellen
js_code = '''// Service Worker Registration
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js')
        .then(reg => console.log('Service Worker registriert'))
        .catch(err => console.log('Service Worker Fehler:', err));
}

// App State
let state = {
    zahlenraum: 10,
    rechenart: 'gemischt',
    aktuelleAufgabe: null,
    korrekteAntwort: null,
    statistik: {
        richtig: 0,
        gesamt: 0
    }
};

// Statistik aus LocalStorage laden
function ladeStatistik() {
    const gespeichert = localStorage.getItem('rechenStatistik');
    if (gespeichert) {
        state.statistik = JSON.parse(gespeichert);
        aktualisiereStatistik();
    }
}

// Statistik speichern
function speichereStatistik() {
    localStorage.setItem('rechenStatistik', JSON.stringify(state.statistik));
}

// Radio Buttons Handler
document.querySelectorAll('.radio-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const gruppe = this.dataset.group;
        const wert = this.dataset.value;
        
        // Deaktiviere alle Buttons in der Gruppe
        document.querySelectorAll(`[data-group="${gruppe}"]`).forEach(b => {
            b.classList.remove('active');
        });
        
        // Aktiviere den geklickten Button
        this.classList.add('active');
        
        // Aktualisiere State
        state[gruppe] = wert;
    });
});

// Neue Aufgabe erstellen
document.getElementById('neueAufgabe').addEventListener('click', neueAufgabe);

function neueAufgabe() {
    const maxZahl = parseInt(state.zahlenraum);
    let operation;
    
    // Rechenart bestimmen
    if (state.rechenart === 'gemischt') {
        operation = Math.random() > 0.5 ? '+' : '-';
    } else if (state.rechenart === 'plus') {
        operation = '+';
    } else {
        operation = '-';
    }
    
    let zahl1, zahl2;
    
    // Zahlen generieren
    if (operation === '+') {
        zahl1 = Math.floor(Math.random() * (maxZahl + 1));
        zahl2 = Math.floor(Math.random() * (maxZahl - zahl1 + 1));
        state.korrekteAntwort = zahl1 + zahl2;
    } else {
        zahl1 = Math.floor(Math.random() * maxZahl) + 1;
        zahl2 = Math.floor(Math.random() * (zahl1 + 1));
        state.korrekteAntwort = zahl1 - zahl2;
    }
    
    // Aufgabe anzeigen
    state.aktuelleAufgabe = `${zahl1} ${operation} ${zahl2}`;
    document.getElementById('taskDisplay').textContent = `${state.aktuelleAufgabe} = ?`;
    
    // Antwortbereich anzeigen
    document.getElementById('answerSection').style.display = 'block';
    document.getElementById('answer').value = '';
    document.getElementById('result').textContent = '';
    document.getElementById('result').className = 'result';
    
    // Fokus auf Eingabefeld
    setTimeout(() => {
        document.getElementById('answer').focus();
    }, 100);
}

// Antwort prüfen
document.getElementById('checkBtn').addEventListener('click', pruefeAntwort);
document.getElementById('answer').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        pruefeAntwort();
    }
});

function pruefeAntwort() {
    const antwort = parseInt(document.getElementById('answer').value);
    const resultDiv = document.getElementById('result');
    
    if (isNaN(antwort)) {
        alert('Bitte gib eine Zahl ein!');
        return;
    }
    
    state.statistik.gesamt++;
    
    if (antwort === state.korrekteAntwort) {
        state.statistik.richtig++;
        resultDiv.textContent = '✓ Richtig! Super gemacht! 🎉';
        resultDiv.className = 'result correct';
        
        // Vibration bei Erfolg (falls verfügbar)
        if (navigator.vibrate) {
            navigator.vibrate([100, 50, 100]);
        }
    } else {
        resultDiv.textContent = `✗ Leider falsch. Die richtige Antwort ist ${state.korrekteAntwort}`;
        resultDiv.className = 'result incorrect';
        
        // Kurze Vibration bei Fehler
        if (navigator.vibrate) {
            navigator.vibrate(200);
        }
    }
    
    aktualisiereStatistik();
    speichereStatistik();
}

// Statistik aktualisieren
function aktualisiereStatistik() {
    const prozent = state.statistik.gesamt > 0 
        ? Math.round((state.statistik.richtig / state.statistik.gesamt) * 100)
        : 0;
    
    document.getElementById('stats').textContent = 
        `Richtig: ${state.statistik.richtig} | Gesamt: ${state.statistik.gesamt} | Erfolgsquote: ${prozent}%`;
}

// Install Prompt für iOS
function zeigeInstallPrompt() {
    // Prüfe ob die App bereits installiert ist
    if (!window.navigator.standalone) {
        document.getElementById('installPrompt').style.display = 'block';
    }
}

// Initialisierung
ladeStatistik();
setTimeout(zeigeInstallPrompt, 3000);'''

# 4. Service Worker erstellen
sw_code = '''const CACHE_NAME = 'rechenaufgaben-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/style.css',
    '/app.js',
    '/manifest.json',
    '/icon-192.png',
    '/icon-512.png'
];

// Installation
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(urlsToCache))
    );
});

// Aktivierung
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Fetch
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});'''

# 5. Manifest.json erstellen
manifest_code = '''{
    "name": "Rechenaufgaben 1. Klasse",
    "short_name": "Rechenaufgaben",
    "description": "Lern-App für Rechenaufgaben der ersten Klasse",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#667eea",
    "theme_color": "#667eea",
    "orientation": "portrait",
    "icons": [
        {
            "src": "icon-192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "any maskable"
        },
        {
            "src": "icon-512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "any maskable"
        }
    ]
}'''

# Dateien speichern
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_code)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw_code)

with open('manifest.json', 'w', encoding='utf-8') as f:
    f.write(manifest_code)

print("✓ Progressive Web App erfolgreich erstellt!")
print("\nErstellte Dateien:")
print("- index.html (Hauptseite)")
print("- style.css (Design)")
print("- app.js (Funktionalität)")
print("- sw.js (Service Worker für Offline-Funktion)")
print("- manifest.json (App-Konfiguration)")
print("\nDie App ist optimiert für iPhone und kann zum Home-Bildschirm hinzugefügt werden!")
