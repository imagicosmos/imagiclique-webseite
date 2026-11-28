"""Erzeugt impressum.html, datenschutz.html, neuigkeiten.html (aus app/neuigkeiten.json), 404.html (Kopf und Fuß aus
index.html) sowie robots.txt, sitemap.xml, llms.txt und _config.yml.
Aufruf im Projektordner (über webseite/): python webseite/werkzeuge/rechtsseiten.py"""
import io, json, html, datetime
src = io.open('webseite/index.html', encoding='utf-8').read()

def seite(titel, inhalt, wurzel='', robots='noindex', beschreibung=''):
    kopf = src[src.index('<header class="kopf">'):src.index('</header>') + 9]
    fuss = src[src.index('<footer class="fuss">'):src.index('</footer>') + 9]
    ix = wurzel + 'index.html'
    kopf = kopf.replace('href="#"', 'href="%s"' % ix).replace('href="#', 'href="%s#' % ix)
    fuss = (fuss.replace('href="#"', 'href="%s"' % ix)
                .replace('href="impressum.html"', 'href="%simpressum.html"' % wurzel)
                .replace('href="datenschutz.html"', 'href="%sdatenschutz.html"' % wurzel)
                .replace('href="neuigkeiten.html"', 'href="%sneuigkeiten.html"' % wurzel))
    meta = '<meta name="robots" content="%s">' % robots
    if beschreibung:
        meta += '\n<meta name="description" content="%s">' % html.escape(beschreibung)
    return f'''<!DOCTYPE html>
<html lang="de" data-modus="hell">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'">
<title>{titel} · Imagiclique</title>
{meta}
<link rel="icon" href="{wurzel}bilder/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{wurzel}bilder/apple-touch-icon.png">
<script src="{wurzel}modus.js"></script>
<link rel="stylesheet" href="{wurzel}style.css">
</head>
<body>
{kopf}
<main id="inhalt">
  <div class="leuchten" aria-hidden="true"></div>
  <article class="breite"><div class="rechtstext">
{inhalt.strip()}
  </div></article>
</main>
{fuss}
<script src="{wurzel}app.js"></script>
<script src="{wurzel}bausteine/zauberstab.js" data-stern="#22c55e" data-band="#86efac" defer></script>
</body>
</html>
'''

ADR = '''<address>
Mario Glaser<br>
Gründelparkweg 5c<br>
08371 Glauchau%s
</address>'''
MAIL = '<a href="mailto:kontakt@imagiclique.de">kontakt@imagiclique.de</a>'

impressum = f'''
<h1>Impressum</h1>
<p><strong>Angaben gemäß § 5 Digitale-Dienste-Gesetz (DDG) und § 18 Abs. 1 Medienstaatsvertrag (MStV)</strong></p>
{ADR % ''}
<h2>Kontakt</h2>
<p>E-Mail: {MAIL}</p>
<h2>Über diese Seite</h2>
<p>Imagiclique ist ein privates Software-Projekt. Diese Seite stellt die App vor und führt zu ihr. Imagiclique ist ein Projekt von <a href="https://imagicosmos.github.io/imagicosmos-webseite/" rel="noopener">Imagicosmos</a>, einer Sammlung von Programmen, die Fotos gestalten und präsentieren.</p>
<p>Imagiclique ist ein unabhängiges Projekt und steht in keiner Verbindung zu WhatsApp oder Meta. „WhatsApp“ ist eine Marke der WhatsApp LLC.</p>
<h2 id="bildnachweis">Bildnachweis</h2>
<p>Die Bilder auf dieser Seite zeigen Imagiclique mit einem erfundenen Beispiel. Die darin gezeigten Fotos stammen aus Wikimedia Commons. Sie wurden verkleinert, zugeschnitten und als Teil der Status-Bilder und Bildschirmfotos verwendet.</p>
<ul>
  <li>Chiemsee bei Chieming: Bananenfalter, <a href="https://commons.wikimedia.org/wiki/File:Chiemsee_chieming_splash.JPG" rel="noopener">Wikimedia Commons</a>, CC0</li>
  <li>„Alpine Meadow“: Dana Hutchinson, <a href="https://commons.wikimedia.org/wiki/File:Alpine_Meadow_(200540915).jpeg" rel="noopener">Wikimedia Commons</a>, Lizenz <a href="https://creativecommons.org/licenses/by/3.0/deed.de" rel="noopener">CC BY 3.0</a></li>
  <li>Kirche St. Peter und Paul, Oberammergau (innen): Jebulon, <a href="https://commons.wikimedia.org/wiki/File:Church_Saint_Peter_Saint_Paul,_inside,_Oberammergau,_Bavaria,_Germany.jpg" rel="noopener">Wikimedia Commons</a>, CC0</li>
  <li>Zwei goldene Eheringe: Rgaudin, <a href="https://commons.wikimedia.org/wiki/File:Two_golden_wedding_rings.jpg" rel="noopener">Wikimedia Commons</a>, CC0</li>
</ul>
<h2>Links zu anderen Seiten</h2>
<p>Diese Seite enthält Links zu anderen Webseiten (zum Beispiel zur App bei GitHub Pages). Für deren Inhalte sind die jeweiligen Anbieter verantwortlich. Bei Hinweisen auf rechtswidrige Inhalte entferne ich den Link umgehend.</p>
'''

