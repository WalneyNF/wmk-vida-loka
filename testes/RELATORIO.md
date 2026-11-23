# Relatório da v2.4.0 — WMK Vida Loka

Ambiente: Chromium headless, Python Playwright, Node.js 22 (23/11/2026).

| Suíte | Resultado |
|---|---:|
| Avatar | 12/12 |
| Catálogos | 19/19 |
| Creator roundtrip | 3/3 |
| Gizmos | 13/13 |
| Smoke | 39/39 |
| v2.0 | 18/18 |
| v2.1 | 22/22 |
| v2.2 | 18/18 |
| v2.3 | 23/23 |
| v2.4 | 16/16 |
| **Total** | **183/183** |

A importação assíncrona de prefabs exigiu correção da sincronização do teste da v2.2. Testes reais de persistência após reiniciar o navegador por HTTP no Windows ainda estão pendentes. Os presets de terreno não são atlas/autotile. Desempenho com muitos bots também não foi validado.
