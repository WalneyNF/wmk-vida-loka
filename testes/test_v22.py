"""World Studio v2.2 — smoke test em Chromium (playwright)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]/"index.html"
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path="/usr/bin/chromium",headless=True,args=["--no-sandbox"])
 page=browser.new_page(viewport={"width":1600,"height":960},accept_downloads=True)
 errors=[];page.on("pageerror",lambda e:errors.append(str(e)))
 page.goto("about:blank")
 page.evaluate("""+"'''"+"""(()=>{let d=new Map;Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>d.get(k)||null,setItem:(k,v)=>d.set(k,String(v))}})})()"""+"'''"+""")
 page.set_content(P.read_text(encoding="utf-8"))
 assert page.locator("#wmkMain").is_visible()
 page.locator("#wmkOpenMapStudio").click()
 page.locator("#studioMapSelect").select_option("terminal-zero")
 assert page.locator("#studioGroup").is_visible()
 page.locator("#studioTool").select_option("barrier")
 page.locator("#studioCanvas").click(position={"x":320,"y":280})
 first=page.evaluate("selectedObjectId")
 page.locator("#studioTool").select_option("barrier")
 page.locator("#studioCanvas").click(position={"x":445,"y":355})
 second=page.evaluate("selectedObjectId")
 assert first!=second
 page.evaluate("([a,b])=>{studioSelection=new Set(['obj:'+a,'obj:'+b]);selectedObjectId=b;renderObjectList();drawStudio()}",[first,second])
 assert page.evaluate("studioSelection.size")==2
 page.locator("#studioGroup").click()
 assert page.evaluate("new Set(selectedStudioEntries().map(x=>x.entity.groupId)).size")==1
 page.locator("#studioCloneSelection").click()
 assert page.evaluate("studioSelection.size")==2
 page.on("dialog",lambda d:d.accept("Prefab de teste"))
 page.locator("#studioSaveComposite").click()
 assert page.evaluate("compositeCatalog.some(p=>p.name==='Prefab de teste')")
 before=page.evaluate("editingMap.objects.length")
 page.locator("#studioInsertComposite").click()
 assert page.evaluate("editingMap.objects.length")==before+2
 page.locator("#studioUngroup").click()
 assert page.evaluate("selectedStudioEntries().every(x=>!x.entity.groupId)")
 page.locator("#studioUndo").click()
 page.locator("#studioRedo").click()
 assert not errors, errors
 browser.close()
 print("OK: World Studio v2.2, seleção múltipla, grupo, duplicação, prefab, desfazer/refazer.")
