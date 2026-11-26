# Builds the "vous" story set (Baptiste's 2026-11-26 criteria) into stories.js.
import glob, json, re, os
here = os.path.dirname(os.path.abspath(__file__))
V = {}
for f in sorted(glob.glob(os.path.join(here, 'b[0-9]*.py'))):
    g = {}; exec(open(f).read(), g); V.update(g['V'])
TXT = {k: [v['sfr'], v['sen']] for k, v in V.items()}
LNG = {k: [v['lfr'], v['len']] for k, v in V.items()}
HK = {k: [v['hook_fr'], v['look_fr'], v['hook_en'], v['look_en']] for k, v in V.items() if 'hook_fr' in v}
p = os.path.join(here, '..', '..', 'stories.js')
s = open(p).read()
a, b = '\n// V2-START', '// V2-END\n'
if a in s: s = s[:s.index(a)] + s[s.index(b) + len(b):]
block = (a + ' histoires au vouvoiement (générées par i18n-src/v2/build_v2.py)\n'
         'Object.assign(window.MF_TXT, ' + json.dumps(TXT, ensure_ascii=False) + ');\n'
         'Object.assign(window.MF_LONG, ' + json.dumps(LNG, ensure_ascii=False) + ');\n'
         'window.MF_HOOK = ' + json.dumps(HK, ensure_ascii=False) + ';\n' + b)
s = s.rstrip('\n') + '\n' + block
open(p, 'w').write(s)
# report
for k, v in V.items():
    n = lambda t: len(t.split())
    print('%-40s S %3d/%3d  L %3d/%3d' % (k[:40], n(v['sfr']), n(v['sen']), n(v['lfr']), n(v['len'])))
print('total', len(V))
