# -*- coding: utf-8 -*-
"""ASF SEO fix: substitui o H1 dinamico (cronometro) por <p>, preservando id/JS. Idempotente."""
p = 'index.html'
s = open(p, encoding='utf-8').read()
old = '<h1 id="t" style="text-align:center;font-size:3rem;color:var(--mar)">0:00</h1>'
new = '<p id="t" style="text-align:center;font-size:3rem;color:var(--mar);margin:0;font-weight:bold">0:00</p>'
if old in s:
    open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    print('H1 dinamico corrigido')
else:
    print('Nada a corrigir.')