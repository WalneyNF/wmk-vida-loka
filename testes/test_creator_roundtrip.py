from pathlib import Path
import json
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parents[1]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(accept_downloads=True)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('dialog',lambda d:d.accept())
    page.set_content((p/'index.html').read_text(encoding='utf8'),wait_until='load')
    page.locator('#wmkOpenGameCreator').click()
    data=page.evaluate('buildCreatorPackage()')
    data['maps'][0]['id']='mapa-avulso'
    data['maps'][0]['name']='Mapa Avulso'
    data['missions']=[]
    count=page.evaluate('mapCatalog.length')
    page.locator('#creatorImportFile').set_input_files(files=[{'name':'meu-jogo.json','mimeType':'application/json','buffer':json.dumps(data).encode()}])
    page.wait_for_timeout(200)
    assert page.evaluate('mapCatalog.length')==count+len(data['maps'])
    assert page.evaluate("mapCatalog.some(m=>m.id==='mapa-avulso')")
    assert not errors,errors
    print('3/3 verificações: importação, mapa e sem exceções')
    browser.close()
