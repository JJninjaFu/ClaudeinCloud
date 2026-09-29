"""Generate 'Hard Hat Heavy' KSP 1.12 .craft file from stock part templates.

Templates (full MODULE/RESOURCE blocks) are lifted from kRPC's 1.12.5 test craft,
then re-positioned, re-linked and re-staged here.

  git clone --depth 1 https://github.com/krpc/krpc
  python3 gen.py "Hard Hat Heavy.craft" krpc/service/SpaceCenter/test/craft/
"""
import re, glob, math, random, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from q import qmul, qconj, qrot, qy

SRC = sys.argv[2] if len(sys.argv) > 2 else 'krpc/service/SpaceCenter/test/craft/'
PREF = ['Staging.craft', 'Parts.craft', 'Resources.craft', 'PartsParachute.craft']
STOCK_STRIP = {'KOSNameTag'}

# ---------- templates ----------
def blocks(path):
    t = open(path, encoding='utf-8', errors='replace').read().replace('\r', '')
    if 'version = 1.12' not in t[:200]:
        return []
    out = []
    for b in t.split('\nPART\n{')[1:]:
        b = b.rsplit('\n}', 1)[0] if b.rstrip().endswith('}') else b
        out.append(b)
    return out

files = [SRC + f for f in PREF] + sorted(glob.glob(SRC + '*.craft'))
TEMPL = {}
for f in files:
    for b in blocks(f):
        name = re.search(r'\tpart = (\S+)_\d+', b).group(1)
        TEMPL.setdefault(name, b)

def split_top_nodes(body):
    """Split the tail (from first top-level EVENTS) into top-level nodes."""
    lines = body.split('\n')
    i = next(k for k, l in enumerate(lines) if l == '\tEVENTS')
    tail = lines[i:]
    nodes, cur, depth = [], [], 0
    for l in tail:
        if not l.strip():
            continue
        cur.append(l)
        depth += l.count('{') - l.count('}')
        if depth == 0 and l.strip() == '}':
            nodes.append(cur); cur = []
    assert not cur, cur
    return nodes

def body_for(name, tweaks=None):
    nodes = split_top_nodes(TEMPL[name])
    out = []
    for n in nodes:
        text = '\n'.join(n)
        if n[0].strip() == 'MODULE':
            mname = re.search(r'\n\t\tname = (\S+)', text).group(1)
            if mname in STOCK_STRIP:
                continue
        if n[0].strip() == 'RESOURCE':
            mx = re.search(r'\n\t\tmaxAmount = (\S+)', text).group(1)
            text = re.sub(r'\n\t\tamount = \S+', '\n\t\tamount = ' + mx, text)
        if tweaks:
            text = tweaks(text)
        out.append(text)
    return '\n'.join(out)

# ---------- vessel tree ----------
rng = random.Random(1969)
PARTS = []
_next = [4294100000]

class P:
    def __init__(s, name, pos, rot=(0, 0, 0, 1), parent=None, attm=0, istg=-1, sepI=-1, dstg=0,
                 staged=False, pnode=None, cnode=None, srfN=None, tweaks=None, strut='Off'):
        _next[0] -= 37
        s.name, s.id = name, f'{name}_{_next[0]}'
        s.pid = rng.randrange(10**8, 4 * 10**9)
        s.pos, s.rot, s.parent, s.attm = pos, rot, parent, attm
        s.istg, s.sepI, s.dstg, s.staged = istg, sepI, dstg, staged
        s.links, s.attN, s.sym = [], [], []
        s.srfN, s.tweaks, s.strut = srfN, tweaks, strut
        s.sidx = -1
        if parent:
            parent.links.append(s)
            if pnode:  # stack attach: (parent node name, parent node y, child node name, child node y)
                pn, py, cn, cy = pnode
                d = lambda y: f'0|{y:g}|0_0|{1 if y > 0 else -1}|0_0|{y:g}|0_0|{1 if y > 0 else -1}|0'
                parent.attN.append(f'{pn},{s.id}_{d(py)}')
                s.attN.append(f'{cn},{parent.id}_{d(cy)}')
        PARTS.append(s)

