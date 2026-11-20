const VL={external:'External',internal:'Internal'},VS={external:'e',internal:'i'};
const FRONT_END=50,BAY={x0:9,x1:116,h:11.7};
let P=[],hist=[],sel=-1,selId=null,filt='all',drag=null,ghost=null,dragged=false,tm,pickView=null,shipId=null,view='external',mv=null,uid=1;
const snap=()=>JSON.stringify(P);
try{const s=JSON.parse(localStorage.getItem('libplan3')||'null');if(Array.isArray(s))P=s.filter(p=>byName(p.n))}catch(e){}
if(!P.length){try{const o=JSON.parse(localStorage.getItem('libplan2')||'null'),f=JSON.parse(localStorage.getItem('libfit')||'{}')||{};const C={front:['external',21],up1:['external',66],up2:['external',99.3],g1:['internal',40],g2:['internal',80]};
if(o)for(const k in C)if(o[k]&&byName(o[k]))P.push({id:0,n:o[k],v:C[k][0],x:C[k][1],y:0,r:0,f:f[k]&&f[k].n===o[k]?{v:f[k].v,m:f[k].m}:null})}catch(e){}}
P.forEach(p=>{p.id=uid++});
const save=()=>{try{localStorage.setItem('libplan3',JSON.stringify(P))}catch(e){}};
const byId=id=>P.find(p=>p.id===id);
function cfg(id){const p=byId(id);if(!p)return null;const d=byName(p.n),vs=variants(d);if(!vs.length)return{p,d,vs,ship:null};if(!p.f||!vs.includes(p.f.v))p.f={v:vs[0],m:{}};return{p,d,vs,f:p.f,ship:LD.ships[p.f.v]}}
const fitV=(d,v)=>d[VS[v]];
const sym=s=>({ok:'✓',unk:'?',warn:'!',no:'✕'})[cls(s)];
const badge=(s,name)=>`<span class="b ${cls(s)}" title="${esc(name+': '+(s?L[s]:NF))}">${s&&s.startsWith('front')?'Front pad':name} ${sym(s)}</span>`;
const desc=d=>`${dims(d)} · Deck: ${d.e?L[d.e]:NF} · Garage: ${d.i?L[d.i]:NF}`;
function corners(p){const d=byName(p.n),a=p.r*Math.PI/180,u=[Math.cos(a),Math.sin(a)],w=[-u[1],u[0]],l=(d.L||4)/2,b=(d.B||3)/2;return[[1,1],[1,-1],[-1,-1],[-1,1]].map(([i,j])=>[p.x+i*l*u[0]+j*b*w[0],p.y+i*l*u[1]+j*b*w[1]])}
function hit(p,q){const A=corners(p),B=corners(q);for(const C of[A,B])for(let i=0;i<2;i++){const ax=[C[i+1][0]-C[i][0],C[i+1][1]-C[i][1]];const pr=K=>K.map(c=>c[0]*ax[0]+c[1]*ax[1]);const a=pr(A),b=pr(B);if(Math.max(...a)<=Math.min(...b)+1e-6||Math.max(...b)<=Math.min(...a)+1e-6)return false}return true}
function issues(p){const d=byName(p.n),f=fitV(d,p.v),o=[];
if(!f)o.push(['bad',`${p.v==='external'?'Deck':'Garage'}: ${NF}`]);else if(lvl(f)!=='ok')o.push([cls(f),L[f]]);
if(p.v==='external'&&d.e&&d.e.startsWith('front')&&p.x>FRONT_END)o.push(['warn','F ship: fits only on the front pad']);
if(p.v==='internal'&&corners(p).some(([x,y])=>x<BAY.x0||x>BAY.x1||Math.abs(y)>BAY.h))o.push(['warn','Outside the approximate vehicle-bay outline']);
for(const q of P)if(q!==p&&q.v===p.v&&hit(p,q))o.push(['bad',`Overlaps ${q.n}`]);return o}
const worst=o=>o.some(x=>x[0]==='bad')?'bad':o.some(x=>x[0]==='warn')?'warn':o.some(x=>x[0]==='unk')?'unk':'ok';
function shown(){const q=$('#q').value.trim().toLowerCase();return D.map((d,i)=>[d,i]).filter(([d])=>(filt==='all'||(filt==='ship'&&d.k==='ship')||(filt==='ground'&&d.k==='ground')||(filt==='in'&&!!d.i)||(filt==='front'&&!!d.e&&d.e.startsWith('front')))&&(!q||(d.n+' '+d.m).toLowerCase().includes(q)))}
function renderCards(){const r=shown();$('#count').textContent=`${r.length} of ${D.length} ships and vehicles`;
$('#cards').innerHTML=r.length?r.map(([d,i])=>`<div class="card${i===sel?' on':''}" data-i="${i}" tabindex="0" role="button" aria-pressed="${i===sel}"><span class="grip" aria-hidden="true">⠿</span>${thumb(d)}<span class="nm"><b>${esc(d.n)}</b><small>${esc(d.m)}${d.k==='ground'?' · ground':''} · ${dims(d)}</small></span><span class="bs">${badge(d.e,'Deck')}${badge(d.i,'Garage')}</span></div>`).join(''):'<p class="empty">No ships match that search.</p>'}
function setView(v){view=v;for(const t of $$('[role=tab]'))t.setAttribute('aria-selected',String(t.dataset.v===v));$('#v-external').hidden=v!=='external';$('#v-internal').hidden=v!=='internal';const p=selId&&byId(selId);if(p&&p.v!==v)selId=null;try{localStorage.setItem('libview',v)}catch(e){}renderPlan()}
function drawShips(){for(const sv of $$('svg.ship')){const v=sv.dataset.v,int=v==='internal';
let h=`<image class="lib${int?' int':''}" href="${LIBIMG}" x="0" y="-33.5" width="119" height="67"/>`;
h+=int?`<rect class="bay" x="${BAY.x0}" y="${-BAY.h}" width="${BAY.x1-BAY.x0}" height="${2*BAY.h}" rx="1"/><text class="el" x="${BAY.x0+1}" y="${-BAY.h-1.2}">Vehicle bay, approximate outline (deck 02)</text>`:`<text class="el lt" x="12" y="-13">Front pad</text><text class="el lt" x="51.5" y="-13">Upper pad 1</text><text class="el lt" x="85" y="-13">Upper pad 2</text>`;
for(const p of P.filter(p=>p.v===v)){const d=byName(p.n),o=issues(p),w=worst(o),l=d.L||4,b=d.B||3,k=Math.min(1.6,b/3),n=Math.min(2.4,l/3);
h+=`<g class="pc ${w}${p.id===selId?' on':''}" data-id="${p.id}" transform="translate(${p.x} ${p.y}) rotate(${p.r-90})"><title>${esc(d.n)}</title>`+(d.td?`<image href="${d.td}" x="${-b/2}" y="${-l/2}" width="${b}" height="${l}" preserveAspectRatio="xMidYMid meet"/><rect class="fpr img" x="${-b/2}" y="${-l/2}" width="${b}" height="${l}" rx=".6"/>`:`<rect class="fpr" x="${-b/2}" y="${-l/2}" width="${b}" height="${l}" rx="${Math.min(b,l)*.15}"/><path class="nose" d="M0 ${-l/2+.6}l${k} ${n}h${-2*k}z"/>`)+'</g>'}
h+=`<path class="bar" d="M0 34h10M0 33v2M10 33v2"/><text class="el" x="11" y="35">10 m</text><text class="el" x="119" y="35" text-anchor="end">◀ bow · 119 × 67 m</text>`;
sv.innerHTML=h}}
function renderPlan(){const vp=P.filter(p=>p.v===view);
$('#placed').innerHTML=vp.length?vp.map(p=>{const d=byName(p.n),o=issues(p),c=cfg(p.id),S=c&&c.ship?stats(c):null;return `<div class="pl ${worst(o)}${p.id===selId?' on':''}" data-id="${p.id}"><button class="chg" data-id="${p.id}" aria-pressed="${p.id===selId}"><b>${esc(d.n)}</b><i>${dims(d)}${S?` · ${fmt(S.dps)} DPS · ${fmt(S.sh)} shield`:''}${nmod(c)?' · <span class="mod">modified</span>':''}</i>${o.map(([k,t])=>`<i class="is ${k}">${esc(t)}</i>`).join('')}</button><button class="ld" data-id="${p.id}">Stats</button><button class="rm" data-id="${p.id}" aria-label="Remove ${esc(d.n)}">✕</button></div>`}).join(''):`<p class="empty">No ships ${view==='external'?'on the deck':'in the bay'} yet. Use + Add ship or drag one in from the list.</p>`;
const sp=selId&&byId(selId);$('#selbar').hidden=!sp;if(sp)$('#seln').textContent=`${sp.n} · ${Math.round(((sp.r%360)+360)%360)}°`;
for(const t of $$('[role=tab]')){const dt=t.querySelector('.dot');dt.className='dot';if(sel>=0)dt.classList.add(lvl(fitV(D[sel],t.dataset.v)))}
$('#bar').hidden=sel<0;document.body.classList.toggle('hasbar',sel>=0);
if(sel>=0){const d=D[sel];$('#bn').textContent=d.n;$('#bd').textContent=desc(d);for(const b of $$('#bar [data-v]')){const l=lvl(fitV(d,b.dataset.v));b.disabled=l==='no';b.className=l}}
drawShips();$('#undo').disabled=!hist.length;save();renderRRR();if(shipId)renderShip()}
function renderShip(){const c=cfg(shipId);if(!c){closeShip();return}
$('#sdt').textContent=`${c.d.n} · ${VL[c.p.v]}`;
if(!c.ship){$('#sb').innerHTML='<p class="empty">No game-data loadout for this entry.</p>';return}
const S=stats(c),sh=c.ship,row=(k,v)=>`<div><dt>${k}</dt><dd>${v}</dd></div>`;
let h=c.vs.length>1?`<label class="vr">Variant <select id="vsel">${c.vs.map(v=>`<option${v===c.f.v?' selected':''}>${esc(v)}</option>`).join('')}</select></label>`:`<p class="vr">${esc(c.f.v)}</p>`;
h+=`<dl class="stats">${row('Role',esc(sh.role||'—'))}${row('Crew',sh.crew[0]===sh.crew[1]?fmt(sh.crew[0]):sh.crew.join('–'))}${row('Size L × B × H',dims(c.d))}${row('Speed SCM / max',`${fmt(sh.scm)} / ${fmt(sh.vmax)} m/s`)}${row('Hull HP',fmt(sh.hull))}${row('Shield HP',fmt(S.sh))}${row('Gun DPS / alpha',`${fmt(S.dps)} / ${fmt(S.a)}`)}${row('Missiles',S.ms?`${S.ms} · ${fmt(S.md)} dmg`:'none')}${row('Power / cooling',`${fmt(S.pw)} / ${fmt(S.cl)}`)}${row('Quantum drive',S.qd?`${esc(S.qd.n)} · ${fmt(S.qd.sp/1e6)} Mm/s`:'none')}${row('Fuel: hydrogen / quantum',`${sh.fuel??'—'} / ${sh.qfuel??'—'}`)}${row('Cargo',sh.cargo?sh.cargo+' SCU':'—')}</dl>`;
const g={};sh.slots.forEach((sl,i)=>(g[sl.t]=g[sl.t]||[]).push(i));
for(const t of Object.keys(TN)){if(!g[t])continue;h+=`<h4>${TN[t]}</h4>`;
for(const i of g[t]){const sl=sh.slots[i],k=cur(c,i),it=k!=null?IT[k]:null,lbl=`${esc(pretty(sl.id))} <small>S${sl.s}${sl.n>1?' × '+sl.n:''}</small>`;
if(t==='WeaponDefensive'||sl.ed===false){h+=`<div class="lo"><span>${lbl}</span><span>${it?esc(it.n):'—'}${it&&it.am?` · ${it.am} charges`:''}</span></div>`;continue}
const op=IT.map((x,j)=>[x,j]).filter(([x])=>x.t===t&&x.s===sl.s).sort((a,b)=>a[0].n.localeCompare(b[0].n));if(k!=null&&!op.some(([,j])=>j===k))op.unshift([IT[k],k]);
h+=`<label class="lo${c.f.m[i]!==undefined?' chg':''}"><span>${lbl}</span><select data-k="${i}"><option value=""${k==null?' selected':''}>Empty</option>${op.map(([x,j])=>`<option value="${j}"${j===k?' selected':''}>${esc(x.n)}${j===sl.d?' (stock)':''}${statTxt(x)}</option>`).join('')}</select></label>`}}
h+=`<div class="tools"><button id="sreset"${nmod(c)?'':' disabled'}>Reset to stock</button></div><p class="note">Stats and parts are game data (4.10.3) via api.star-citizen.wiki. The options are parts of the same type and size. Grouped rows let you pick the variant you own.</p>`;
$('#sb').innerHTML=h}
function openShip(id){shipId=id;renderShip();const g=$('#sd');try{g.showModal()}catch(e){g.setAttribute('open','')}}
function closeShip(){const g=$('#sd');try{g.close()}catch(e){g.removeAttribute('open')}shipId=null}
$('#sx').addEventListener('click',closeShip);$('#sd').addEventListener('click',e=>{if(e.target===e.currentTarget)closeShip()});$('#sd').addEventListener('close',()=>{shipId=null});
$('#sb').addEventListener('change',e=>{const c=cfg(shipId);if(!c||!c.ship)return;const t=e.target;
if(t.id==='vsel'){c.p.f={v:t.value,m:{}}}else if(t.dataset.k!=null){const i=+t.dataset.k,v=t.value===''?null:+t.value;if(v===c.ship.slots[i].d)delete c.f.m[i];else c.f.m[i]=v}renderPlan()});
$('#sb').addEventListener('click',e=>{if(e.target.id==='sreset'){const c=cfg(shipId);if(c&&c.ship){c.f.m={};renderPlan()}}});
function rrrData(){const A={},M={},C={},H=[],none=[];let fu=0,qf=0;
for(const p of P){const c=cfg(p.id);if(!c.ship){none.push(c.d.n);continue}const S=stats(c);
for(const[k,v]of S.ammo){const a=A[k]=A[k]||{g:0,r:0,w:new Set()};a.g++;a.r+=v;a.w.add(c.d.n)}
for(const[k,v]of S.mis)M[k]=(M[k]||0)+v;for(const[k,v]of S.cm)C[k]=(C[k]||0)+v;
fu+=c.ship.fuel||0;qf+=c.ship.qfuel||0;H.push([`${c.d.n} (${VL[p.v]})`,c.ship.hull])}return{A,M,C,H,fu,qf,none}}
function renderRRR(){const R=rrrData();if(!R.H.length&&!R.none.length){$('#rrr').innerHTML='<p class="empty">Place ships to build the restock list.</p>';return}
const tb=(hd,rows)=>rows.length?`<table><thead><tr>${hd.map(x=>`<th${x.startsWith('#')?' class="n"':''}>${x.replace(/^#/,'')}</th>`).join('')}</tr></thead><tbody>${rows.join('')}</tbody></table>`:'<p class="empty">None.</p>';
const A=Object.entries(R.A).sort((a,b)=>b[1].r-a[1].r).map(([k,a])=>`<tr><td>${esc(k)}<br><small>${esc([...a.w].join(', '))}</small></td><td class="n">${a.g}</td><td class="n">${fmt(a.r)}</td></tr>`);
const M=Object.entries(R.M).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`<tr><td>${esc(k)}</td><td class="n">${v}</td></tr>`);
const C=Object.entries(R.C).map(([k,v])=>`<tr><td>${esc(k)}</td><td class="n">${fmt(v)}</td></tr>`);
const H=R.H.map(([k,v])=>`<tr><td>${esc(k)}</td><td class="n">${fmt(v)}</td></tr>`);
$('#rrr').innerHTML=`<div class="rg"><div><h3>Ballistic ammo</h3>${tb(['Weapon','#Guns','#Rounds'],A)}<p class="note">Energy weapons regenerate and need no ammo.</p></div><div><h3>Missiles</h3>${tb(['Missile','#Count'],M)}<h3>Countermeasures</h3>${tb(['Launcher','#Charges'],C)}</div><div><h3>Fuel</h3>${tb(['Tank','#Capacity'],[`<tr><td>Hydrogen, all ships</td><td class="n">${+R.fu.toFixed(2)}</td></tr>`,`<tr><td>Quantum, all ships</td><td class="n">${+R.qf.toFixed(2)}</td></tr>`])}<h3>Repair</h3>${tb(['Ship','#Hull HP'],H)}${R.none.length?`<p class="note">No loadout data: ${esc(R.none.join(', '))}.</p>`:''}</div></div>`}
$('#rcopy').addEventListener('click',async()=>{const R=rrrData();const T=['Liberator RRR restock list','Ballistic ammo:',...Object.entries(R.A).map(([k,a])=>`  ${k}: ${a.r} rounds (${a.g} guns)`),'Missiles:',...Object.entries(R.M).map(([k,v])=>`  ${k}: ${v}`),'Countermeasures:',...Object.entries(R.C).map(([k,v])=>`  ${k}: ${v}`),`Fuel: hydrogen ${+R.fu.toFixed(2)}, quantum ${+R.qf.toFixed(2)}`,'Hull HP:',...R.H.map(([k,v])=>`  ${k}: ${v}`)];try{await navigator.clipboard.writeText(T.join('\n'));flash('Restock list copied.')}catch(e){flash('Copy was blocked here.')}});
const render=()=>{renderCards();renderPlan()};
const flash=t=>{$('#msg').textContent=t;clearTimeout(tm);tm=setTimeout(()=>{$('#msg').textContent=''},4000)};
function freeSpot(v,i){const d=D[i],t={id:-1,n:d.n,v,x:0,y:0,r:0};const xs=v==='external'?(d.e&&d.e.startsWith('front')?[21,30,15]:[66,99.3,21]):[];for(let x=(v==='internal'?BAY.x0:8)+(d.L||4)/2;x<=114;x+=1)xs.push(x);
for(const y of[0,-6,6,-12,12])for(const x of xs){t.x=x;t.y=y;if(!P.some(q=>q.v===v&&hit(t,q))&&(v!=='internal'||!corners(t).some(([a,b])=>a<BAY.x0||a>BAY.x1||Math.abs(b)>BAY.h)))return[x,y]}return[v==='internal'?60:30,0]}
function add(v,i,at){const d=D[i],f=fitV(d,v);if(lvl(f)==='no'){flash(`${d.n} ${NF} ${v==='external'?'on the deck':'in the bay'}.`);return}
hist.push(snap());const[x,y]=at||freeSpot(v,i);const p={id:uid++,n:d.n,v,x:+x.toFixed(1),y:+y.toFixed(1),r:0,f:null};P.push(p);selId=p.id;if(v!==view)setView(v);flash(`${d.n} added to ${VL[v].toLowerCase()}${lvl(f)==='warn'?` (${L[f].toLowerCase()})`:''}. Drag it to arrange.`);renderPlan()}
function renderPick(){const v=pickView,q=$('#dq').value.trim().toLowerCase();
const r=D.map((d,i)=>[d,i,fitV(d,v)]).filter(([d,,f])=>f&&(!q||(d.n+' '+d.m).toLowerCase().includes(q))).sort((a,b)=>(lvl(a[2])==='ok'?0:1)-(lvl(b[2])==='ok'?0:1));
$('#dl').innerHTML=r.length?r.map(([d,i,f])=>`<button class="opt" data-i="${i}">${thumb(d)}<span style="flex:1"><b>${esc(d.n)}</b><small>${esc(d.m)} · ${dims(d)}</small></span><span class="b ${cls(f)}">${L[f]}</span></button>`).join(''):'<p class="empty">Nothing that fits here matches.</p>'}
function openPick(v){pickView=v;$('#dt').textContent=`Add to ${VL[v].toLowerCase()}`;$('#dq').value='';renderPick();const g=$('#dlg');try{g.showModal()}catch(e){g.setAttribute('open','')}$('#dq').focus()}
const closePick=()=>{const g=$('#dlg');try{g.close()}catch(e){g.removeAttribute('open')}pickView=null};
$('#dq').addEventListener('input',renderPick);$('#dx').addEventListener('click',closePick);
$('#dl').addEventListener('click',e=>{const o=e.target.closest('.opt');if(!o||!pickView)return;const v=pickView;closePick();add(v,+o.dataset.i)});
$('#dlg').addEventListener('click',e=>{if(e.target===e.currentTarget)closePick()});
$('#addbtn').addEventListener('click',()=>openPick(view));
const pick=i=>{sel=sel===i?-1:i;render()};
$('#cards').addEventListener('click',e=>{if(dragged)return;const c=e.target.closest('.card');if(c)pick(+c.dataset.i)});
$('#cards').addEventListener('keydown',e=>{const c=e.target.closest('.card');if(c&&(e.key==='Enter'||e.key===' ')){e.preventDefault();pick(+c.dataset.i)}});
$('.tabs').addEventListener('click',e=>{const t=e.target.closest('[role=tab]');if(t)setView(t.dataset.v)});
const del=id=>{hist.push(snap());P=P.filter(p=>p.id!==id);if(selId===id)selId=null;renderPlan()};
const turn=a=>{const p=byId(selId);if(!p)return;hist.push(snap());p.r=((p.r+a)%360+360)%360;renderPlan()};
$('#placed').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const id=+b.dataset.id;if(b.classList.contains('rm'))del(id);else if(b.classList.contains('ld'))openShip(id);else{selId=selId===id?null:id;renderPlan()}});
$('#selbar').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const a=b.dataset.a;if(a==='l')turn(-15);else if(a==='r')turn(15);else if(a==='q')turn(90);else if(a==='s')openShip(selId);else if(a==='x')del(selId);else if(a==='d'){selId=null;renderPlan()}});
$('#bar').addEventListener('click',e=>{const b=e.target.closest('[data-v]');if(b&&sel>=0){add(b.dataset.v,sel)}if(e.target.closest('#bx')){sel=-1;render()}});
$('#q').addEventListener('input',renderCards);
$('.chips').addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(!b)return;filt=b.dataset.f;for(const x of $$('.chips [data-f]'))x.setAttribute('aria-pressed',String(x===b));renderCards()});
$('#undo').addEventListener('click',()=>{if(hist.length){P=JSON.parse(hist.pop());if(!byId(selId))selId=null;renderPlan();flash('Undone.')}});
$('#clear').addEventListener('click',()=>{if(!P.length)return;hist.push(snap());P=[];selId=null;renderPlan();flash('Plan cleared. Undo brings it back.')});
$('#copy').addEventListener('click',async()=>{const t=['Liberator plan',...['external','internal'].flatMap(v=>[`${VL[v]}:`,...(P.filter(p=>p.v===v).map(p=>{const d=byName(p.n),c=cfg(p.id),o=issues(p).filter(x=>x[0]!=='ok').map(x=>x[1]);return `  ${d.n} (${dims(d)})${c&&c.ship?` [${c.f.v}${nmod(c)?', modified: '+Object.keys(c.f.m).map(i=>{const k=c.f.m[i];return pretty(c.ship.slots[i].id)+' → '+(k==null?'empty':IT[k].n)}).join('; '):''}]`:''}${o.length?' — '+o.join('; '):''}`}).concat(P.some(p=>p.v===v)?[]:['  —']))])].join('\n');try{await navigator.clipboard.writeText(t);flash('Plan copied.')}catch(e){flash('Copy was blocked here.')}});
const svgPt=(sv,x,y)=>new DOMPoint(x,y).matrixTransform(sv.getScreenCTM().inverse());
const typing=()=>/input|select|textarea/i.test((document.activeElement||{}).tagName||'');
document.addEventListener('keydown',e=>{if(pickView||shipId)return;if(e.key==='Escape'){if(selId){selId=null;renderPlan()}else if(sel>=0){sel=-1;render()}return}
const p=selId&&byId(selId);if(!p||typing())return;const s=e.shiftKey?2:.5,mvk={ArrowLeft:[-s,0],ArrowRight:[s,0],ArrowUp:[0,-s],ArrowDown:[0,s]}[e.key];
if(mvk){e.preventDefault();hist.push(snap());p.x=+(p.x+mvk[0]).toFixed(1);p.y=+(p.y+mvk[1]).toFixed(1);renderPlan()}else if(e.key==='r'||e.key==='R'){turn(e.key==='R'?-15:15)}else if(e.key==='Delete'||e.key==='Backspace'){e.preventDefault();del(p.id)}});
for(const sv of $$('svg.ship')){
sv.addEventListener('pointerdown',e=>{if(e.button>0)return;const g=e.target.closest('.pc');const pt=svgPt(sv,e.clientX,e.clientY);
if(g){const p=byId(+g.dataset.id);e.preventDefault();mv={p,sx:pt.x,sy:pt.y,x0:p.x,y0:p.y,moved:false,sv};selId=p.id;sv.setPointerCapture(e.pointerId);drawShips();return}
if(sel>=0){add(sv.dataset.v,sel,[pt.x,pt.y]);return}if(selId){selId=null;renderPlan()}});
sv.addEventListener('pointermove',e=>{if(!mv||mv.sv!==sv)return;const pt=svgPt(sv,e.clientX,e.clientY),dx=pt.x-mv.sx,dy=pt.y-mv.sy;if(!mv.moved){if(Math.hypot(dx,dy)<.4)return;hist.push(snap());mv.moved=true}
mv.p.x=+Math.min(130,Math.max(-12,mv.x0+dx)).toFixed(1);mv.p.y=+Math.min(40,Math.max(-40,mv.y0+dy)).toFixed(1);drawShips()});
const up=()=>{if(mv){mv=null;renderPlan()}};sv.addEventListener('pointerup',up);sv.addEventListener('pointercancel',up)}
$('#cards').addEventListener('pointerdown',e=>{const c=e.target.closest('.card');if(!c||e.button>0)return;if(e.pointerType!=='mouse'&&!e.target.closest('.grip'))return;drag={x:e.clientX,y:e.clientY,i:+c.dataset.i}});
const svgAt=(x,y)=>{const el=document.elementFromPoint(x,y);return el?el.closest('svg.ship'):null};
window.addEventListener('pointermove',e=>{if(!drag)return;
if(!ghost){if(Math.hypot(e.clientX-drag.x,e.clientY-drag.y)<6)return;ghost=document.createElement('div');ghost.className='ghost';ghost.innerHTML=(D[drag.i].td?`<img src="${D[drag.i].td}" alt="" style="height:64px;width:auto">`:thumb(D[drag.i]))+esc(D[drag.i].n);document.body.append(ghost);sel=drag.i;renderPlan();for(const c of $$('.card'))c.classList.toggle('on',+c.dataset.i===sel)}
ghost.style.left=e.clientX+'px';ghost.style.top=e.clientY+'px';const s=svgAt(e.clientX,e.clientY);for(const x of $$('svg.ship'))x.classList.toggle('hov',x===s);
const t=document.elementFromPoint(e.clientX,e.clientY);const tab=t&&t.closest('[role=tab]');if(tab&&tab.dataset.v!==view)setView(tab.dataset.v)});
const end=e=>{if(!drag)return;if(ghost){const s=e.type==='pointerup'?svgAt(e.clientX,e.clientY):null;ghost.remove();ghost=null;for(const x of $$('svg.ship'))x.classList.remove('hov');dragged=true;setTimeout(()=>{dragged=false},80);if(s){const pt=svgPt(s,e.clientX,e.clientY);add(s.dataset.v,drag.i,[pt.x,pt.y])}}drag=null};
window.addEventListener('pointerup',end);window.addEventListener('pointercancel',end);
let v0='external';try{v0=localStorage.getItem('libview')||v0}catch(e){}
renderCards();setView(v0==='internal'?'internal':'external');
