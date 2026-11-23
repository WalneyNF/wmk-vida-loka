"""WMK Vida Loka v2.1 — testes da Biblioteca (Playwright + Chromium).
Executa com: python testes/test_v21.py
A navegação HTTP pode estar bloqueada em ambientes automatizados:
por isso o HTML e o módulo são carregados como conteúdo na página.
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8').replace(
 '<script src="js/wmk-core.js"></script>',
 '<script>'+ (root/'js/wmk-core.js').read_text(encoding='utf-8') + '</script>')
checks=[]
def test(label,condition):
 ok=bool(condition);checks.append(ok);print(('OK' if ok else 'FALHA')+' '+label)
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':900},accept_downloads=True)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(html,wait_until='load')
 test('Menu',page.locator('#wmkMain').is_visible())
 test('Core',page.evaluate("WMKCore.version==='2.1.0'"))
 test('Atalho',page.locator('#wmkOpenLibrary').is_visible())
 page.locator('#wmkOpenLibrary').click()
 test('Biblioteca aberta',page.locator('#wmkLibrary').is_visible())
 test('Relatório inicial',page.evaluate('wmkLibraryLastReport.problems.length===0'))
 test('Quatro mapas',page.evaluate('wmkLibraryLastReport.counts.maps===4'))
 test('Armas cadastradas',page.evaluate('wmkLibraryLastReport.counts.weapons>=3'))
 for typ in ['missions','bots','objects','weapons','avatars','assets']:
  page.locator('#wmkLibraryType').select_option(typ)
  test('Categoria '+typ,page.locator('#wmkLibraryEntries').count()==1)
 with page.expect_download() as item:page.locator('#wmkLibraryBackup').click()
 tmp=root/'testes'/'biblioteca-test-backup.json';item.value.save_as(tmp)
 obj=json.loads(tmp.read_text());tmp.unlink(missing_ok=True)
 test('Backup JSON',obj.get('format')=='wmk-vida-loka-library' and len(obj['project']['maps'])==4)
 test('Backup de prefabs',len(obj['project']['objects'])>=3)
 page.locator('#wmkLibraryType').select_option('weapons')
 page.locator('#wmkLibraryGoEditor').click()
 test('Ir ao Arsenal Lab',page.locator('#wmkWeaponStudio').is_visible())
 page.locator('#weaponReturn').click()
 page.locator('#wmkOpenLibrary').click()
 page.evaluate("mapCatalog[0].bots.push({...sanitizeBot({id:'test-bot',name:'Bot teste'},0),weapon:'arma-xyz',avatarId:'avatar-xyz'});mapCatalog[0].objects.push({...sanitizeMap({objects:[{id:'obj-xyz',type:'sprite',assetId:'sprite-xyz'}]}).objects[0]})")
 page.locator('#wmkLibraryAudit').click()
 for kind in ['arma','avatar','sprite']:
  test('Referência inválida '+kind,page.evaluate("(kind)=>wmkLibraryLastReport.problems.some(p=>p.kind===kind)",kind))
 page.locator('#wmkLibraryReturn').click()
 test('Voltar ao menu',page.locator('#wmkMain').is_visible())
 page.locator('#wmkOpenAvatarStudio').click()
 page.locator('#avatarName').fill('Teste WMK 21')
 page.locator('#avatarProfileSave').click()
 test('Perfil na memória',page.locator('#avatarProfiles option').filter(has_text='Teste WMK 21').count()==1)
 test('Sem erro JS',not errors)
 browser.close()
print(sum(checks),'/',len(checks))
assert all(checks)