datenschutz = f'''
<h1>Datenschutz</h1>
<p>Kurz gesagt: Diese Webseite setzt <strong>keine Cookies</strong>, nutzt <strong>keine Statistik- oder Werbedienste</strong> und lädt <strong>keine Inhalte von fremden Servern</strong> (auch keine Schriften). Es gibt kein Kontaktformular und kein Benutzerkonto.</p>
<p>Der erste Teil gilt für den Besuch dieser Webseite. Was die <strong>App</strong> Imagiclique mit Daten macht, steht im Abschnitt <a href="#app">Die App Imagiclique</a>.</p>

<h2>Verantwortlich</h2>
{ADR % ('<br>' + chr(10) + 'E-Mail: ' + MAIL)}

<h2>Bereitstellung der Seite (Hosting)</h2>
<p>Diese Seite wird über <strong>GitHub Pages</strong> ausgeliefert. Anbieter ist die GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite verarbeitet GitHub technisch notwendige Daten, insbesondere deine <strong>IP-Adresse</strong>, Datum und Uhrzeit, die aufgerufene Seite und Angaben zu Browser und Betriebssystem. Das ist nötig, um die Seite auszuliefern und sie gegen Angriffe zu schützen.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und funktionierenden Webseite). Dabei können Daten in die USA übermittelt werden. GitHub ist nach dem EU-US Data Privacy Framework zertifiziert; dafür besteht ein Angemessenheitsbeschluss der EU-Kommission (Art. 45 DSGVO). Mehr dazu in der <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>

<h2>Hell oder dunkel</h2>
<p>Wenn du oben rechts auf ☀/☾ klickst, merkt sich dein Browser deine Wahl („hell“ oder „dunkel“) im lokalen Speicher deines Geräts. Diese Angabe wird nicht übertragen, und du kannst sie jederzeit über die Einstellungen deines Browsers löschen. Sie wird nur gespeichert, weil du die Funktion ausdrücklich nutzt (§ 25 Abs. 2 Nr. 2 TDDDG).</p>

<h2>Kontakt per E-Mail</h2>
<p>Wenn du mir eine E-Mail schreibst, verwende ich deine Angaben nur, um deine Anfrage zu beantworten (Art. 6 Abs. 1 lit. b bzw. f DSGVO). Ich lösche sie, sobald sie dafür nicht mehr nötig sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>

<h2 id="app">Die App Imagiclique</h2>
<p>Imagiclique ist eine Web-App. Sie läuft im Browser auf deinem Handy. <strong>Es gibt kein Konto, und ich erhalte weder deine Fotos noch deine Texte, deine Musik oder deine Sprachaufnahmen.</strong> Die Status-Bilder und Videos werden auf deinem Gerät erzeugt.</p>

<h3>Auslieferung der App</h3>
<p>Die App wird ebenfalls über GitHub Pages ausgeliefert (Adresse <code>imagicosmos.github.io</code>). Beim Öffnen und bei Aktualisierungen verarbeitet GitHub dieselben technischen Daten wie oben beschrieben.</p>

<h3>Was auf deinem Gerät gespeichert wird</h3>
<p>Damit du nach dem Schließen weitermachen kannst, speichert die App im Speicher deines Browsers: deine Fotos in verkleinerter Fassung, geholte Videos, die Gruppen mit Texten und Einstellungen, gewählte Musik und Sprachaufnahmen, außerdem an welchen Tagen du geteilt oder gespeichert hast (für das Ausblenden des Schriftzugs) welche Erklärungen du schon gesehen hast und welche Stile und Layouts du hinzugefügt hast (nur Farben, Namen, Schmuck- und Flächenangaben). Für die Nutzung ohne Netz legt sie ihre eigenen Dateien in einem Zwischenspeicher ab.</p>
<p>Nichts davon wird übertragen. Du löschst es mit „Neu beginnen“ in der App oder vollständig über die Einstellungen deines Browsers („Websitedaten löschen“) bzw. durch Deinstallieren der App. Die Speicherung ist für die von dir gewünschte Funktion erforderlich (§ 25 Abs. 2 Nr. 2 TDDDG).</p>

<h3>Stile</h3>
<p>Öffnest du in der App die Seite „Stile“ oder einen Link zu einem Stil, ruft die App den Stil-Katalog und den gewählten Stil von derselben Adresse ab, von der auch die App kommt (GitHub Pages). Ein weiterer Anbieter ist nicht beteiligt. Gibst du einen eigenen Stil als Link weiter, stehen seine Angaben im Link selbst hinter dem Zeichen „#“; dieser Teil wird beim Öffnen an keinen Server übertragen. Den Link verschickst du selbst über das Teilen-Menü.</p>
<p>Ein eigener Stil kann ein Hintergrundbild und einen Rahmen enthalten. Diese Bilder rechnet die App neu (ohne Angaben wie den Aufnahmeort) und speichert sie nur auf deinem Gerät. Einen Stil mit Bildern gibst du als Datei weiter, nicht als Link. <strong>Die Bilder stecken in dieser Datei und gehen mit dem Stil an die Person, der du sie schickst.</strong></p>

<h3>Verbindungen zu anderen Diensten</h3>
<p>Die App nimmt nur in diesen Fällen Verbindung zu anderen Servern auf. Dabei erfährt der jeweilige Anbieter technisch bedingt deine IP-Adresse.</p>
<table class="rechtstabelle">
  <tr><th>Wann</th><th>Dienst</th><th>Was übertragen wird</th></tr>
  <tr><td>Nur wenn du „Infos zum Ort“ antippst</td><td>Wikipedia (Wikimedia Foundation, USA)</td><td>Dein Suchbegriff oder die Koordinaten des Fotos bzw. deines Standorts.</td></tr>
  <tr><td>Nur wenn du diktierst</td><td>Spracherkennung deines Browsers (bei Chrome: Google)</td><td>Die gesprochene Aufnahme, damit daraus Text wird. Das übernimmt dein Browser, nicht die App.</td></tr>
</table>
<p>Aufnahmedatum und -ort liest die App auf deinem Gerät aus dem Foto; dafür wird nichts übertragen. Alle Schriften bringt die App selbst mit; dafür wird ebenfalls nichts übertragen. Rechtsgrundlage für „Infos zum Ort“ und das Diktieren ist deine ausdrückliche Nutzung der Funktion.</p>

<h3>Zugriffe, um die dich dein Handy fragt</h3>
<ul>
  <li><strong>Mikrofon:</strong> für die Sprachaufnahme zur Diashow und fürs Diktieren. Die Sprachaufnahme bleibt auf deinem Gerät.</li>
  <li><strong>Standort:</strong> nur, wenn du bei „Infos zum Ort“ deinen aktuellen Standort wählst.</li>
  <li><strong>Kamera und Fotos:</strong> wenn du Fotos aufnimmst oder auswählst.</li>
</ul>

<h3>Teilen und KI-Hilfe</h3>
<p>Wenn du „Teilen“ antippst, übergibt dein Handy die Bilder oder das Video an die App, die du im Teilen-Menü auswählst (zum Beispiel WhatsApp). Ab dann gelten die Regeln dieses Anbieters. Hat eine Gruppe einen Link, legt die App ihn beim Teilen in die Zwischenablage deines Handys, damit du ihn in der anderen App einfügen kannst. Fügst du einen Link oder die Adresse der Webseite als Bildunterschrift hinzu, legt die App diesen Text zusätzlich in die Zwischenablage.</p>
<p>Die KI-Hilfe sendet selbst nichts, solange du keinen eigenen API-Schlüssel einträgst (siehe unten). Sie erstellt eine Frage (und auf Wunsch ein Übersichtsbild deiner Fotos), die <strong>du</strong> in eine KI-App deiner Wahl kopierst oder teilst. Was du dort eingibst, verarbeitet der jeweilige KI-Anbieter.</p>
<p><strong>Claude direkt fragen (nur mit eigenem API-Schlüssel):</strong> Trägst du in der App einen eigenen API-Schlüssel von Anthropic ein und tippst „Claude direkt fragen“ an, sendet die App die Frage – mit Titel, Text, Wunsch, Aufnahmezeit und gegebenenfalls Aufnahmeort und Wikipedia-Auszügen – und bis zu vier Fotos der Gruppe bzw. beim Entwurf des ganzen Status das Übersichtsbild direkt an Anthropic (api.anthropic.com, Anthropic PBC, USA). Die Anfrage läuft über deinen eigenen Zugang bei Anthropic; dafür gelten dessen Bedingungen und Datenschutzhinweise, und Anthropic berechnet sie deinem Guthaben. Der Schlüssel bleibt im Speicher der App auf deinem Gerät und wird nur an Anthropic gesendet. Ohne Schlüssel sendet die App nichts an eine KI. Rechtsgrundlage ist Art. 6 Abs. 1 lit. a DSGVO (deine Einwilligung durch das Eintragen des Schlüssels und das Antippen); du beendest sie, indem du den Schlüssel im Menü ⋮ „Claude direkt“ entfernst.</p>

<h3 id="android">Imagiclique als Android-App</h3>
<p>Imagiclique gibt es auch als eigenständige Android-App (derzeit in Erprobung, noch nicht im Play Store). Sie zeigt dieselbe Oberfläche und arbeitet genauso auf deinem Gerät: <strong>kein Konto, keine Übertragung deiner Fotos, Texte, Musik oder Sprachaufnahmen an mich.</strong> Es gilt alles oben Beschriebene, mit diesen Unterschieden:</p>
<ul>
  <li><strong>Auslieferung:</strong> Die App lädst du als Datei (<code>imagiclique.apk</code>) von dieser Webseite; dabei verarbeitet GitHub wie bei jedem Seitenaufruf deine IP-Adresse und die technischen Angaben von oben. Die App bringt ihre Dateien und den Stil-Katalog selbst mit. Beim Benutzen wird dafür nichts von GitHub Pages abgerufen.</li>
  <li><strong>Nach neuen Versionen sehen:</strong> Höchstens einmal am Tag ruft die App die kleine Datei <code>version.json</code> von dieser Webseite ab (GitHub Pages, siehe oben), um dir eine neue Fassung zu melden; „Jetzt nachsehen“ auf der Seite „Über Imagiclique“ ruft sie sofort ab. Dabei verarbeitet GitHub wie bei jedem Seitenaufruf deine IP-Adresse und die technischen Angaben von oben; Cookies oder Daten aus der App werden nicht gesendet. Herunterladen und installieren musst du eine neue Fassung selbst. Abschalten kannst du die Abfrage auf der Seite „Über Imagiclique“ mit „Nach neuen Versionen sehen“. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse, Nutzer auf Fehlerbehebungen hinzuweisen).</li>
  <li><strong>Speicher:</strong> Der Bearbeitungsstand liegt im Speicher der App statt im Browser. Du löschst ihn mit „Neu beginnen“, über die Einstellungen deines Handys (Apps → Imagiclique → Speicher) oder durch Deinstallieren.</li>
  <li><strong>Fotos und Aufnahmeort:</strong> Die App bittet um den Zugriff auf deine Fotos, damit sie die ausgewählten Fotos mit ihrem Aufnahmeort lesen kann (im Browser entfernt Android diese Angabe). Sie liest nur die Fotos, die du auswählst oder an sie teilst. Den Aufnahmeort merkt sie sich auf deinem Gerät zum Foto; übertragen wird er nur, wenn du „Infos zum Ort“ antippst (an Wikipedia, siehe oben). In den fertigen Status-Bildern und Videos steht er nicht. Ohne diesen Zugriff funktioniert alles andere weiter.</li>
  <li><strong>Speichern:</strong> „Speichern“ legt Bilder und Videos in die Galerie deines Handys (Album „Imagiclique“), Stil-Dateien in den Ordner „Download/Imagiclique“.</li>
  <li><strong>Teilen:</strong> Zum Teilen legt die App die Dateien in ihren eigenen Zwischenspeicher. Zugriff darauf bekommt nur die App, die du im Teilen-Menü auswählst.</li>
  <li><strong>Übergabe aus anderen Imagi-Apps:</strong> Teilt eine andere App von Imagicosmos (zum Beispiel Imagicruise) Fotos an Imagiclique, kann sie Titel, Text, Datum, Ortsname und Koordinaten getrennt mitgeben. Die App übernimmt Titel und Text in die neue Gruppe, das Datum in die Fußzeile und zu Fotos ohne eigenes Aufnahmedatum, den Ortsnamen in die Suche von „Infos zum Ort“. Die Koordinaten merkt sie sich auf deinem Gerät zu diesen Fotos und nutzt sie nur für „Infos zum Ort“ (an Wikipedia, siehe oben), nicht für Fragen an eine KI.</li>
  <li><strong>Diktieren:</strong> Es läuft über die Spracheingabe deines Handys (meist von Google) statt über den Browser.</li>
  <li><strong>Mikrofon, Standort, Kamera:</strong> wie oben; Android fragt dich jeweils beim ersten Gebrauch.</li>
</ul>

<h2>Deine Rechte</h2>
<p>Du hast das Recht auf</p>
<ul>
  <li>Auskunft über die gespeicherten Daten (Art. 15 DSGVO),</li>
  <li>Berichtigung (Art. 16), Löschung (Art. 17) und Einschränkung der Verarbeitung (Art. 18),</li>
  <li>Datenübertragbarkeit (Art. 20) und Widerspruch gegen die Verarbeitung (Art. 21),</li>
  <li>Beschwerde bei einer Datenschutz-Aufsichtsbehörde (Art. 77), zum Beispiel der deines Wohnorts.</li>
</ul>
<p>Für Anfragen genügt eine E-Mail an die oben genannte Adresse.</p>

<p class="leise" style="margin-top:40px">Stand: November 2026</p>
'''

