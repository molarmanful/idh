import sys
from nbformat import read, NO_CONVERT

with open(sys.argv[1]) as f:
    notebook = read(f, NO_CONVERT)

n = 1
for c in notebook['cells']:
    if c['cell_type'] == 'code':
        print('Out[%d]:' % n)
        for o in c['outputs']:
            if o.get('text'):
                print(''.join(o['text']))
            elif o.get('data'):
                for k, v in o['data'].items():
                    if k != 'text/html':
                        print(''.join(v))
        print()
        n += 1
