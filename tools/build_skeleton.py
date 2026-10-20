#!/usr/bin/env python3
"""Скелет для анатомического режима: assets/skeleton.bin из костей модели OpenSim Rajagopal 2016.

Кости берутся из той же модели, по которой заданы мышцы ног (anatomy/legs), и переводятся
в системы сегментов приложения теми же правилами, что и точки мышц:
  - бедро, голень: t — проекция на ось «сустав → сустав», делённая на длину сегмента модели;
    поперечные смещения × 1,80/1,70 (anatomy/legs/README.md);
  - таз: от центра своего тазобедренного сустава, оси корпуса (корпус модели отклонён на 4,4° назад от таза),
    все размеры × 1,80/1,70, как у точек мышц таза;
  - стопа: изотропно × 1,06 вокруг голеностопа, t = 0,23 + dx/0,261, высота — от голеностопа;
  - позвоночник, рёбра, лопатки, ключицы: ось от середины тазобедренных к середине плечевых суставов,
    поперечные смещения × 0,958 (anatomy/trunk/README.md);
  - плечо, предплечье: равномерный масштаб сегмента, центр хвата — 0,75 пути от запястья к III пястно-фаланговому
    суставу (anatomy/arms/tools/extract.py), лучевая кость и кисть — в пронации, как в данных рук;
  - кисть: пальцы согнуты до касания грифа, большой палец обхватывает гриф с другой стороны (подбор углов),
    запястье разогнуто так, что ось грифа проходит через центр хвата приложения.
Грубые сетки (бедро — 265 треугольников) сглаживаются подразделением Loop.

Запуск: python3 tools/build_skeleton.py [папка-кэш]
Источник: github.com/opensim-org/opensim-models, Models/Rajagopal/RajagopalLaiUhlrich2023.osim и Geometry/*.vtp.
"""
import json, os, re, struct, sys, urllib.request
import numpy as np
import xml.etree.ElementTree as ET

RAW = 'https://raw.githubusercontent.com/opensim-org/opensim-models/master/'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/.cache/opensim-models')

# эталон приложения (index.html, MREF)
H = 1.8
MREF = dict(trunk=.288*H, thigh=.245*H, shank=.246*H, ua=.186*H, fa=.19*H, foot=.145*H)
HW = .1 * H                # расстояние между тазобедренными суставами приложения
SW = .21 * H               # ширина плеч приложения (между центрами плечевых суставов)
K_LEG = 1.80/1.70          # поперечный масштаб ног и таза
K_TRUNK = 0.958            # поперечный масштаб корпуса
GRIP_FRAC = 0.75


def fetch(rel):
    path = os.path.join(CACHE, rel)
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        urllib.request.urlretrieve(RAW + rel, path)
    return path


def read_vtp(path):
    s = open(path, 'rb').read().decode('latin1')
    P, F = [], []
    for pc in re.findall(r'<Piece(.*?)</Piece>', s, re.S):
        p = np.array(re.search(r'<Points>.*?<DataArray[^>]*>(.*?)</DataArray>', pc, re.S).group(1).split(), float).reshape(-1, 3)
        polys = re.search(r'<Polys>(.*?)</Polys>', pc, re.S).group(1)
        con = np.array(re.search(r'Name="connectivity"[^>]*>(.*?)</DataArray>', polys, re.S).group(1).split(), int)
        off = np.array(re.search(r'Name="offsets"[^>]*>(.*?)</DataArray>', polys, re.S).group(1).split(), int)
        base, start = sum(len(x) for x in P), 0
        for o in off:
            poly = con[start:o]; start = o
            for k in range(1, len(poly) - 1):
                F.append((poly[0] + base, poly[k] + base, poly[k + 1] + base))
        P.append(p)
    return np.vstack(P), np.array(F)


def weld(V, F, tol=1e-6):
    key = np.round(V / tol).astype(np.int64)
    _, idx, inv = np.unique(key, axis=0, return_index=True, return_inverse=True)
    inv = inv.ravel()
    F = inv[F]
    F = F[(F[:, 0] != F[:, 1]) & (F[:, 1] != F[:, 2]) & (F[:, 0] != F[:, 2])]
    return V[idx], F