# Neuigkeiten: aus app/neuigkeiten.json (dieselbe Datei zeigt die App im Menü ⋮). Regeln: docs/neuigkeiten.md
MONATE = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
ART = {'neu': 'Neu', 'besser': 'Besser', 'behoben': 'Behoben'}
neu_daten = json.load(io.open('app/neuigkeiten.json', encoding='utf-8'))
neu_daten['eintraege'] = [e for e in neu_daten['eintraege'] if e.get('version') != 'neu']   # noch nicht freigegeben
def tag(iso):
    d = datetime.date.fromisoformat(iso)
    return '%d. %s %d' % (d.day, MONATE[d.month - 1], d.year)
blöcke = []
for e in neu_daten['eintraege']:
    kopf_ = html.escape(e.get('titel') or ('Fassung ' + e['version'] if e.get('version') else 'Web-App'))
    zusatz = ' · '.join(x for x in [e['version'] if e.get('titel') and e.get('version') else '', tag(e['datum'])] if x)
    punkte = '\n'.join('  <li><span class="neu-art %s">%s</span> %s</li>' % (p['art'], ART[p['art']], html.escape(p['text']))
                       for p in e['punkte'])
    anker = ' id="v%s"' % e['version'] if e.get('version') else ''
    blöcke.append(f'<h2{anker}>{kopf_} <small>{zusatz}</small></h2>\n<ul class="neu-punkte">\n{punkte}\n</ul>')
