"""Verificações automatizadas WMK Vida Loka v2.6."""
from pathlib import Path
from playwright.sync_api import sync_playwright

p = Path(__file__).resolve().parents[1]
results = []

def test(label, value):
    results.append(bool(value))
    print(("OK " if value else "FALHA ") + label, flush=True)

with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path="/usr/bin/chromium", headless=True, args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1480, "height": 960})
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.goto("about:blank")
    page.set_content((p / "index.html").read_text())
    test("Menu inicial", page.locator("#wmkMain").is_visible())
    labs = [
        ("wmkBotStudio", "#wmkOpenBotStudio", "#botReturn", ".bot-grid"),
        ("wmkAvatarStudio", "#wmkOpenAvatarStudio", "#avatarReturn", ".avatar-layout"),
        ("wmkEditor", "#wmkOpenMissionStudio", "#missionReturn", ".editor-layout"),
    ]
    for name, open_btn, close_btn, layout in labs:
        page.locator(open_btn).click()
        test(name + " visível", page.locator("#" + name).is_visible())
        area = page.locator("#" + name + " " + layout)
        test(name + " alças", area.locator(".wmk-lab-grip").count() == 2)
        buttons = page.locator("#" + name + " .wmk-layout-controls button")
        buttons.first.click()
        test(name + " flutuante", area.evaluate('(e)=>e.classList.contains("wmk-lab-layout-active")'))
        pane = area.locator(".wmk-lab-pane").first
        initial = pane.evaluate("(e)=>e.offsetLeft")
        handle = pane.locator(".wmk-lab-grip")
        rect = handle.bounding_box()
        page.mouse.move(rect["x"] + 32, rect["y"] + 13)
        page.mouse.down()
        page.mouse.move(rect["x"] + 108, rect["y"] + 48, steps=6)
        page.mouse.up()
        test(name + " arrastável", pane.evaluate("(e)=>e.offsetLeft") >= initial + 20)
        key = "wmk-v26-layout-" + name
        test(name + " layout salvo", page.evaluate('(k)=>{let a=JSON.parse(localStorage.getItem(k));return a.enabled&&a.panels.length===2}', key))
        buttons.nth(1).click()
        test(name + " layout restaurado", pane.evaluate("(e)=>e.offsetLeft") <= 20)
        buttons.first.click()
        test(name + " padrão", not area.evaluate('(e)=>e.classList.contains("wmk-lab-layout-active")'))
        page.locator(close_btn).click()
    test("Cobertura", page.evaluate('typeof wmkCoverPosition === "function"'))
    test("Equipe", page.evaluate('wmkTeamSignals instanceof Map'))
    test("Navegação", page.evaluate('typeof botRouteAStar === "function"'))
    test("Sem erros JS", not errors)
    browser.close()
print("V2.6", sum(results), "/", len(results))
assert all(results)
