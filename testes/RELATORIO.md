# Relatório v1.5 — WMK Vida Loka

- 39/39 verificações de regressão da v1.4 aprovadas no Chromium.
- 13/13 verificações do novo Editor e gizmos aprovadas no Chromium.
- Desfazer/refazer e checkbox Grade 25 testados adicionalmente.
- JavaScript validado com `node --check`.

**Não garantido pelos testes:** colisão após rotação em ângulos extremos, sprites grandes, persistência HTTP real, uso em dispositivos móveis, performance de muitos bots.

Executar: `python -m pip install playwright`, `python -m playwright install chromium`, `python testes/test_smoke.py`, `python testes/test_gizmos.py`. No ZIP local, o teste de gizmos contém cenários adicionais.
## WMK v1.6.0 — Catálogos (23/11/2026)
- 39/39 testes do fluxo principal.
- 13/13 testes de gizmos.
- 19/19 testes de catálogos e seletor de bots.
- **71/71 verificações automatizadas aprovadas** no Chromium headless; sem exceções JavaScript reportadas.
- Testados: criação/duplicação/exportação de objetos; armas customizadas e atribuição a bots; inserção de prefabs; janela de seleção de bots e identificação por equipe.
- Observações: localStorage simulado; não equivalem a teste real de retenção entre sessões HTTP/Windows nem de performance prolongada.

## v1.7 — Testes do Avatar Lab
- 12/12 verificações aprovadas em Chromium com `page.set_content` e localStorage simulado.
- Abertura de editor, canvas, alteração de valores, salvar, estado local, exportação, reset não destrutivo, retorno ao menu, início do jogo e ausência de exceções JS.
- O ambiente bloqueou navegações `file://` e HTTP local; a persistência real entre sessões no Windows/HTTP ainda não foi testada.
