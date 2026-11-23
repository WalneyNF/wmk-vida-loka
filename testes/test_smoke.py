"""Smoke test WMK v1.4.0 — suíte ampliada de 39 verificações está no ZIP da versão."""
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('about:blank');page.set_content((root/'index.html').read_text(encoding='utf8'))
 assert page.locator('.wmk-map-card').count()==4
 page.locator('#wmkOpenBotStudio').click()
 assert page.locator('#wmkBotStudio').is_visible()
 page.locator('#botReturn').click()
 page.locator('#wmkOpenMapStudio').click()
 assert page.locator('#wmkMapStudio').is_visible()
 assert not errors,errors
 print('Sucesso: mapa, menus e editores')
 b.close()
