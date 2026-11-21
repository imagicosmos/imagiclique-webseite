# Webseite für Imagiclique

Die öffentliche Seite, die **Imagiclique** vorstellt und zur App führt. Aufbau, Gestaltung und Regeln sind von
`../../imagichron-webseite` (imagichron.de) übernommen; die Farben sind das Grün der Marke aus
`../../imagicosmos/marke/`. Erstellt am 15.11.2026, veröffentlicht am 15.11.2026 unter
`imagicosmos.github.io/imagiclique-webseite`; seit 17.11.2026 unter der eigenen Domain **https://imagiclique.de/** (Datei `CNAME`).

Grundsätze wie bei imagichron.de: einfaches HTML/CSS/JavaScript, **nichts von fremden Servern** (keine
Google-Schriften, keine Statistik, keine Cookies), Skripte nur aus eigenen Dateien (Content-Security-Policy im
Seitenkopf).

## Dateien

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Einstieg, Warum, Ansehen, Funktionen, So geht’s, Datenschutz, App, Fragen |
| `impressum.html`, `datenschutz.html` | Pflichtangaben. Die Datenschutzseite hat einen eigenen Abschnitt „Die App Imagiclique“ (`#app`): ändert sich, was die App lädt oder speichert, dort nachziehen. |
| `404.html` | Seite für falsche Adressen (Verweise beginnen mit `/`) |
| `style.css` | gesamtes Aussehen; Farben für hell und dunkel oben als Variablen, Eigenes von Imagiclique im Abschnitt 15 |
| `app.js`, `modus.js` | Hell/Dunkel, Laufband, wechselnde Überschrift, Einblenden, Bilder vergrößern |
| `bausteine/zauberstab.js` | Logo-Animation, gemeinsamer Baustein „zauberstab“ aus `../bausteine` (seit 18.11.2026; nicht von Hand ändern, neu einbauen mit `node ../bausteine/werkzeuge/einbauen.js zauberstab webseite/bausteine`). Wort und Farben liest er aus dem Logo und `style.css`, die Leuchtfarben stehen als `data-stern`/`data-band` in der Einbindung |
| `bilder/` | `favicon.svg` und `apple-touch-icon.png` aus `imagicosmos/marke/`; `status-*.webp` (Bilder aus der App, 720 × 1280), `app-*.webp` (Bildschirmfotos der App), `teilen.jpg` (Vorschaubild beim Teilen des Links, 1200 × 630) |
| `schriften/` | Josefin Sans für den Schriftzug (SIL Open Font License, Lizenztext liegt bei) |
| `robots.txt`, `sitemap.xml`, `llms.txt` | für Suchmaschinen und KI-Suchen; bei neuen Funktionen `llms.txt` mitpflegen |
| `version.json` | neueste Fassung der Android-App (`{ app, version, datum, seite }`); die App sieht dort höchstens einmal am Tag nach (Baustein „aktualisieren“, abschaltbar). Schreibt `android-bauen.cmd --freigabe`; das Veröffentlichen bricht ab, wenn sie nicht zur beigelegten Freigabe-APK passt |
| `imagiclique.apk` (nur online) | die Android-App zum Laden (Abschnitt „App“); legt `werkzeuge/webseite_veroeffentlichen.py` beim Veröffentlichen dazu, ebenso Fassung und Größe in `index.html` (`@@FASSUNG@@`, `@@GROESSE@@`). Nicht in Git |
| `_config.yml` | GitHub Pages lässt `README.md` und `werkzeuge/` weg |
| `werkzeuge/stile_bauen.py` | schreibt den Abschnitt „Stile“ in `index.html` neu, fest aus `../app/bausteine/stile/katalog.json` (Baustein vorlagen) (kein Abruf von der App-Adresse) |
| `werkzeuge/rechtsseiten.py` | erzeugt `impressum.html`, `datenschutz.html`, `neuigkeiten.html` (aus `../app/neuigkeiten.json`), `404.html` (Kopf und Fuß aus `index.html`) sowie `robots.txt`, `sitemap.xml`, `llms.txt`, `_config.yml`. Die Texte dieser Dateien deshalb **im Werkzeug ändern**, nicht in den erzeugten Dateien. |

**Menü auf allen Seiten gleich:** Kopf und Fuß der Unterseiten sind Kopien aus `index.html`. Nach Änderungen am
Menü im Projektordner `python webseite/werkzeuge/rechtsseiten.py` ausführen.

**Neuigkeiten:** Nach jeder Freigabe-Fassung `python webseite/werkzeuge/rechtsseiten.py` ausführen (die Fassung setzt `android-bauen.cmd --freigabe`
in `app/neuigkeiten.json` ein, siehe `../docs/neuigkeiten.md`), dann veröffentlichen.

**Stile:** Kommt im Katalog (Baustein vorlagen, in der App `app/bausteine/stile/katalog.json`) ein Stil dazu, `python webseite/werkzeuge/stile_bauen.py`
ausführen, danach `rechtsseiten.py`. Die Karten verlinken auf `<App-Adresse>?stil=<id>`; die App-Adresse steht
oben im Werkzeug (`APP`).

