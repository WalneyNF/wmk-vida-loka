/* WMK Vida Loka 2.1 — biblioteca de inspeção e backup sem executar JSON.
 * Walney Moreira Klein — walneyk@hotmail.com */
(function(root){
 'use strict';
 const clone=value=>JSON.parse(JSON.stringify(value));
 const list=value=>Array.isArray(value)?value:[];
 const id=value=>String(value??'').trim();
 function inspect(project){
  const maps=list(project.maps),missions=list(project.missions),objects=list(project.objects),weapons=list(project.weapons),avatars=list(project.avatars),assets=list(project.assets);
  const problems=[],uses={maps:[],missions:[],weapons:[],avatars:[],assets:[]};
  for(const [kind,items] of [['mapa',maps],['missão',missions],['objeto',objects],['arma',weapons],['avatar',avatars],['sprite',assets]]){
   const seen=new Set();
   items.forEach((item,i)=>{const key=id(item?.id);if(!key)problems.push({kind,code:'missing-id',message:kind+' #'+(i+1)+': identificador ausente'});else if(seen.has(key))problems.push({kind,code:'duplicate-id',message:kind+': ID duplicado «'+key+'»'});seen.add(key)});
  }
  const mapIds=new Set(maps.map(m=>id(m?.id))),weaponIds=new Set(weapons.map(w=>id(w?.id))),avatarIds=new Set(avatars.map(a=>id(a?.id))),spriteIds=new Set(assets.map(a=>id(a?.id)));
  maps.forEach(map=>{
   const mapName=String(map.name||map.id||'mapa');
   list(map.objects).forEach(o=>{if(o.assetId){uses.assets.push({id:o.assetId,at:mapName});if(!spriteIds.has(o.assetId))problems.push({kind:'sprite',code:'missing-reference',message:mapName+' / '+(o.name||o.id)+': sprite «'+o.assetId+'» ausente'})}});
   list(map.bots).forEach(bot=>{
    if(bot.weapon){uses.weapons.push({id:bot.weapon,at:mapName});if(!weaponIds.has(bot.weapon))problems.push({kind:'arma',code:'missing-reference',message:mapName+' / '+(bot.name||bot.id)+': arma «'+bot.weapon+'» ausente'})}
    if(bot.avatarId){uses.avatars.push({id:bot.avatarId,at:mapName});if(!avatarIds.has(bot.avatarId))problems.push({kind:'avatar',code:'missing-reference',message:mapName+' / '+(bot.name||bot.id)+': avatar «'+bot.avatarId+'» ausente'})}
   });
  });
  missions.forEach(m=>list(m.maps).forEach(mapId=>{uses.maps.push({id:mapId,at:m.title||m.id});if(!mapIds.has(mapId))problems.push({kind:'mapa',code:'missing-reference',message:'Missão «'+(m.title||m.id)+'»: mapa «'+mapId+'» ausente'})}));
  return {version:1,counts:{maps:maps.length,missions:missions.length,objects:objects.length,weapons:weapons.length,avatars:avatars.length,assets:assets.length,bots:maps.reduce((n,m)=>n+list(m.bots).length,0),placedObjects:maps.reduce((n,m)=>n+list(m.objects).length,0)},problems,uses};
 }
 function validateBundle(bundle){if(!bundle||typeof bundle!=='object')throw new Error('Projeto inválido');if(!Array.isArray(bundle.maps)||!Array.isArray(bundle.missions))throw new Error('O pacote precisa de mapas e missões em listas');const r=inspect(bundle);if(r.problems.some(p=>p.code==='duplicate-id'||p.code==='missing-id'))throw new Error('Pacote contém IDs ausentes ou repetidos');return r}
 function makeBackup(project){const data=clone(project);validateBundle(data);return {format:'wmk-vida-loka-library',version:1,generatedAt:new Date().toISOString(),project:data}}
 root.WMKCore=Object.freeze({version:'2.1.0',inspect,validateBundle,makeBackup,clone});
})(typeof window!=='undefined'?window:globalThis);
