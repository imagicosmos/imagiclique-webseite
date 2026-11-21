"""Baut den Abschnitt „Stile“ der Webseite aus app/bausteine/stile/katalog.json (statisch) und zieht Menü und Datenschutz nach.
Aufruf im Projektordner (über webseite/): python webseite/werkzeuge/stile_bauen.py, danach rechtsseiten.py (Menü der Unterseiten)"""
import io, json, re, html

APP = 'https://imagicosmos.github.io/imagiclique-app/'
kat = json.load(io.open('app/bausteine/stile/katalog.json', encoding='utf-8'))
p = 'webseite/index.html'
s = io.open(p, encoding='utf-8').read()

karten = []
for st in kat['stile']:
    f = st['farben']
    desc = st['desc'].split(':', 1)[1].strip() if ':' in st['desc'] else st['desc']
    desc = desc[0].upper() + desc[1:] + '.'
    karten.append(
        f'''        <a class="stil zeigen" href="{APP}?stil={st['id']}" rel="noopener">
          <span class="stil-bild" style="background:linear-gradient(135deg,{f['bg1']},{f['bg2']} 60%,{f['acc']});color:{f['fg']}" aria-hidden="true"><span class="stil-zeichen">{st['icon']}</span><span class="stil-strich" style="background:{f['acc']}"></span></span>
          <span class="stil-text"><b>{html.escape(st['name'])}</b><span>{html.escape(desc)}</span><span class="stil-link">In der App öffnen →</span></span>
        </a>''')

abschnitt = f'''  <!-- ===================== STILE ===================== -->
  <!-- Statisch aus app/bausteine/stile/katalog.json erzeugt (kein Abruf von der App-Adresse). Bei neuen Stilen im Katalog neu erzeugen, siehe README.md. -->
  <section class="abschnitt eng" id="stile">
    <div class="breite">
      <div class="abschnitt-kopf zeigen">
        <p class="vorzeile">Stile</p>
        <h2>Für jeden Anlass die passende Farbe.</h2>
        <p>Ein Stil bringt Farben, Schrift und kleinen Schmuck wie Schneeflocken oder Konfetti mit. Tippe auf dem Handy einen Stil an: Er öffnet sich in der App und steht dort im Reiter „Stil“ bereit. Über „Eigenen Stil gestalten“ legst du in der App auch eigene Stile an und gibst sie als Link an Freunde weiter.</p>
      </div>
      <div class="stile">
{chr(10).join(karten)}
      </div>
    </div>
  </section>

'''
a = s.find('  <!-- ===================== STILE')
if a >= 0:
    s = s[:a] + s[s.index("  <!-- ===================== SO GEHT'S"):]
m = "  <!-- ===================== SO GEHT'S"
assert s.count(m) == 1
s = s.replace(m, abschnitt + m)
if 'href="#stile"' not in s:
    n = '      <a href="#funktionen">Funktionen</a>\n'
    assert s.count(n) == 1
    s = s.replace(n, n + '      <a href="#stile">Stile</a>\n')
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)

c = 'webseite/style.css'
css = io.open(c, encoding='utf-8').read()
if '.stile{' not in css:
    css += '''/* Abschnitt „Stile“: Karten aus dem Stil-Katalog der App */
.stile{ display:grid; grid-template-columns:repeat(3,1fr); gap:18px; }
.stil{ display:grid; grid-template-columns:92px 1fr; gap:18px; align-items:center; padding:16px; border-radius:var(--radius); border:1px solid var(--linie); background:var(--kachel-grund); text-decoration:none; transition:border-color .2s, transform .2s; }
.stil:hover{ border-color:color-mix(in srgb, var(--akzent) 50%, transparent); transform:translateY(-2px); }
.stil-bild{ aspect-ratio:9/16; border-radius:12px; display:grid; place-items:center; position:relative; box-shadow:0 0 0 1px var(--linie), 0 10px 24px rgba(0,0,0,.18); }
.stil-zeichen{ font-size:2rem; line-height:1; }
.stil-strich{ position:absolute; left:16%; bottom:14%; width:38%; height:4px; border-radius:2px; }
.stil-text{ display:grid; gap:4px; }
.stil-text b{ font-family:var(--titel); font-weight:400; text-transform:uppercase; font-size:1.35rem; letter-spacing:.01em; }
.stil-text span{ color:var(--leise); font-size:.93rem; }
.stil-text .stil-link{ color:var(--akzent); font-weight:650; margin-top:4px; }
@media (max-width:900px){ .stile{ grid-template-columns:1fr 1fr; } }
@media (max-width:620px){ .stile{ grid-template-columns:1fr; } }
'''
    io.open(c, 'w', encoding='utf-8', newline='\n').write(css)
print('ok', len(karten), 'Stile')