def components(V, F):
    parent = np.arange(len(V))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for a, b, c in F:
        ra, rb, rc = find(a), find(b), find(c)
        parent[rb] = ra; parent[rc] = ra
    roots = np.array([find(i) for i in range(len(V))])
    out = []
    for r in np.unique(roots):
        vi = np.where(roots == r)[0]
        remap = -np.ones(len(V), int); remap[vi] = np.arange(len(vi))
        fi = F[np.isin(F[:, 0], vi)]
        out.append((V[vi], remap[fi]))
    return out


def loop_subdivide(V, F):
    """Одна итерация подразделения Loop (края с одной гранью — граница)."""
    nV = len(V)
    E = np.sort(np.vstack([F[:, [0, 1]], F[:, [1, 2]], F[:, [2, 0]]]), axis=1)
    Eu, einv = np.unique(E, axis=0, return_inverse=True); einv = einv.ravel()
    nf = len(F)
    fe = einv.reshape(3, nf).T                      # рёбра грани: (0-1), (1-2), (2-0)
    opp = np.concatenate([F[:, 2], F[:, 0], F[:, 1]])  # вершина напротив ребра
    cnt = np.bincount(einv, minlength=len(Eu))
    osum = np.zeros((len(Eu), 3)); np.add.at(osum, einv, V[opp])
    a, b = V[Eu[:, 0]], V[Eu[:, 1]]
    interior = (cnt == 2)[:, None]
    epts = np.where(interior, .375 * (a + b) + .125 * osum, .5 * (a + b))
    # старые вершины
    nb = np.zeros((nV, 3)); val = np.zeros(nV)
    np.add.at(nb, Eu[:, 0], V[Eu[:, 1]]); np.add.at(nb, Eu[:, 1], V[Eu[:, 0]])
    np.add.at(val, Eu[:, 0], 1); np.add.at(val, Eu[:, 1], 1)
    bnd = np.zeros(nV, bool); be = Eu[cnt != 2]; bnd[be.ravel()] = True
    bsum = np.zeros((nV, 3)); np.add.at(bsum, be[:, 0], V[be[:, 1]]); np.add.at(bsum, be[:, 1], V[be[:, 0]])
    n = np.maximum(val, 1)
    beta = (1 / n) * (5 / 8 - (3 / 8 + .25 * np.cos(2 * np.pi / n)) ** 2)
    Vn = (1 - n * beta)[:, None] * V + beta[:, None] * nb
    bc = np.bincount(be.ravel(), minlength=nV)
    Vb = np.where((bc == 2)[:, None], .75 * V + .125 * bsum, V)
    Vn = np.where(bnd[:, None], Vb, Vn)
    m = fe + nV
    F2 = np.vstack([np.c_[F[:, 0], m[:, 0], m[:, 2]], np.c_[F[:, 1], m[:, 1], m[:, 0]],
                    np.c_[F[:, 2], m[:, 2], m[:, 1]], m])
    return np.vstack([Vn, epts]), F2


def rot_xyz(r):
    """Ориентация PhysicalOffsetFrame в OpenSim: последовательные повороты вокруг осей X, Y, Z тела."""
    def R(ax, a):
        c, s = np.cos(a), np.sin(a)
        if ax == 0: return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
        if ax == 1: return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return R(0, r[0]) @ R(1, r[1]) @ R(2, r[2])


def frame_axes(origin, end, ant_hint):
    ax = end - origin; L = np.linalg.norm(ax); ax /= L
    ant = ant_hint - ant_hint.dot(ax) * ax; ant /= np.linalg.norm(ant)
    lat = np.cross(ant, ax)
    if lat[2] < 0: lat = -lat               # кости правой стороны: +z — наружу
    return ax, ant, lat, L


def to_seg(V, origin, ax, ant, lat, k_ax, k_tr):
    d = V - origin
    return np.c_[d @ ax * k_ax, d @ ant * k_tr, d @ lat * k_tr]


