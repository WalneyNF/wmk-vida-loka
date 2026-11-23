"""Testes de gizmos WMK Vida Loka v1.5. Requer Playwright/Chromium."""
from pathlib import Path
from playwright.sync_api import sync_playwright
HTML=Path(__file__).resolve().parents[1]/'index.html'
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':1600,'height':960})
    errors=[]
    page.on('pageerror',lambda error:errors.append(str(error)))
    page.goto('about:blank')
    page.evaluate("Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:()=>null,setItem:()=>{}}})")
    page.set_content(HTML.read_text(encoding='utf8'))
    page.locator('#wmkOpenMapStudio').click()
    page.locator('#studioMapSelect').select_option('terminal-zero')
    page.locator('#studioTool').select_option('barrier')
    page.locator('#studioCanvas').click(position={'x':480,'y':310})
    assert page.evaluate('selectedObject() !== null')
    def move_handle(name,dx,dy):
        pos=page.evaluate("""(name)=>{
          const v=gizmoGeometry()[name],t=drawingTransform(),r=studioCanvas.getBoundingClientRect();
          return {x:r.left+(v.x*t.scale+t.ox)*r.width/studioCanvas.width,
                  y:r.top+(v.y*t.scale+t.oy)*r.height/studioCanvas.height}
        }""",name)
        page.mouse.move(pos['x'],pos['y'])
        page.mouse.down()
        page.mouse.move(pos['x']+dx,pos['y']+dy,steps=10)
        page.mouse.up()
    page.locator('#gizmoMove').click()
    before=page.evaluate('selectedObject().x')
    move_handle('x',50,0)
    assert page.evaluate('selectedObject().x')>before
    page.locator('#gizmoScale').click()
    before=page.evaluate('selectedObject().w')
    move_handle('scale',40,30)
    assert page.evaluate('selectedObject().w')>before
    page.locator('#gizmoRotate').click()
    before=page.evaluate('selectedObject().rotation')
    move_handle('rotate',45,0)
    assert page.evaluate('selectedObject().rotation')!=before
    page.locator('#studioTool').select_option('bot')
    page.locator('#pickerCards .wmk-picker-card').first.click()
    page.locator('#studioCanvas').click(position={'x':650,'y':390})
    assert page.evaluate('selectedBotInMap() !== null')
    page.locator('#gizmoMove').click()
    before=page.evaluate('selectedBotInMap().x')
    move_handle('x',55,0)
    assert page.evaluate('selectedBotInMap().x')>before
    page.locator('#studioSave').click()
    page.locator('#studioReturn').click()
    page.locator('#wmkOpenMissionStudio').click()
    assert page.locator('#wmkEditor').is_visible()
    assert not page.locator('#wmkMain').is_visible()
    assert not page.locator('.mission-advanced').evaluate('(el)=>el.open')
    page.locator('.mission-advanced summary').click()
    assert page.locator('.mission-advanced').evaluate('(el)=>el.open')
    page.locator('#missionReturn').click()
    assert page.locator('#wmkMain').is_visible()
    assert not errors, errors
    print('OK: World Studio + Editor de Missões')
    browser.close()