def stack(parent, pnode, py, name, cnode, cy, **kw):
    # child node sits on parent node: child center = parent center + py - cy
    pos = (parent.pos[0], parent.pos[1] + py - cy, parent.pos[2])
    return P(name, pos, parent=parent, pnode=(pnode, py, cnode, cy), **kw)

def add(v, w): return tuple(a + b for a, b in zip(v, w))

def abort(module, *actions):
    """Tweak: bind the given actions of `module` to the Abort action group."""
    def tw(t):
        if not re.search(r'\n\t\tname = ' + re.escape(module) + r'\n', t):
            return t
        for a in actions:
            t = re.sub(r'(\n\t\t\t' + a + r'\n\t\t\t\{\n\t\t\t\tactionGroup = )None', r'\1Abort', t)
        return t
    return tw

# Stage plan (KSP counts down; highest fires first)
S_LAUNCH, S_SRB_SEP, S_LES, S_CORE_SEP, S_POD_SEP, S_CHUTES = 5, 4, 3, 2, 1, 0

Y = 22.0
pod = P('mk1-3pod', (0, Y, 0), dstg=0)
sep1 = stack(pod, 'top', 1.19318998, 'Separator.1', 'bottom', -0.0500000007,
             istg=S_LES, sepI=S_LES, dstg=1, staged=True)
les = stack(sep1, 'top', 0.0500000007, 'LaunchEscapeSystem', 'bottom', -1.37254405,
            istg=S_LES, sepI=S_LES, dstg=2, staged=True, tweaks=abort('ModuleEnginesFX', 'ActivateAction'))
sep2 = stack(pod, 'bottom', -0.47924, 'Separator.2', 'top', 0.100000001,
             istg=S_POD_SEP, sepI=S_POD_SEP, dstg=1, staged=True, tweaks=abort('ModuleDecouple', 'DecoupleAction'))
up_tank = stack(sep2, 'bottom', -0.100000001, 'Rockomax32.BW', 'top', 1.86000001,
                istg=S_POD_SEP, sepI=S_POD_SEP, dstg=2)
poodle = stack(up_tank, 'bottom', -1.86000001, 'liquidEngine2-2.v2', 'top', 0,
               istg=S_CORE_SEP, sepI=S_POD_SEP, dstg=2, staged=True, tweaks=abort('ModuleEngines', 'ShutdownAction'))
dec2 = stack(poodle, 'bottom', -1.5, 'Decoupler.2', 'top', 0.100000001,
             istg=S_CORE_SEP, sepI=S_CORE_SEP, dstg=3, staged=True)
core_top = stack(dec2, 'bottom', -0.100000001, 'Rockomax32.BW', 'top', 1.86000001,
                 istg=S_CORE_SEP, sepI=S_CORE_SEP, dstg=4)
core = stack(core_top, 'bottom', -1.86000001, 'Rockomax64.BW', 'top', 3.73000002,
             istg=S_CORE_SEP, sepI=S_CORE_SEP, dstg=4)
mainsail = stack(core, 'bottom', -3.73000002, 'liquidEngineMainsail.v2', 'top', 1.01358998,
                 istg=S_LAUNCH, sepI=S_CORE_SEP, dstg=4, staged=True, tweaks=abort('ModuleEngines', 'ShutdownAction'))

# Radial chutes on the pod: copied placement from a stock-built 1.12.5 craft
CHUTES = [((-0.2188, 0.4881, -0.8165), (-0.196113095, -0.127947196, 0.0258187801, -0.971855223))]
chutes = []
for k in range(4):
    qa = qy(90 * k)
    d, r = CHUTES[0]
    chutes.append(P('parachuteRadial', add(pod.pos, qrot(qa, d)), qmul(qa, r), parent=pod, attm=1,
                    istg=S_CHUTES, sepI=-1, dstg=0, staged=True,
                    srfN=f'srfAttach,{pod.id},,0|0|0,0|0|-1,0|0|0'))

