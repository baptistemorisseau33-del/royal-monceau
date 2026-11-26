# usage: python3 conv.py file.py NN   (file defines D = {key: {'zh':[...],'ar':[...],'ru':[...]}}) or LONG = {key:{...: str}}
import sys,json,os,runpy
g=runpy.run_path(sys.argv[1]); nn=sys.argv[2]; out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'stories')
if 'D' in g:
    for L in ['zh','ar','ru']:
        json.dump({k:v[L] for k,v in g['D'].items()},open(f'{out}/{L}_{nn}.json','w'),ensure_ascii=False,indent=0)
    print('short',len(g['D']))
if 'LONG' in g:
    for L in ['zh','ar','ru']:
        json.dump({k:v[L] for k,v in g['LONG'].items()},open(f'{out}/long_{L}_{nn}.json','w'),ensure_ascii=False,indent=0)
    print('long',len(g['LONG']))