neueste = next(e for e in neu_daten['eintraege'] if e.get('version'))
neuigkeiten = f'''
<h1>Neuigkeiten</h1>
<p>Imagiclique wächst jede Woche. Hier steht, was in jeder Fassung dazugekommen ist – das Neueste oben. Dieselbe Liste findest du in der App im Menü ⋮ unter „Neuigkeiten“.</p>
<p><a class="knopf" href="index.html#app">Neueste Fassung {neueste['version']} laden</a></p>
''' + '\n'.join(blöcke) + '''
<p class="leise" style="margin-top:40px">Kleinere Umbauten ohne sichtbare Wirkung stehen hier nicht.</p>
'''

nf = '''
<h1>Seite nicht gefunden</h1>
<p>Diese Seite gibt es leider nicht (mehr). Vielleicht hilft der Weg zurück zur Startseite.</p>
<p style="margin-top:28px"><a class="knopf" href="/">Zur Startseite</a></p>
'''

def w(p, s):
    io.open('webseite/' + p, 'w', encoding='utf-8', newline='\n').write(s)

w('impressum.html', seite('Impressum', impressum))
w('datenschutz.html', seite('Datenschutz', datenschutz))
w('neuigkeiten.html', seite('Neuigkeiten', neuigkeiten, robots='index',
  beschreibung='Was in jeder Fassung von Imagiclique neu ist: neue Vorlagen, Funktionen und behobene Fehler.'))
