import re, math, sys
t=open(sys.argv[1]).read()
assert t.count('{')==t.count('}'), 'brace mismatch'
blks=t.split('\nPART\n{')[1:]
parts={}
for b in blks:
    pid=re.search(r'\n\tpart = (\S+)',b).group(1)
    parts[pid]=dict(links=re.findall(r'\n\tlink = (\S+)',b), sym=re.findall(r'\n\tsym = (\S+)',b),
      attN=re.findall(r'\n\tattN = [^,]+,(\S+?_\d+)_',b), srfN=re.findall(r'\n\tsrfN = srfAttach,([^,]+)',b),
      res=re.findall(r'\n\t\tname = (\w+)\n\t\tamount = (\S+)\n\t\tmaxAmount = (\S+)',b),
      istg=int(re.search(r'\n\tistg = (\S+)',b).group(1)))
assert len(parts)==len(blks)
parent={c:p for p,v in parts.items() for c in v['links']}
roots=[p for p in parts if p not in parent]; assert len(roots)==1, roots
for p,v in parts.items():
    for s in v['sym']: assert s in parts and p in parts[s]['sym']
    for a in v['attN']: assert a in parts and (parent.get(p)==a or parent.get(a)==p), (p,a)
    for s in v['srfN']: assert parent[p]==s
    for n,a,m in v['res']: assert a==m, (p,n)
print('structure OK, root', roots[0], len(parts),'parts')
