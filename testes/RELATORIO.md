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