# Four Kickbacks on TT-70s. Base transforms (booster toward -z) from a stock
# Rockomax64 > radialDecoupler2 > MassiveBooster assembly.
DEC_D = (0, 0, -1.1781); DEC_R = (0, 0.707106829, 0, -0.707106829)
SRB_D = (0, 0.3939, -1.2527); SRB_R = (0, -1, 0, 0)
DEC_Y = mainsail.pos[1] - 1.95704997 + 7.43561602 - 0.3939 + 0.35  # SRB nozzles just above Mainsail bell

def kick_tweak(t):
    return t.replace('\t\tthrustPercentage = 100', '\t\tthrustPercentage = 80')

# Sepratron local frame on the Kickback: outer side (local +z), near the nose,
# nozzle up (local y flipped) so they retro-fire and flick the nose outward.
def mat_to_q(x, y, z):
    m00, m01, m02 = x[0], y[0], z[0]
    m10, m11, m12 = x[1], y[1], z[1]
    m20, m21, m22 = x[2], y[2], z[2]
    tr = m00 + m11 + m22
    if tr > 0:
        s = math.sqrt(tr + 1) * 2
        return ((m21 - m12) / s, (m02 - m20) / s, (m10 - m01) / s, 0.25 * s)
    if m00 > m11 and m00 > m22:
        s = math.sqrt(1 + m00 - m11 - m22) * 2
        return (0.25 * s, (m01 + m10) / s, (m02 + m20) / s, (m21 - m12) / s)
    if m11 > m22:
        s = math.sqrt(1 + m11 - m00 - m22) * 2
        return ((m01 + m10) / s, 0.25 * s, (m12 + m21) / s, (m02 - m20) / s)
    s = math.sqrt(1 + m22 - m00 - m11) * 2
    return ((m02 + m20) / s, (m12 + m21) / s, 0.25 * s, (m10 - m01) / s)

def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

SEP_LOCAL = []
for side in (-1, 1):
    a = math.radians(30 * side)
    n = (math.sin(a), 0, math.cos(a))
    yv = (0, -1, 0)
    xv = cross(yv, n)
    SEP_LOCAL.append(((0.64 * n[0], 5.2, 0.64 * n[2]), mat_to_q(xv, yv, n)))

decs, srbs, seps = [], [], [[], []]
for k in range(4):
    qa = qy(90 * k)
    dpos = add((core.pos[0], DEC_Y, core.pos[2]), qrot(qa, DEC_D))
    dec = P('radialDecoupler2', dpos, qmul(qa, DEC_R), parent=core, attm=1,
            istg=S_SRB_SEP, sepI=S_SRB_SEP, dstg=5, staged=True,
            srfN=f'srfAttach,{core.id},,-0.0299999993|0|0,1|0|0,-0.0299999993|0|0')
    srot = qmul(qa, SRB_R)
    srb = P('MassiveBooster', add(dpos, qrot(qa, SRB_D)), srot, parent=dec, attm=1,
            istg=S_LAUNCH, sepI=S_SRB_SEP, dstg=6, staged=True, tweaks=kick_tweak, strut='Grandparent',
            srfN=f'srfAttach,{dec.id},,0|0|-0.63499999,0|0|1,0|0|-0.63499999')
    decs.append(dec); srbs.append(srb)
    for j, (dl, rl) in enumerate(SEP_LOCAL):
        seps[j].append(P('sepMotor1', add(srb.pos, qrot(srot, dl)), qmul(srot, rl), parent=srb, attm=1,
                         istg=S_SRB_SEP, sepI=S_SRB_SEP, dstg=6, staged=True,
                         srfN=f'srfAttach,{srb.id},,0|0|0,0|0|1.25,0|0|0'))

