import json,sys,glob,os
D=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,D)
from ui import UI,MODES,INTRO
from loops import LOOPS
out={}
for L in ['zh','ar','ru']:
    stops={}
    for f in sorted(glob.glob(os.path.join(D,'stories',L+'_*.json'))):
        stops.update(json.load(open(f)))
    out[L]={'ui':UI[L],'modes':MODES[L],'intro':INTRO[L],'loops':{k:v[L] for k,v in LOOPS.items()},'stops':stops}
    print(L,len(stops),'stops',sum(1 for v in stops.values() if len(v)>5 and v[5]),'longs')
js=open(os.path.join(D,'apply.js')).read()+'\nwindow.MF_I18N = '+json.dumps(out,ensure_ascii=False)+';\n'
open(os.path.join(D,'..','i18n.js'),'w').write(js)
