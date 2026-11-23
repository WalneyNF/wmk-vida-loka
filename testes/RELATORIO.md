# Relatório de testes — WMK Vida Loka v2.1.0

Data: 23/11/2026. Ambiente: Chromium headless, Python Playwright e Node.js.

| Suíte | Resultado |
|---|---:|
| test_smoke.py | 39/39 |
| test_v20.py | 18/18 |
| test_catalogos.py | 19/19 |
| test_gizmos.py | 13/13 |
| test_avatar.py | 12/12 |
| test_creator_roundtrip.py | 3/3 |
| test_v21.py | 22/22 |
| **Total** | **126/126** |

## Novidades verificadas
Abertura de Biblioteca; carregamento de WMKCore; categorias e contagens; auditoria de referências; detecção de arma/avatar/sprite inexistentes; exportação JSON; navegação para Arsenal Lab; retorno ao menu; ausência de erros de JavaScript no teste. A verificação da sintaxe do script principal e do módulo passou.

## Restrições de teste
O Chromium do ambiente bloqueou navegação direta HTTP e `file://` (`ERR_BLOCKED_BY_ADMINISTRATOR`). Os testes de UI usaram `page.set_content` com módulo incorporado. **O carregamento por HTTP e o armazenamento persistente após reinício real permanecem pendentes**; validar no Windows local. A biblioteca não altera conteúdo e seu backup próprio é apenas para auditoria, não restauração.


## v2.2.0 — World Studio (23/11/2026)

- **144/144 verificações aprovadas localmente** (8 suítes em Chromium, incluindo 18 novas no script de testes distribuído no ZIP).
- Seleção múltipla por Ctrl/Shift, deslocamento em grupo, IDs persistidos, agrupamento, desagrupamento e duplicação.
- Prefabs compostos: criação, inserção, exportação/importação JSON, desfazer/refazer.
- Erros JavaScript não observados nas suítes executadas.
- O arquivo `testes/test_v22.py` no GitHub contém um smoke test reproduzível simplificado; o ZIP contém a suíte completa de 18 verificações.
- **Limitações de teste:** Chromium bloqueou navegação HTTP localhost; persistência após reload real do Windows/HTTP ainda não foi comprovada. Escala/rotação de grupos, hierarquia aninhada e autotile continuam pendentes.


## v2.3.0 — Hierarquia, camadas e pivô coletivo
- test_v23.py: 23/23 verificações Chromium com armazenamento simulado.
- Regressão: nove suítes, 167/167 verificações aprovadas.
- Validações: árvore e grupos, visibilidade/bloqueio de camadas, pivôs, escala e rotação coletiva, undo/redo, exportação JSON e ausência de exceções JS.
- JavaScript passou por node --check.
- Limite: HTTP local bloqueado por política do Chromium deste ambiente (ERR_BLOCKED_BY_ADMINISTRATOR). Persistência real em Windows ainda não validada.
