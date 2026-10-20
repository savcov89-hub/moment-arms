// node wrap_reference.test.mjs — сверка JS-реализации обходов с Python (длины путей на 28 позах)
import {musclePath} from './wrap_reference.js';
import fs from 'fs';
const cases=JSON.parse(fs.readFileSync(new URL('./wrap_fixture.json',import.meta.url)));
let worst=0;
for(const c of cases){ const L=musclePath(c.W,c.wraps).length; worst=Math.max(worst,Math.abs(L-c.length)); }
console.log(`cases ${cases.length}, max |ΔL| = ${worst.toExponential(2)} m`);
if(worst>1e-9) process.exit(1);