w('404.html', seite('Seite nicht gefunden', nf, '/'))
w('robots.txt', '''# imagiclique.de - reine Informationsseite ohne private Inhalte.
# Alle Suchmaschinen und KI-Dienste duerfen lesen (wie bei imagichron.de, entschieden 11.11.2026).

User-agent: *
Allow: /

Sitemap: https://imagiclique.de/sitemap.xml
''')
w('sitemap.xml', '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Nur Seiten, die in Suchmaschinen erscheinen sollen (Rechtstexte haben „noindex“). Bei Änderungen lastmod anpassen. -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://imagiclique.de/</loc><lastmod>2026-11-15</lastmod></url>
  <url><loc>https://imagiclique.de/neuigkeiten.html</loc><lastmod>''' + neu_daten['eintraege'][0]['datum'] + '''</lastmod></url>
</urlset>
''')
w('llms.txt', '''# Imagiclique

> Imagiclique ist eine App für das Android-Handy, die aus eigenen Fotos und kurzen Texten Status-Bilder im Hochformat (9:16) für WhatsApp macht: mit Vorlagen, Collagen und Diashows als Video. Sprache: Deutsch.

Wichtige Fakten:

- **Läuft auf dem eigenen Handy:** als Android-App (Android 10 oder neuer, Datei zum Laden auf der Startseite) oder als installierbare Web-App in Chrome. Kein Konto, kein Upload der Fotos, keine Nutzungsstatistik.
- **Vorlagen:** Foto + Text, Bericht, Collage (2 bis 12 Fotos), Zitat, Sofortbild, Postkarte, Weißrand, Filmstreifen, Vorher / Nachher und Diashow.
- **Gruppen:** Fotos werden zu Gruppen zusammengefasst, jede Gruppe bekommt eine eigene Gestaltung und wird einzeln an WhatsApp geteilt.
- **Bildbearbeitung:** Fotos drehen, spiegeln, zuschneiden, automatisch verbessern, Helligkeit, Kontrast und Farbe einstellen, Filter. Das eingelesene Foto bleibt erhalten.
- **Diashow als Video** mit eigener Musik oder Sprachaufnahme.
- **Stile:** Farben, Schrift und Schmuck für Anlässe wie Weihnachten, Geburtstag, Silvester, Ostern, Urlaub und Hochzeit; eigene Stile lassen sich als Link weitergeben.
- **Teilen:** über das Teilen-Menü des Handys an WhatsApp, „Mein Status“.
- **Schriftzug im Bild:** Unten rechts steht klein „Imagiclique“. Nach sieben Tagen mit geteiltem oder gespeichertem Status lässt er sich ausblenden.
- **Kosten:** derzeit kostenlos.
- **Stand:** in Entwicklung, Testphase (November 2026). Noch nicht im Play Store; die Android-App gibt es als Datei: https://imagiclique.de/imagiclique.apk
- Imagiclique ist ein unabhängiges Projekt und steht in keiner Verbindung zu WhatsApp oder Meta.

## Seiten

- [Startseite](https://imagiclique.de/): Beispiele, Funktionen, Ablauf, Datenschutz, Weg zur App
- [Neuigkeiten](https://imagiclique.de/neuigkeiten.html): was in jeder Fassung neu ist
- [Datenschutz](https://imagiclique.de/datenschutz.html): Webseite und App

## Verwandt

- [Imagicosmos](https://imagicosmos.github.io/imagicosmos-webseite/): das Dach über Imagiclique und seinen Geschwistern
- [Imagichron](https://imagichron.de/): persönliche Bilder-Zeitreisen (Windows-Programm) aus derselben Familie
''')
w('_config.yml', '''# GitHub Pages (Jekyll): Die Seite besteht aus fertigen Dateien, Jekyll kopiert sie nur.
# Interne Dateien werden nicht mit veröffentlicht.
exclude:
  - README.md
  - werkzeuge
''')
print('ok')
