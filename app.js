// Service Worker Registration
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
setTimeout(zeigeInstallPrompt, 3000);