# ---------- кисть в хвате ----------
FINGERS = (('index', 2), ('middle', 3), ('ring', 4), ('little', 5))
CARPALS = ('pisiform', 'lunate', 'scaphoid', 'triquetrum', 'hamate', 'capitate', 'trapezoid', 'trapezium')


def rodrigues(axis, ang):
    a = axis / np.linalg.norm(axis); K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def rot_about(P, c, R):
    return (P - c) @ R.T + c


def pca_axis(V, toward):
    c = V.mean(0); a = np.linalg.svd(V - c, full_matrices=False)[2][0]
    return a if a.dot(toward) > 0 else -a


def joint(A, B):
    """Центр сустава между костью A (проксимальной) и B (дистальной): середина между концами костей."""
    cA, cB = A.mean(0), B.mean(0)
    aA, aB = pca_axis(A, cB - cA), pca_axis(B, cB - cA)
    pa, pb = (A - cA) @ aA, (B - cB) @ aB
    eA = A[pa > pa.max() - .2 * np.ptp(pa)].mean(0)
    eB = B[pb < pb.min() + .2 * np.ptp(pb)].mean(0)
    return (eA + eB) / 2


def dist_axis(P, B, b):
    d = P - B; return np.linalg.norm(d - (d @ b)[..., None] * b, axis=-1)