**Fragen:** Die sichtbaren Fragen und die strukturierten Daten (JSON-LD im `<head>` von `index.html`) müssen
übereinstimmen.

## Beispielbilder

Die Bilder zeigen die echte App mit einem erfundenen Beispiel („Wochenende im Chiemgau“). Die Fotos sind frei
lizenzierte Aufnahmen aus Wikimedia Commons (dieselben wie auf imagichron.de), ohne erkennbare Personen.
Urheber und Lizenz stehen im **Impressum unter „Bildnachweis“**. Wer ein Foto austauscht, muss den Nachweis
anpassen.

| Foto | Lizenz |
|---|---|
| Chiemsee bei Chieming (Bananenfalter) | CC0 |
| „Alpine Meadow“ (Dana Hutchinson) | CC BY 3.0 |
| Kirche St. Peter und Paul, Oberammergau (Jebulon) | CC0 |
| Zwei goldene Eheringe (Rgaudin) | CC0 |

Entstanden sind die Bilder in einem unsichtbaren Chrome: Fotos in die App geladen, Gruppen angelegt, mit
`exportBlobs()` exportiert und als WebP gespeichert; die App-Ansichten als Bildschirmfoto bei 412 px Breite.
Ändert sich die Oberfläche der App deutlich, die drei `app-*.webp` neu aufnehmen.

## Ansehen auf dem eigenen Rechner

Im Ordner `webseite`: `python -m http.server 8798`, dann http://127.0.0.1:8798/ öffnen.

## Veröffentlichen

Dieses Repository (`imagicosmos/imagiclique`) ist privat. Die Seite liegt im öffentlichen Repository
`imagicosmos/imagiclique-webseite`; GitHub Pages liefert dessen Zweig `main` aus.

**Änderungen veröffentlichen:** in `webseite/` ändern, committen, dann im Projektordner
`webseite-veroeffentlichen.cmd` doppelklicken (`--vorschau` legt die fertige Seite nur nach `ausgabe/webseite/`). Es ruft
`werkzeuge/webseite_veroeffentlichen.py` auf: Das nimmt die neueste **Freigabe-Fassung** aus `ausgabe/android/`
(`android-bauen.cmd --freigabe`, mit dem eigenen Schlüssel signiert – Test-Fassungen kommen nie auf die Seite), prüft, dass
`version.json` im Commit dieselbe Fassung nennt, legt sie als `imagiclique.apk` dazu und lädt den committeten Stand von
`webseite/` als einzelnen Commit mit neutralem Autor hoch (Force-Push, wie `app-veroeffentlichen.cmd`). Nichts außerhalb von
`webseite/` außer der APK und keine private E-Mail-Adresse gelangt dorthin. Nach 1–2 Minuten ist der neue Stand online.
Neue Android-Fassung anbieten: `android-bauen.cmd --freigabe`, `webseite/version.json` committen, Webseite veröffentlichen.

Nichts direkt im öffentlichen Repository ändern (auch nicht über die GitHub-Oberfläche): Der nächste Lauf des
Skripts überschreibt es.

## Domain imagiclique.de verbinden (Schritt für Schritt)

**Stand 17.11.2026: Die Domain ist verbunden.** Mario hat das DNS bei IONOS gesetzt und die Datei `CNAME` angelegt; sie liegt auch im
öffentlichen Repository. Geprüft am 17.11.2026: https://imagiclique.de/ zeigt den committeten Stand, `www.`, der Aufruf ohne
`https` und die alte Adresse `imagicosmos.github.io/imagiclique-webseite/` leiten dorthin um, eine falsche Adresse zeigt die
gestaltete Seite „Seite nicht gefunden“. Schritt 5 (Domain für die Organisation bestätigen) hat Mario am 17.11.2026 erledigt. Nicht geprüft: das Vorschaubild
in WhatsApp. Die Schritte unten bleiben als Anleitung stehen (auch für die anderen Projekte).
Vorbild ist imagichron.de (`../../imagichron-webseite/README.md`), dort sind dieselben Einträge gesetzt.

Die Reihenfolge ist wichtig: **erst DNS (Schritt 1–2), dann die Datei `CNAME` (Schritt 3).** Mit `CNAME` leitet
GitHub die github.io-Adresse sofort auf imagiclique.de um – solange das DNS dort noch auf IONOS zeigt, wäre die
Seite gar nicht erreichbar.

### Schritt 1 – bei IONOS: DNS-Einträge setzen (macht Mario)

1. Auf https://www.ionos.de anmelden → **Domains & SSL** → bei `imagiclique.de` auf das Zahnrad → **DNS**.
2. Vorhandene Einträge für die Hauptdomain löschen, die auf IONOS zeigen: die **A**- und **AAAA**-Einträge mit
   Hostname `@` (derzeit `217.160.0.23` und `2001:8d8:100f:f000::200`) und, falls vorhanden, den Eintrag für
   `www` (A, AAAA oder CNAME). **Nicht löschen:** MX- und TXT-Einträge für E-Mail (z. B. `mx00.ionos.de`, SPF),
   falls für die Domain Postfächer eingerichtet sind oder werden sollen.