for group in [chutes, decs, srbs] + seps:
    for p in group:
        p.sym = [o for o in group if o is not p]

# staging indices within each stage
for st in range(0, 6):
    for i, p in enumerate([p for p in PARTS if p.staged and p.istg == st]):
        p.sidx = i

# ---------- write ----------
def f(v): return ','.join(f'{c:.7g}' if abs(c) > 1e-9 else '0' for c in v)

DESC = ("Hard Hat Heavy: 3-kerbal Mk1-3 crew rocket, 6 stages, all stock (KSP 1.12). "
        "Stage order: [5] Mainsail + 4 Kickbacks (80% thrust) liftoff, "
        "[4] TT-70s kick the Kickbacks loose while 8 Sepratrons retro-fire their noses outward, "
        "[3] pop the launch escape tower, [2] drop the core and light the Poodle, "
        "[1] pod separation, [0] 4 radial chutes. "
        "About 7 km/s vacuum dV: orbit with the core, then the Poodle has around 3.7 km/s for a Mun or Minmus trip and home. "
        "ABORT (Backspace): cuts the liquid engines, blows the pod off the stack and fires the escape tower; then stage off the tower and pop chutes. "
        "Gravity turn at 60-80 m/s, about 45 degrees by 10 km.")

lines = [
    'ship = Hard Hat Heavy', 'version = 1.12.5', f'description = {DESC}', 'type = VAB',
    'size = 5.8,24.2,5.8', 'steamPublishedFileId = 0', f'persistentId = {rng.randrange(10**8, 4*10**9)}',
    'rot = 0,0,0,1', 'missionFlag = Squad/Flags/default', 'vesselType = Ship',
    'OverrideDefault = False,False,False,False', 'OverrideActionControl = 0,0,0,0',
    'OverrideAxisControl = 0,0,0,0', 'OverrideGroupNames = ,,,',
]
for p in PARTS:
    par = p.parent
    if par:
        lpos = qrot(qconj(par.rot), tuple(a - b for a, b in zip(p.pos, par.pos)))
        lrot = qmul(qconj(par.rot), p.rot)
    else:
        lpos, lrot = p.pos, p.rot
    h = [
        f'part = {p.id}', 'partName = Part', f'persistentId = {p.pid}',
        f'pos = {f(p.pos)}', 'attPos = 0,0,0', f'attPos0 = {f(lpos)}',
        f'rot = {f(p.rot)}', 'attRot = 0,0,0,1', f'attRot0 = {f(lrot)}',
        'mir = 1,1,1', 'symMethod = Radial', f'autostrutMode = {p.strut}', 'rigidAttachment = False',
        f'istg = {p.istg}', 'resPri = 0', f'dstg = {p.dstg}', f'sidx = {p.sidx}',
        f'sqor = {p.istg if p.staged else -1}', f'sepI = {p.sepI}', f'attm = {p.attm}',
        'sameVesselCollision = False', 'modCost = 0', 'modMass = 0', 'modSize = 0,0,0',
    ]
    h += [f'link = {c.id}' for c in p.links]
    h += [f'sym = {o.id}' for o in p.sym]
    h += [f'attN = {a}' for a in p.attN]
    if p.srfN:
        h.append(f'srfN = {p.srfN}')
    lines += ['PART', '{'] + ['\t' + x for x in h] + [body_for(p.name, p.tweaks), '}']

open(sys.argv[1], 'w', newline='\n').write('\n'.join(lines) + '\n')
print(len(PARTS), 'parts written')
for p in PARTS:
    print(f'{p.name:28s} y={p.pos[1]:8.3f} r={math.hypot(p.pos[0], p.pos[2]):6.3f} istg={p.istg} sepI={p.sepI} sidx={p.sidx}')
