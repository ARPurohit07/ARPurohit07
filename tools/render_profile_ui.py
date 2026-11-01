"""Build self-contained GitHub-safe toolkit cards and linked button artwork."""
from pathlib import Path
from html import escape
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/ui'
OUT.mkdir(exist_ok=True)
FONT = 'Arial, Helvetica, sans-serif'


def icon(name, x, y):
    path = ROOT / 'assets/icons' / f'{name}.svg'
    if path.exists():
        source = path.read_text(encoding='utf-8')
        root = ET.fromstring(source)
        assert root.tag.endswith('svg'), name
        inner = source[source.index('>')+1:source.rfind('</svg>')]
        for ident in set(re.findall(r'id="([^"]+)"', inner)):
            inner = inner.replace(f'id="{ident}"', f'id="{name}-{ident}"')
            inner = inner.replace(f'#{ident})', f'#{name}-{ident})')
            inner = inner.replace(f'"#{ident}"', f'"#{name}-{ident}"')
        return f'<svg x="{x}" y="{y}" width="30" height="30" viewBox="{root.attrib.get("viewBox", "0 0 48 48")}">{inner}</svg>'
    # Concept glyphs are deliberately unbranded, not invented technology logos.
    glyphs = {
        'reactflow': '<path d="M9 9h8v6H9zM5 23h8v6H5zM22 23h8v6h-8zM13 15v4H9v4m4-4h13v4"/>',
        'webgl2': '<path d="m12 10-7 7 7 7m10-14 7 7-7 7m-3-17-4 20"/>',
        'ollama': '<path d="M11 14 9 5q4-2 6 8h4q2-10 6-8l-2 10q4 4 1 10-7 5-14 0-3-7 1-11z"/><path d="M13 20h1m6 0h1m-6 5h4"/>',
        'rag': '<path d="M7 6h14v17H7zM10 10h8m-8 4h6"/><circle cx="23" cy="23" r="5"/><path d="m27 27 4 4"/>',
        'wasm': '<text x="17" y="22" text-anchor="middle" fill="#C4B5FD" stroke="none" font-size="13" font-weight="700">WA</text>',
    }
    return f'<g transform="translate({x} {y})"><rect width="30" height="30" rx="7" fill="#25223B"/><g transform="scale(.88)" fill="none" stroke="#B9B2F2" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{glyphs[name]}</g></g>'


groups = [
    ('languages', 'Languages', [('cpp','C++'),('py','Python'),('ts','TypeScript'),('js','JavaScript')]),
    ('frontend', 'Frontend / graphics', [('react','React'),('html','HTML'),('css','CSS'),('reactflow','React Flow'),('webgl2','WebGL2'),('wasm','WebAssembly')]),
    ('backend-ml', 'Backend / ML', [('nodejs','Node.js'),('fastapi','FastAPI'),('pytorch','PyTorch'),('ollama','Ollama'),('rag','RAG')]),
    ('platforms', 'Data / platforms', [('postgres','PostgreSQL'),('docker','Docker'),('git','Git'),('github','GitHub')]),
]
for slug, title, entries in groups:
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="380" height="194" viewBox="0 0 380 194" role="img" aria-labelledby="title desc" font-family="{FONT}">',
             f'<title id="title">{escape(title)}</title><desc id="desc">{escape(", ".join(label for _,label in entries))}</desc>',
             '<rect x=".5" y=".5" width="379" height="193" rx="12" fill="#11151F" stroke="#2B3041"/>',
             '<rect x="20" y="22" width="3" height="15" rx="1.5" fill="#A78BFA"/>',
             f'<text x="32" y="35" fill="#E7EAF2" font-size="16" font-weight="600">{escape(title)}</text>']
    for n, (name, label) in enumerate(entries):
        x, y = 20 + (n%2)*181, 57 + (n//2)*43
        parts += [icon(name,x,y), f'<text x="{x+40}" y="{y+20}" font-size="14" fill="#C9CEDC">{escape(label)}</text>']
    parts += ['</svg>']
    (OUT/f'toolkit-{slug}.svg').write_text('\n'.join(parts),encoding='utf-8')

for slug, label, width in [('portfolio','Portfolio',126),('galaxy','Explore the map',180),('goodflow','View repository',176),('linkedin','LinkedIn',124)]:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="38" viewBox="0 0 {width} 38" role="img" aria-label="{label}">
<rect x=".5" y=".5" width="{width-1}" height="37" rx="7" fill="#25203C" stroke="#7760B4"/>
<text x="16" y="24" fill="#F0EAFF" font-family="{FONT}" font-size="13" font-weight="600">{label}</text>
<path d="M{width-28} 19h12m-5-5 5 5-5 5" fill="none" stroke="#C4B5FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
    (OUT/f'button-{slug}.svg').write_text(svg,encoding='utf-8')
print('Generated four toolkit panels and four CTA assets.')