3. Vier **A**-Einträge anlegen, Hostname `@`, Werte:
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
4. Vier **AAAA**-Einträge anlegen, Hostname `@`, Werte:
   `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
5. Einen **CNAME**-Eintrag anlegen, Hostname `www`, Wert `imagicosmos.github.io` (der Name der Organisation,
   nicht der des Repositorys).
6. TTL kann auf dem Vorschlag von IONOS bleiben (1 Stunde).

Falls bei IONOS für die Domain eine **Weiterleitung** oder ein **Webspace** verbunden ist, diese Verbindung
vorher lösen (Domains & SSL → Domain → „Verwendungsart anpassen“), sonst setzt IONOS die eigenen Einträge wieder.

### Schritt 2 – warten und prüfen

Die Umstellung dauert meist wenige Minuten, höchstens einige Stunden. Prüfen in der Eingabeaufforderung:

```
nslookup imagiclique.de
nslookup www.imagiclique.de
```

Richtig ist es, wenn bei `imagiclique.de` die vier Adressen `185.199.108.153` bis `185.199.111.153` erscheinen und
bei `www.imagiclique.de` der Name `imagicosmos.github.io`.

### Schritt 3 – Datei `CNAME` anlegen und veröffentlichen (macht Claude oder Mario)

1. In `webseite/` eine Datei `CNAME` (ohne Endung) mit genau einer Zeile anlegen: `imagiclique.de`
2. Committen und `webseite-veroeffentlichen.cmd` ausführen.

Die Datei muss hier im Ordner liegen. Trägt man die Domain nur in der GitHub-Oberfläche ein, legt GitHub die
Datei im öffentlichen Repository an, und der nächste Lauf des Skripts löscht sie wieder.

### Schritt 4 – bei GitHub: HTTPS einschalten

1. https://github.com/imagicosmos/imagiclique-webseite → **Settings** → **Pages**.
2. Unter „Custom domain“ muss `imagiclique.de` stehen und nach kurzer Zeit „DNS check successful“ erscheinen.
3. Sobald GitHub das Zertifikat erstellt hat (einige Minuten bis etwa eine Stunde): **„Enforce HTTPS“** anhaken.

### Schritt 5 – empfohlen: Domain für die Organisation bestätigen

So kann niemand sonst `imagiclique.de` auf GitHub verwenden.

1. https://github.com/organizations/imagicosmos/settings/pages → **Add a domain** → `imagiclique.de`.
2. GitHub zeigt einen **TXT**-Eintrag (Hostname `_github-pages-challenge-imagicosmos`, dazu ein Wert).
3. Bei IONOS im DNS der Domain einen **TXT**-Eintrag mit genau diesem Hostnamen und Wert anlegen.
4. Zurück bei GitHub auf **Verify** klicken.

### Schritt 6 – Abschlussprüfung

- https://imagiclique.de/ zeigt die Seite mit Schloss-Symbol; http:// und www. leiten dorthin um.
- https://imagicosmos.github.io/imagiclique-webseite/ leitet auf https://imagiclique.de/ um.
- Eine falsche Adresse (z. B. `/gibtsnicht`) zeigt die gestaltete Seite „Seite nicht gefunden“.
- Den Link in WhatsApp an sich selbst schicken: Es erscheint das Vorschaubild.

Vor einem späteren **Verkauf** zieht die Seite zu Cloudflare Pages um (GitHub Pages ist nicht für Verkaufsseiten
gedacht), wie für imagichron.de vorgesehen. Dafür ändert man nur die DNS-Einträge.

## Noch offen

1. **Domain:** verbunden seit 17.11.2026 (siehe oben). Auch Schritt 5 (Domain für die Organisation bestätigt) ist erledigt.
   Offen nur noch: der Blick auf das Vorschaubild in WhatsApp.
2. **Adresse der App:** Die App liegt weiter unter https://imagicosmos.github.io/imagiclique-app/ (Knopf „App
   öffnen“, Stil-Links; in `werkzeuge/stile_bauen.py` als `APP`). Für den Play Store braucht sie später eine
   Adresse unter der eigenen Domain (z. B. `app.imagiclique.de`). Beim Umzug gehen die auf dem Handy
   gespeicherten Daten verloren – deshalb vor der Testphase mit fremden Testern umziehen.
3. **Imagicosmos:** Impressum und Fußzeile verweisen auf die Dachseite (seit 16.11.2026), vorerst unter
   https://imagicosmos.github.io/imagicosmos-webseite/. Sobald imagicosmos.de verbunden ist, die Adresse umstellen
   (`index.html` Fußzeile, `werkzeuge/rechtsseiten.py` zwei Stellen), Rechtsseiten neu erzeugen.
4. **Rechtstexte prüfen:** Impressum und Datenschutz sind nach dem Muster von imagichron.de geschrieben und nicht
   juristisch geprüft. Die App lädt Schriften von Google Fonts und ein Hilfsprogramm von jsDelivr; das steht
   offen in der Datenschutzseite. Besser wäre, beides in die App zu legen (`app/vendor/`), dann entfallen die
   beiden Zeilen.
