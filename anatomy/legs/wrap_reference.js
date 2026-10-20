// Эталонная реализация обходов (wrap) для путей мышц из muscles.json.
// Чистые функции, векторы — массивы [x,y,z]. Совпадает с Python-кодом, которым подгонялись пути
// (проверено на наборе случаев в wrap_reference.test.mjs, расхождение < 1e-9 м).
//
// Обход задаётся в мышце полем wrap: [{type, seg, t, a, l, r, after, hand}]
//   after — индекс точки пути, после которой идёт участок с обходом (между path[after] и path[after+1]);
//   type 'cyl'    — цилиндр, ось = латеральная ось сегмента seg; путь огибает окружность радиуса r
//                   в плоскости, перпендикулярной оси. hand = +1: центр остаётся слева от направления
//                   движения P→Q, −1: справа (в базисе e1 = вперёд, e2 = к проксимальному концу сегмента);
//   type 'sphere' — сфера радиуса r, путь огибает её по кратчайшей стороне (геодезическая в плоскости P, Q, C).
// Центр (C) считается из {seg,t,a,l} так же, как точки пути.

const sub=(a,b)=>[a[0]-b[0],a[1]-b[1],a[2]-b[2]];
const add=(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2]];
const mul=(a,k)=>[a[0]*k,a[1]*k,a[2]*k];
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const norm=a=>Math.sqrt(dot(a,a));
const cr2=(a,b)=>a[0]*b[1]-a[1]*b[0];
const rot2=(v,ang)=>{const c=Math.cos(ang),s=Math.sin(ang);return [c*v[0]-s*v[1],s*v[0]+c*v[1]];};
const n2=v=>Math.hypot(v[0],v[1]);

// Обход окружности (центр в начале координат) в 2D. Возвращает {L, pts}.
function wrap2d(P,Q,r,hand,npts=8){
  const d=[Q[0]-P[0],Q[1]-P[1]], Ld=n2(d);
  if(Ld<1e-12) return {L:0,pts:[P,Q]};
  const s=cr2(d,[-P[0],-P[1]])/Ld;                  // расстояние от центра до прямой (+ слева)
  const lam=(-P[0]*d[0]-P[1]*d[1])/(Ld*Ld);         // проекция центра на отрезок
  const dp=n2(P), dq=n2(Q);
  // прямо, если прямая проходит мимо окружности с разрешённой стороны или отрезок вовсе её не задевает
  if(hand*s>=r || ((lam<0||lam>1) && (hand*s>=0 || (dp>r && dq>r)))) return {L:Ld,pts:[P,Q]};
  const rr=Math.min(r,0.999*dp,0.999*dq);
  const bp=Math.acos(rr/dp), bq=Math.acos(rr/dq);
  const T1=rot2([P[0]/dp*rr,P[1]/dp*rr],hand*bp), T2=rot2([Q[0]/dq*rr,Q[1]/dq*rr],-hand*bq);
  const a1=Math.atan2(T1[1],T1[0]), a2=Math.atan2(T2[1],T2[0]);
  let dang=(hand*(a2-a1))%(2*Math.PI); if(dang<0) dang+=2*Math.PI;
  if(hand*s>=0 && dang>Math.PI) return {L:Ld,pts:[P,Q]};   // центр с разрешённой стороны: дуга < 180°, больше — переворот точек касания
  const arc=[]; for(let k=1;k<npts;k++) arc.push(rot2(T1,hand*dang*k/npts));
  return {L:n2([T1[0]-P[0],T1[1]-P[1]])+rr*dang+n2([Q[0]-T2[0],Q[1]-T2[1]]), pts:[P,T1,...arc,T2,Q]};
}

// Цилиндр: ax — латеральная ось сегмента (единичная), e1 — «вперёд» сегмента, e2 — к проксимальному концу
// (для стопы — вверх); e1, e2 ортогональны ax. Длина = sqrt(L2d² + Δ²) — геодезическая на развёртке.
export function wrapCylinder(P,Q,C,ax,e1,e2,r,hand){
  const to2=X=>{const v=sub(X,C);return [dot(v,e1),dot(v,e2)];};
  const w=wrap2d(to2(P),to2(Q),r,hand), dl=dot(sub(Q,P),ax), p0=dot(sub(P,C),ax);
  const L=Math.sqrt(w.L*w.L+dl*dl);
  const seg=[0]; for(let k=1;k<w.pts.length;k++) seg.push(seg[k-1]+n2([w.pts[k][0]-w.pts[k-1][0],w.pts[k][1]-w.pts[k-1][1]]));
  const pts=w.pts.map((p,k)=>add(add(add(C,mul(e1,p[0])),mul(e2,p[1])),mul(ax,p0+(seg[seg.length-1]>0?seg[k]/seg[seg.length-1]:1)*dl)));
  return {length:L, points:pts};
}

// Сфера: огибание по кратчайшей стороне.
export function wrapSphere(P,Q,C,r){
  const d=sub(Q,P), Ld=norm(d);
  let lam=dot(sub(C,P),d)/(Ld*Ld); lam=Math.max(0,Math.min(1,lam));
  const X=add(P,mul(d,lam));
  if(norm(sub(X,C))>=r) return {length:Ld, points:[P,Q]};
  let n=cross(sub(P,C),sub(Q,C)); const nn=norm(n);
  if(nn<1e-12) return {length:Ld, points:[P,Q]};
  n=mul(n,1/nn); const e1=mul(sub(P,C),1/norm(sub(P,C))), e2=cross(n,e1);
  const to2=Y=>{const v=sub(Y,C);return [dot(v,e1),dot(v,e2)];};
  const P2=to2(P), Q2=to2(Q), hand=cr2([Q2[0]-P2[0],Q2[1]-P2[1]],[-P2[0],-P2[1]])>=0?1:-1;
  const w=wrap2d(P2,Q2,r,hand);
  return {length:w.L, points:w.pts.map(p=>add(add(C,mul(e1,p[0])),mul(e2,p[1])))};
}

// Длина пути мышцы. W — мировые координаты точек path; wraps — массив обходов, в каждом уже посчитаны
// C (центр в мире), а для цилиндра — ax, e1, e2 (оси сегмента seg в мире).
export function musclePath(W,wraps=[]){
  const byAfter={}; for(const w of wraps) byAfter[w.after]=w;
  let L=0; const pts=[W[0]];
  for(let i=0;i<W.length-1;i++){
    const P=W[i],Q=W[i+1],w=byAfter[i];
    let res;
    if(!w) res={length:norm(sub(Q,P)),points:[P,Q]};
    else if(w.type==='sphere') res=wrapSphere(P,Q,w.C,w.r);
    else res=wrapCylinder(P,Q,w.C,w.ax,w.e1,w.e2,w.r,w.hand);
    L+=res.length; pts.push(...res.points.slice(1));
  }
  return {length:L, points:pts};
}

// Плечо силы для сустава: r = −ΔL/Δθ (центральная разность, θ в радианах, ±0,25°).
// lengthAt(θ) — функция, которая ставит позу с углом θ и возвращает musclePath(...).length.
export function momentArm(lengthAt,theta,h=0.25*Math.PI/180){
  return -(lengthAt(theta+h)-lengthAt(theta-h))/(2*h);
}
