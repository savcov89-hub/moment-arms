#!/usr/bin/env python3
"""Собирает assets/muscles.js из anatomy/<регион>/muscles.json (формат anatomy/SCHEMA.md).

Запуск из корня репозитория:  python3 tools/build_muscles.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'muscles.js'

# Удельное напряжение (Н/см²) для Fmax = PCSA × σ и альтернативные пути, выбранные при интеграции.
REGIONS = {
    # README корпуса: с 46 Н/см² максимум разгибания 127 Н·м против 236–241 у мужчин; 100 даёт 276 (Favier 2021, Bruno 2015)
    'trunk': {'sigma': 100, 'alt_path': {'rectus_abdominis': 'alt_path_ct'}},
    # README рук: PCSA = Fmax MoBL-ARMS / 50,8 Н/см² (Saul 2015). Поправка групп к измеренной силе (README, «Сила мышц в сумме»):
    # сгибатели локтя × 0,6, разгибатели × 1,3, отводящие плеча × 1,6, приводящие × 0,8
    'arms': {'sigma': 50.8, 'strength': {
        **dict.fromkeys(['biceps_long', 'biceps_short', 'brachialis', 'brachioradialis', 'pronator_teres'], .6),
        **dict.fromkeys(['triceps_long', 'triceps_lateral', 'triceps_medial', 'anconeus'], 1.3),
        **dict.fromkeys(['deltoid_middle', 'supraspinatus'], 1.6),
        **dict.fromkeys(['lat_dorsi_thoracic', 'lat_dorsi_lumbar', 'lat_dorsi_iliac', 'teres_major', 'pec_major_sternal', 'pec_major_abdominal'], .8)},
        # плечелучевая: путь по точкам прикрепления MoBL (extra.path_anatomical без точек огибания), а не подогнанная прямая
        # начало → шиловидный отросток. Промежуточная точка на лучевой кости (t 0,45) при повороте предплечья уходит назад,
        # поэтому путь даёт и пронацию, и нейтраль, и супинацию: rms 0,19 / 0,17 / 0,66 см против 0,68 / 0,55 / 1,45 у прямой
        'site_path': ['brachioradialis'],
        # длинная головка трицепса: подогнанная точка на плечевой кости (2 см выше центра сустава, 8 см сзади) заменяет огибание
        # головки, когда рука поднята, а при опущенной руке путь идёт спереди от центра, и мышца сгибает плечо (+2,3 см при 0°
        # против разгибания 1,95–4 см). До 20° подъёма вместо неё — точка прикрепления MoBL на t 0,39 (extra.path_anatomical),
        # к 45° плавно переходит в подогнанную: (точка пути, номер точки прикрепления, e0, e1). Переход кончается до 45°,
        # чтобы не менять жим лёжа (там 41–87°); с переходом 45→90° сагиттальная rms чуть лучше (0,89 против 0,92 см)
        'low_point': {'triceps_long': (1, 2, 20, 45)}},
    # README ног: PCSA = Fmax Rajagopal 2016 / 60 Н/см² (объёмы по МРТ); под рост и массу — регрессия объёма Handsfield 2014
    # подвздошная и поясничная после 110–115° сгибания бедра выходят за проверенный диапазон модели и меняют знак плеча (README ног):
    # в тазобедренном суставе считаем их только сгибателями
    'legs': {'sigma': 60, 'hip_flex_only': ['iliopsoas_iliacus', 'iliopsoas_psoas']},
}

# Точки корпуса: таз отдельно (ниже L5–S1), лопатка и ключица — с шириной плеч, позвонки и рёбра — с длиной корпуса
SPINE_BODIES = {'L1', 'L2', 'L3', 'L4', 'L5', 'thorax', 'abdominal_wall'}
# флаги точки (5-й элемент): 1 — сдвиг с массой тела (живот), 2 — поперечные смещения × рост/1,80 (у локтя и головки плеча, Murray 2002),
# 4 — точка стопы считается от высоты голеностопа: a − 0,072 (эталонная высота) × длина стопы, плюс высота голеностопа приложения (README ног)
# 8, 16 — точка предплечья на лучевой кости или на кисти: на картинке поворачивается вместе с ними по рукояти (index.html, gripTwist)
F_MASS, F_HEIGHT, F_ANKLE, F_RADIUS, F_HAND = 1, 2, 4, 8, 16
ANKLE_H = .072


def body_of(p):
    return p.get('body') or p.get('bone')


def seg_of(p):
    seg, body = p['seg'], body_of(p)
    # точки таза из данных ног: от центра своего тазобедренного сустава (l = hw/2 + lh), масштаб — ширина таза
    if seg == 'trunk' and 'lh' in p:
        return 'hipj'
    if seg == 'trunk':
        if body == 'pelvis':
            return 'pelvis'
        if body in SPINE_BODIES:
            return 'spine'
    return seg


def scaling(m):
    sc = m.get('scaling')
    return sc if isinstance(sc, dict) else {}   # у ног scaling — текстовое правило, оно реализовано в приложении


def flags_of(p, m):
    sc, f = scaling(m), 0
    if body_of(p) in SPINE_BODIES and (sc.get('mass_shift_m_per_kg') or {}):
        f |= F_MASS
    if 'elbow_points' in sc and ((p['seg'] == 'ua' and p['t'] > .85) or (p['seg'] == 'fa' and p['t'] < .15)):
        f |= F_HEIGHT
    if 'humeral_head' in sc and p['seg'] == 'ua' and p['t'] < .1:
        f |= F_HEIGHT
    if p['seg'] == 'foot':
        f |= F_ANKLE
    if p['seg'] == 'fa' and body_of(p) in ('radius', 'hand'):
        f |= F_RADIUS if body_of(p) == 'radius' else F_HAND
    return f


def r4(x):
    return round(float(x), 4)


# Кисть в приложении держит гриф: запястье разогнуто, пальцы согнуты (tools/build_skeleton.py, anatomy/hand_grip.json).
# Точки на кисти из данных рук (прямое запястье) поворачиваются вместе с ней; сухожилия пальцев заканчиваются у головки
# III пястной кости: сгибатели с ладони, разгибатель с тыла, а не торчат прямо на 10 см дальше.
# На расчёт не влияет: эти мышцы пересекают лучезапястный сустав и в распределение момента не входят.
FA_REF = .19 * 1.8
HAND_TENDON = {'flex_digitorum_superficialis': 'mc3_palmar', 'flex_digitorum_profundus': 'mc3_palmar', 'ext_digitorum': 'mc3_dorsal'}
HAND_T = 1.08          # если anatomy/hand_grip.json нет: обрезать по кисти
GRIP = ROOT / 'anatomy' / 'hand_grip.json'
GRIP = json.loads(GRIP.read_text()) if GRIP.exists() else None


def hand_point(p, m):
    if GRIP is None:
        return min(p['t'], HAND_T), p['a'], p['l']
    if m['id'] in HAND_TENDON:
        x, a, l = GRIP[HAND_TENDON[m['id']]]
    else:
        w, R = GRIP['wrist'], GRIP['R']
        d = [p['t'] * FA_REF - w[0], p['a'] - w[1], p['l'] - w[2]]
        x, a, l = (w[i] + sum(R[i][j] * d[j] for j in range(3)) for i in range(3))
    return x / FA_REF, a, l


def point(p, m):
    f = flags_of(p, m)
    a = p['a'] - ANKLE_H if f & F_ANKLE else p['a']
    t, l = p['t'], p['lh'] if 'lh' in p else p['l']
    if p['seg'] == 'fa' and body_of(p) == 'hand':
        t, a, l = hand_point(p, m)
    return [seg_of(p), r4(t), r4(a), r4(l)] + ([f] if f else [])


def convert(m, region, cfg):
    path = m['path']
    alt = cfg.get('alt_path', {}).get(m['id'])
    if alt:
        path = m['extra'][alt]['path']
    if m['id'] in cfg.get('site_path', ()):
        path = [p for p in m['extra']['path_anatomical'] if p.get('kind') == 'site']
    extra = m.get('extra') or {}
    shift = scaling(m).get('mass_shift_m_per_kg') or {}
    pts = [point(p, m) for p in path]
    arms = {}
    for a in m.get('actions', []):
        if a.get('extra_motion') or a.get('arm_source') == 'effective_rhythm':
            continue
        # плечо, которое должен дать путь (у рук — arm_cm_path рядом с arm, у ног — path_arm_cm внутри arm)
        pa = a.get('arm_cm_path') or a['arm'].get('path_arm_cm')
        arms[a['motion']] = [a['arm']['angle_deg'], a['arm']['arm_cm']] + ([pa, a.get('angle_kind')] if pa else [])
    k = cfg.get('strength', {}).get(m['id'], 1)
    out = {
        'id': m['id'], 'r': region, 'name': m['name_ru'], 'group': m['group_ru'],
        'path': pts, 'belly': m.get('belly') or [0, 1],
        'w': m.get('width_m') or .03, 'th': m.get('thickness_m') or .02,
        'pcsa': round(m['pcsa_cm2'] * k, 2), 'lf': m.get('opt_fiber_cm'), 'pen': m.get('pennation_deg'),
        'sig': cfg['sigma'], 'arms': arms,
    }
    if k != 1:
        out['k'] = k
    lo = cfg.get('low_point', {}).get(m['id'])
    if lo:
        i, k, e0, e1 = lo
        site = [p for p in extra['path_anatomical'] if p.get('kind') == 'site'][k]
        q = point(site, m)
        assert q[0] == pts[i][0] and q[4:] == pts[i][4:], 'у точки при опущенной руке тот же сегмент и флаги'
        out['lo'] = [i] + q[1:4] + [e0, e1]
    if m['id'] in cfg.get('hip_flex_only', ()):
        out['hf'] = 1
    # обходы костей: [после точки, 'c' цилиндр / 's' сфера, центр как точка пути, радиус, сторона обхода]
    if m.get('wrap'):
        out['wp'] = [[w['after'], w['type'][0]] + point(w, m)[:4] + [r4(w['r']), w.get('hand', 0)] for w in m['wrap']]
    vr = m.get('volume_regression')
    if vr:
        out['vr'] = [vr['b1_cm3_per_kg_m'], vr['b2_cm3']]
    if alt:
        out['alt'] = alt
    if shift.get('a') or shift.get('l'):
        out['ms'] = [shift.get('a') or 0, shift.get('l') or 0]
    if any(body_of(p) == 'hand' for p in path):
        out['wr'] = 1  # переходит на кисть: пересекает лучезапястный сустав, которого в приложении нет
    # мышцы лопатки: плечевой сустав не пересекают; действуют через движение лопатки (эффективное плечо по ритму, README рук)
    if extra.get('crosses_glenohumeral') is False:
        acts = {a['motion']: a for a in m.get('actions', []) if a.get('arm_source') == 'effective_rhythm'}
        up, down = acts.get('sh_flex'), acts.get('sh_ext')
        if up or down:
            ang = (up or down)['arm']['angle_deg']
            out['rh'] = [ang, [r4(((up['arm']['arm_cm'][i] if up else 0) - (down['arm']['arm_cm'][i] if down else 0)) / 100) for i in range(len(ang))]]
        lr = extra.get('length_rel_vs_elevation')
        if lr:
            out['lrel'] = [lr['angle_deg'], lr['L_over_L0']]
    return out


def merge_psoas(muscles):
    """Большая поясничная есть в корпусе (psoas_upper, psoas_lower) и в ногах (iliopsoas_psoas) — это одна мышца.
    Путь: поясничная часть до края таза — из корпуса (плечи на L5–S1), дальше — путь ног с обходом лобковой кости
    (плечи в тазобедренном суставе). Сила: МРТ-PCSA ног (σ 60, как у остальных мышц бедра), поделённая между пучками
    как в корпусе. Fmax почти тот же: 24,8 × 60 = 1488 Н против (7,01 + 7,62) × 100 = 1463 Н."""
    by = {m['id']: m for m in muscles}
    legs, ups = by.get('iliopsoas_psoas'), [by[i] for i in ('psoas_upper', 'psoas_lower') if i in by]
    if not legs or not ups:
        return muscles
    total = sum(m['pcsa'] for m in ups)
    for m in ups:
        k = next(i for i, p in enumerate(m['path']) if p[0] == 'pelvis')   # первая точка на тазе
        m['path'] = m['path'][:k + 1] + legs['path'][1:]
        m['wp'] = [[w[0] + k] + w[1:] for w in legs['wp']]
        m['arms'] = {**m['arms'], **legs['arms']}
        m.update(r='legs', hf=legs.get('hf', 0), pcsa=round(legs['pcsa'] * m['pcsa'] / total, 2), sig=legs['sig'], vr=legs['vr'], lf=legs['lf'], pen=legs['pen'])
    return [m for m in muscles if m['id'] != 'iliopsoas_psoas']


def main():
    muscles, regions, same = [], {}, set()
    for region, cfg in REGIONS.items():
        f = ROOT / 'anatomy' / region / 'muscles.json'
        if not f.exists():
            continue
        data = json.loads(f.read_text(encoding='utf-8'))
        regions[region] = {'sigma': cfg['sigma'], 'n': len(data)}
        muscles += [convert(m, region, cfg) for m in data]
        # одна мышца в двух регионах (широчайшая): путь у плеча и PCSA берём из рук, второй экземпляр выбрасываем
        same |= {x['same_muscle_as'].split('/')[-1] for x in data if x.get('same_muscle_as')}
    muscles = merge_psoas([m for m in muscles if m['id'] not in same])
    body = json.dumps({'regions': regions, 'muscles': muscles}, ensure_ascii=False, separators=(',', ':'))
    OUT.write_text('// Сгенерировано tools/build_muscles.py из anatomy/<регион>/muscles.json — руками не править\n'
                   f'window.MUSCLE_DATA={body};\n', encoding='utf-8')
    print(f'{OUT.relative_to(ROOT)}: {len(muscles)} мышц, регионы {list(regions)}, убраны дубли {sorted(same)}')


if __name__ == '__main__':
    main()
