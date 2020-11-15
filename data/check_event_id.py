import os
from glob import glob
import json
import re

write = ''
searcher = lambda text : re.search(r'(.*) event_id=\"(\d)\".*', text, re.M|re.I)
for jf in glob('./train/*.json'):
    name = jf.split('/')[-1]
    with open(jf, 'r') as f:
        content = json.load(f)
    html = content['html_annotation']
    search = map(searcher, html)

    ls = []
    for res in search:
        if res:
            ls.append(res.group(2))
    for i in set(ls):
        if ls.count(i) > 1:
            write += 'file : {} , id : {}\n'.format(name, i)
    
with open('result.txt', 'w') as f:
    f.write(write)
    
    
