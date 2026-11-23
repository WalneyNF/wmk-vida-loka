# Relatório de testes — WMK Vida Loka v2.0.0

| Teste | Resultado |
|---|---|
| test_smoke.py | 39/39 |
| test_gizmos.py | 13/13 |
| test_catalogos.py | 19/19 |
| test_avatar.py | 12/12 |
| test_v20.py | 18/18 |
| test_creator_roundtrip.py | 3/3 |
| **TOTAL** | **104/104** |

**Validados:** menus, mapas, gizmos, edição de bots, armas e avatares, rotas e pintura de terreno, colisão de depuração, fluxo de missão, exportação/importação de pacotes, navegação A* unitária, inicialização sem exceções JavaScript.

**Não validados integralmente:** FPS em dezenas de agentes, persistência real entre sessões em todos os browsers, mobile, sincronização multiplayer e geração de jogo HTML independente. O navegador do ambiente bloqueou acesso HTTP local em um teste, portanto parte da suíte usa `set_content` e armazenamento simulado.