def nelder_mead(f, x0, step=.2, it=3000, tol=1e-10):
    n = len(x0); S = [np.array(x0, float)] + [np.array(x0, float) + step * np.eye(n)[i] for i in range(n)]
    F = [f(x) for x in S]
    for _ in range(it):
        o = np.argsort(F); S = [S[i] for i in o]; F = [F[i] for i in o]
        if abs(F[-1] - F[0]) < tol: break
        c = np.mean(S[:-1], 0); xr = c + (c - S[-1]); fr = f(xr)
        if fr < F[0]:
            xe = c + 2 * (c - S[-1]); fe = f(xe)
            S[-1], F[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < F[-2]: S[-1], F[-1] = xr, fr
        else:
            xc = c + .5 * (S[-1] - c); fc = f(xc)
            if fc < F[-1]: S[-1], F[-1] = xc, fc
            else:
                S = [S[0]] + [S[0] + .5 * (s - S[0]) for s in S[1:]]; F = [F[0]] + [f(s) for s in S[1:]]
    return S[int(np.argmin(F))]


def grip_hand(mesh, mc3_tip, grip_frac, k, r_bar=.0155, palm=.011, gap=.0085, log=print):
    """mesh(name) -> (V, F) в системе кисти модели (начало — лучезапястный сустав, ×0,85).
    k — во сколько раз кисть увеличится в приложении: расстояния до грифа делятся на k.
    Возвращает словарь name -> (V, F) после сгибания пальцев и разгибания запястья так, что ось грифа
    проходит через центр хвата приложения (grip_frac пути от запястья к III пястно-фаланговому суставу)."""
    B = {}
    for n in CARPALS: B[n] = mesh(n)
    for i in range(1, 6): B['metacarpal%d' % i] = mesh('metacarpal%d' % i)
    for f, _ in FINGERS:
        for p in ('proximal', 'medial', 'distal'): B[f + '_' + p] = mesh(f + '_' + p)
    for p in ('proximal', 'distal'): B['thumb_' + p] = mesh('thumb_' + p)
    V = {n: v[0].copy() for n, v in B.items()}
    G = grip_frac * mc3_tip; D = np.linalg.norm(G); u = G / D
    X = np.array([1., 0, 0]); nrm = X - X.dot(u) * u; nrm /= np.linalg.norm(nrm)       # к ладони
    b = np.cross(nrm, u); b /= np.linalg.norm(b)                                       # ось грифа
    R_f = (r_bar + gap) / k                                                            # центр фаланги от оси грифа
    # гриф: ладонная поверхность пястных костей + мягкие ткани ладони + радиус грифа; |Bc| = D
    MC = np.vstack([V['metacarpal%d' % i] for i in (2, 3, 4, 5)])
    Dp = D
    for _ in range(20):
        near = MC[np.abs(MC @ u - Dp) < .008]
        d = (near @ nrm).max() + (palm + r_bar) / k
        Dp = np.sqrt(max(D * D - d * d, 1e-6))
    Bc = Dp * u + d * nrm
    log('гриф: %.1f см от запястья вдоль кисти, %.1f см к ладони; разгибание запястья %.0f°' % (Dp * 100 * k, d * 100 * k, np.degrees(np.arctan2(d, Dp))))
    # пальцы: каждый сустав сгибается до касания фалангой грифа
    LIM = (95, 105, 80)
    flex = {}
    for f, mi in FINGERS:
        chain = ['metacarpal%d' % mi, f + '_proximal', f + '_medial', f + '_distal']
        # в хвате пальцы лежат поперёк грифа: приведение в пястно-фаланговом суставе вокруг нормали ладони
        c = joint(V[chain[0]], V[chain[1]]); p = V[chain[3]].mean(0) - c; p -= p.dot(nrm) * nrm
        Ra = rodrigues(nrm, -np.arctan2(p.dot(b), p.dot(np.cross(b, nrm))))
        for n in chain[1:]: V[n] = rot_about(V[n], c, Ra)
        ang = []
        for j in range(1, 4):
            c = joint(V[chain[j - 1]], V[chain[j]])
            # направление сгибания: к ладони — фаланга поворачивается в сторону +nrm
            def turn(th, j=j, c=c):
                Rm = rodrigues(b, np.radians(th)); return rot_about(V[chain[j]].mean(0)[None], c, Rm)[0]
            if j == 1: s = 1 if turn(5).dot(nrm) > turn(0).dot(nrm) else -1
            th_hit = LIM[j - 1]
            prev = dist_axis(turn(0), Bc, b) - R_f
            for th in np.arange(0, LIM[j - 1] + .5, .5):
                cur = dist_axis(turn(s * th), Bc, b) - R_f
                if cur <= 0:
                    th_hit = th - .5 * cur / (cur - prev) if th > 0 and cur != prev else th; break
                prev = cur
            Rm = rodrigues(b, np.radians(s * th_hit))
            for n in chain[j:]: V[n] = rot_about(V[n], c, Rm)
            ang.append(th_hit)
        flex[f] = ang
    log('сгибание MCP/PIP/DIP: ' + ', '.join('%s %.0f/%.0f/%.0f' % (f, *a) for f, a in flex.items()))
    # большой палец: поворот в запястно-пястном суставе (3 угла) и сгибание MCP, IP — оптимизацией
    T0 = {n: V[n].copy() for n in ('metacarpal1', 'thumb_proximal', 'thumb_distal')}
    near_tr = V['trapezium'][np.argmin(np.linalg.norm(V['trapezium'] - T0['metacarpal1'].mean(0), axis=1))]
    pb = T0['metacarpal1']; aB = pca_axis(pb, T0['thumb_proximal'].mean(0) - pb.mean(0)); pr = (pb - pb.mean(0)) @ aB
    cmc = (pb[pr < pr.min() + .2 * np.ptp(pr)].mean(0) + near_tr) / 2
    mcp = joint(T0['metacarpal1'], T0['thumb_proximal']); ip = joint(T0['thumb_proximal'], T0['thumb_distal'])
    tax = T0['thumb_distal'].mean(0) - mcp; tax /= np.linalg.norm(tax)
    tgt_dir = V['index_medial'].mean(0) - T0['thumb_proximal'].mean(0); fl_ax = np.cross(tax, tgt_dir); fl_ax /= np.linalg.norm(fl_ax)
    fingers = np.vstack([V[f + '_' + p] for f, _ in FINGERS for p in ('proximal', 'medial', 'distal')] + [V['metacarpal%d' % i] for i in (2, 3)])
    fsub = fingers[::4]
    im = V['index_medial'].mean(0) - Bc; im -= im.dot(b) * b; im /= np.linalg.norm(im)
    target = Bc + (R_f + .011 / k) * im + b * ((V['index_medial'].mean(0) - Bc).dot(b))

    def place(x):
        Rc = rodrigues(x[:3], np.linalg.norm(x[:3])) if np.linalg.norm(x[:3]) > 1e-9 else np.eye(3)
        out = {n: rot_about(T0[n], cmc, Rc) for n in T0}
        m2, i2, ax = rot_about(mcp[None], cmc, Rc)[0], rot_about(ip[None], cmc, Rc)[0], Rc @ fl_ax
        R2 = rodrigues(ax, x[3]); out['thumb_proximal'] = rot_about(out['thumb_proximal'], m2, R2); out['thumb_distal'] = rot_about(out['thumb_distal'], m2, R2)
        i2 = rot_about(i2[None], m2, R2)[0]
        out['thumb_distal'] = rot_about(out['thumb_distal'], i2, rodrigues(R2 @ ax, x[4]))
        return out

    def cost(x):
        o = place(x); c = 0
        for n in ('thumb_proximal', 'thumb_distal'):
            c += 4 * (dist_axis(o[n].mean(0), Bc, b) - R_f) ** 2
        allp = np.vstack([o[n][::3] for n in o])
        pen = np.minimum(dist_axis(allp, Bc, b) - (r_bar + .002) / k, 0); c += 50 * (pen ** 2).sum()
        dd = np.linalg.norm(allp[:, None, :] - fsub[None], axis=2).min(1); c += 20 * (np.minimum(dd - .004, 0) ** 2).sum()
        c += np.sum((o['thumb_distal'].mean(0) - target) ** 2)
        c += 2e-4 * np.dot(x[:3], x[:3]) + 1e-4 * (max(abs(x[3]) - 1.2, 0) ** 2 + max(abs(x[4]) - 1.4, 0) ** 2)
        return c
    best = None
    for x0 in ([0, 0, 0, .3, .3], [.5, 0, 0, .5, .5], [0, .5, 0, .5, .5], [0, 0, .5, .5, .5], [-.5, 0, 0, .5, .5], [0, -.5, 0, .5, .5], [0, 0, -.5, .5, .5]):
        x = nelder_mead(cost, x0, it=4000)
        if best is None or cost(x) < cost(best): best = x
    o = place(best); V.update(o)
    log('большой палец: поворот у основания %.0f°, MCP %.0f°, IP %.0f°, кончик от цели %.1f мм, стоимость %.2e' % (
        np.degrees(np.linalg.norm(best[:3])), np.degrees(best[3]), np.degrees(best[4]), 1000 * k * np.linalg.norm(o['thumb_distal'].mean(0) - target), cost(best)))
    # головка III пястной: куда идут сухожилия сгибателей (ладонь) и разгибателя пальцев (тыл)
    m3 = V['metacarpal3']; h3 = m3[m3 @ u > (m3 @ u).max() - .008]
    lm = dict(mc3_palmar=h3[np.argmax(h3 @ nrm)], mc3_dorsal=h3[np.argmin(h3 @ nrm)])
    # запястье: поворот вокруг оси, параллельной грифу, через сустав, чтобы ось грифа прошла через центр хвата
    ax = np.cross(Bc, G); ang = np.arccos(np.clip(Bc.dot(G) / (np.linalg.norm(Bc) * D), -1, 1))
    Rw = rodrigues(ax, ang)
    out = {n: (V[n] @ Rw.T, B[n][1]) for n in V}
    return out, dict(bar=(Rw @ Bc), b=Rw @ b, R=R_f, Rw=Rw, wrist_deg=np.degrees(ang), **{n: Rw @ p for n, p in lm.items()})


def main():
    osim = ET.parse(fetch('Models/Rajagopal/RajagopalLaiUhlrich2023.osim')).getroot()
    J = {}
    for j in osim.find('.//JointSet/objects'):
        fr = {f.get('name'): (np.array(f.findtext('translation').split(), float), np.array(f.findtext('orientation').split(), float))
              for f in j.iter('PhysicalOffsetFrame')}
        J[j.get('name')] = (fr[j.findtext('socket_parent_frame')], fr[j.findtext('socket_child_frame')])
    T = lambda name: J[name][0][0]          # положение сустава в родительском теле

    def mesh(name, scale=1.0, subdiv=0):
        V, F = read_vtp(fetch('Geometry/' + name))
        V, F = weld(V * scale, F)
        for _ in range(subdiv):
            V, F = loop_subdivide(V, F)
        return V, F

    parts = []
    def add(name, seg, V, F, side=True, extra=None):
        parts.append(dict(name=name, seg=seg, side=side, V=V, F=F, **(extra or {})))

    X = np.array([1.0, 0, 0])
    # --- таз и корпус: ось от середины тазобедренных к середине плечевых суставов
    hipR = T('hip_r'); hipMid = hipR * [1, 1, 0]
    back = T('back'); shMid = back + T('acromial_r') * [1, 1, 0]
    axT, antT, latT, LT = frame_axes(hipMid, shMid, X)          # LT = 0,533 м
    print('корпус модели %.3f м, наклон оси %.1f°' % (LT, np.degrees(np.arctan2(-axT[0], axT[1]))))
    kT = MREF['trunk'] / LT
    V, F = mesh('r_pelvis.vtp', subdiv=2)
    Vs = to_seg(V, hipR, axT, antT, latT, K_LEG, K_LEG)
    # Тазобедренные суставы приложения шире модели (±0,09 м против ±0,0773 × 1,059 м), поэтому половины таза, поставленные
    # от своих суставов, расходятся с крестцом и в лобковом симфизе почти на 1 см. Медиальную часть (крестцово-подвздошное
    # сочленение, лобковые и седалищные ветви) сдвигаем к середине; вертлужная впадина и крыло снаружи остаются на месте.
    g = HW / 2 - (-Vs[:, 2].min()) - .0015                   # у симфиза остаётся 3 мм хряща
    w = np.clip((-Vs[:, 2] - .012) / .02, 0, 1); Vs[:, 2] -= g * w * w * (3 - 2 * w)
    print('таз: медиальная часть сдвинута к середине на %.1f мм' % (g * 1000))
    add('pelvis', 'hipj', Vs, F)
    V, F = mesh('sacrum.vtp', subdiv=1)
    add('sacrum', 'pelvis', to_seg(V, hipMid, axT, antT, latT, K_LEG, K_LEG), F, side=False)
    # лопатка и ключица: центр плечевого сустава модели (0,163 м от середины после × 0,958) — на плечо приложения (ширина
    # плеч / 2), как у точек мышц плечевого пояса (anatomy/arms: поперечный масштаб по ширине плеч); грудино-ключичный сустав почти на месте
    ac = to_seg((back + T('acromial_r'))[None], hipMid, axT, antT, latT, kT, K_TRUNK)[0]
    k_sh = SW / 2 / ac[2]
    print('лопатка и ключица: вбок × %.3f, чтобы плечевой сустав модели совпал с плечом приложения' % k_sh)
    for nm in ('hat_spine.vtp', 'hat_ribs_scap.vtp'):
        V, F = mesh(nm)
        for Vc, Fc in components(V, F):
            Vs = to_seg(Vc + back, hipMid, axT, antT, latT, kT, K_TRUNK)
            zc = Vc[:, 2].mean(); big = len(Vc)
            if nm == 'hat_ribs_scap.vtp' and abs(zc) > .05 and big in (798, 264):
                if zc < 0: continue                                 # левая — зеркало правой
                Vs[:, 2] = np.abs(Vs[:, 2]) * k_sh
                add('scapula' if big == 798 else 'clavicle', 'trunk', Vs, Fc)
            else:
                add('spine' if nm == 'hat_spine.vtp' else 'ribs', 'spine', Vs, Fc, side=False)
    # --- бедро
    knee = T('walker_knee_r')
    ax, ant, lat, L = frame_axes(np.zeros(3), knee, X)
    print('бедро %.4f м' % L)
    V, F = mesh('r_femur.vtp', subdiv=2)
    add('femur', 'thigh', to_seg(V, np.zeros(3), ax, ant, lat, MREF['thigh'] / L, K_LEG), F)
    # надколенник: своя система (тело patella модели), положение по углу колена считает приложение
    pf = T('patellofemoral_r')
    V, F = mesh('r_patella.vtp', subdiv=1)
    patella = dict(V=V, F=F, femur=dict(ax=ax.tolist(), ant=ant.tolist(), lat=lat.tolist(), k_ax=MREF['thigh'] / L, k_tr=K_LEG, p0=pf.tolist()))
    # --- голень
    k0 = J['walker_knee_r'][1][0]; ank = T('ankle_r')
    ax, ant, lat, L = frame_axes(k0, ank, X)
    print('голень %.4f м' % L)
    for nm, sd in (('r_tibia.vtp', 2), ('r_fibula.vtp', 1)):
        V, F = mesh(nm, subdiv=sd)
        add(nm[2:-4], 'shank', to_seg(V, k0, ax, ant, lat, MREF['shank'] / L, K_LEG), F)
    # --- стопа: от голеностопа, изотропно × 1,06; t·0,261 = 0,23·0,261 + dx
    sub = T('subtalar_r'); mtp = T('mtp_r')
    foot = []
    V, F = mesh('r_talus.vtp', subdiv=1); foot.append(('talus', V, F))
    V, F = mesh('r_foot.vtp'); foot.append(('calcn', V + sub, F))
    V, F = mesh('r_bofoot.vtp'); foot.append(('toes', V + sub + mtp, F))
    for nm, V, F in foot:
        d = V * 1.06
        add(nm, 'foot', np.c_[.23 * MREF['foot'] + d[:, 0], d[:, 1], d[:, 2]], F, extra=dict(ankle=1))
    # --- плечо
    el = T('elbow_r')
    ax, ant, lat, L = frame_axes(np.zeros(3), el, X)
    k = MREF['ua'] / L
    print('плечо %.4f м, × %.3f' % (L, k))
    V, F = mesh('humerus_rv.vtp', subdiv=1)
    add('humerus', 'ua', to_seg(V, np.zeros(3), ax, ant, lat, k, k), F)
    # --- предплечье: локтевая и лучевая в пронации, центр хвата
    ru_t, ru_o = J['radioulnar_r'][0]
    Rj = rot_xyz(ru_o)
    # пронированный хват данных рук (anatomy/arms): ладонь в сторону a < 0; при 180° от супинации модели
    # локтевая и лучевая совпадают с точками квадратного пронатора и плечелучевой мышцы
    q = np.radians(float(os.environ.get('PROSUP', '180')))
    c, s = np.cos(q), np.sin(q); Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    rad2ulna = lambda P: (Rj @ Rz @ Rj.T @ P.T).T + ru_t
    wr = rad2ulna(T('radius_hand_r')[None])[0]
    Vm, _ = read_vtp(fetch('Geometry/metacarpal3_rvs.vtp'))
    mc = rad2ulna((Vm[Vm[:, 1].argmin()] * .85 + T('radius_hand_r'))[None])[0]   # кисть повёрнута вместе с лучевой
    grip = wr + GRIP_FRAC * (mc - wr)
    ax, ant, lat, L = frame_axes(np.zeros(3), grip, X)
    k = MREF['fa'] / L
    print('предплечье до центра хвата %.4f м, × %.3f' % (L, k))
    V, F = mesh('ulna_rv.vtp', subdiv=1)
    add('ulna', 'fa', to_seg(V, np.zeros(3), ax, ant, lat, k, k), F)
    V, F = mesh('radius_rv.vtp', subdiv=1)
    add('radius', 'fa', to_seg(rad2ulna(V), np.zeros(3), ax, ant, lat, k, k), F)
    # --- кисть: 27 костей, пальцы обхватывают гриф, ось грифа проходит через центр хвата
    bones, info = grip_hand(lambda n: mesh(n + '_rvs.vtp', scale=.85), Vm[Vm[:, 1].argmin()] * .85, GRIP_FRAC, k)
    for nm, (V, F) in bones.items():
        add('hand', 'fa', to_seg(rad2ulna(V + T('radius_hand_r')), np.zeros(3), ax, ant, lat, k, k), F)
    seg = lambda P: to_seg(rad2ulna(np.atleast_2d(P) + T('radius_hand_r')), np.zeros(3), ax, ant, lat, k, k)
    bar = seg(info['bar'])[0]
    print('ось грифа в системе предплечья: t = %.3f, a = %.4f, l = %.4f (должно быть 1, 0, 0)' % (bar[0] / MREF['fa'], bar[1], bar[2]))
    # Точки мышц на кисти (данные рук заданы при прямом запястье) поворачиваются вместе с кистью: tools/build_muscles.py.
    # В системе сегмента (вдоль оси — метры эталона, поперёк — a, l): p' = wrist + R (p − wrist)
    Bm = np.array([ax, ant, lat]); Rr = Rj @ Rz @ Rj.T
    grip = dict(note='Разгибание запястья в хвате: tools/build_skeleton.py. Система предплечья: [t·%.3f м, a, l]' % MREF['fa'],
                wrist_deg=round(float(info['wrist_deg']), 1), wrist=seg(np.zeros(3))[0].round(5).tolist(),
                R=(Bm @ Rr @ info['Rw'] @ Rr.T @ Bm.T).round(5).tolist(),
                mc3_palmar=seg(info['mc3_palmar'])[0].round(5).tolist(), mc3_dorsal=seg(info['mc3_dorsal'])[0].round(5).tolist())
    with open(os.path.join(ROOT, 'anatomy', 'hand_grip.json'), 'w') as f:
        json.dump(grip, f, ensure_ascii=False, indent=1)

    # части одной кости (позвонки, рёбра) — одна сетка
    merged = {}
    for p in parts:
        key = (p['name'], p['seg'])
        if key in merged:
            m = merged[key]; m['F'] = np.vstack([m['F'], p['F'] + len(m['V'])]); m['V'] = np.vstack([m['V'], p['V']])
        else:
            merged[key] = dict(p)
    # --- запись: заголовок JSON + вершины int16 (в пределах рамки части) + индексы uint16/uint32
    allp = list(merged.values()) + [dict(name='patella', seg='patella', side=True, **{k2: patella[k2] for k2 in ('V', 'F')}, femur=patella['femur'])]
    head, blobs, off = [], [], 0
    for p in allp:
        V, F = np.asarray(p['V'], float), np.asarray(p['F'], np.int64)
        lo, hi = V.min(0), V.max(0); sc = np.where(hi > lo, hi - lo, 1)
        q16 = np.round((V - lo) / sc * 65535 - 32768).astype('<i2').tobytes()
        idx = F.astype('<u2' if len(V) < 65536 else '<u4').tobytes()
        h = dict(name=p['name'], seg=p['seg'], side=p['side'], nv=len(V), nf=len(F), lo=lo.round(6).tolist(), hi=hi.round(6).tolist(),
                 v=off, f=off + len(q16), i32=len(V) >= 65536)
        for k2 in ('ankle', 'femur'):
            if k2 in p: h[k2] = p[k2]
        off += len(q16) + len(idx); off += (-off) % 4
        blobs.append(q16 + idx + b'\0' * ((-(len(q16) + len(idx))) % 4))
        head.append(h)
        print('%-9s %-7s %6d вершин %6d треугольников' % (p['name'], p['seg'], len(V), len(F)))
    meta = dict(src='opensim-models: Models/Rajagopal/RajagopalLaiUhlrich2023.osim, Geometry/*.vtp', parts=head,
                patellaSpline=patella_spline(osim))
    hj = json.dumps(meta, ensure_ascii=False, separators=(',', ':')).encode()
    hj += b' ' * ((-len(hj)) % 4)
    out = os.path.join(ROOT, 'assets', 'skeleton.bin')
    with open(out, 'wb') as f:
        f.write(struct.pack('<I', len(hj))); f.write(hj); f.write(b''.join(blobs))
    print('%s: %.0f КБ' % (out, os.path.getsize(out) / 1024))


def patella_spline(osim):
    """Положение надколенника в системе бедра модели от угла колена (рад): x, y сдвиги и поворот вокруг z."""
    j = next(j for j in osim.iter('CustomJoint') if j.get('name') == 'patellofemoral_r')
    out = {}
    for ta in j.iter('TransformAxis'):
        sp = ta.find('SimmSpline')
        if sp is not None:
            out[ta.get('name')] = [list(map(float, sp.findtext('x').split())), list(map(float, sp.findtext('y').split()))]
    return out


if __name__ == '__main__':
    main()
