# WMK Vida Loka — Relatório de testes v2.7.0

Chromium/Playwright, HTML carregado no navegador com armazenamento local simulado.

| Suíte | Resultado |
|---|---:|
| test_avatar.py | 12/12 |
| test_catalogos.py | 19/19 |
| test_creator_roundtrip.py | 3/3 |
| test_gizmos.py | 13/13 |
| test_smoke.py | 39/39 |
| test_v20.py | 18/18 |
| test_v21.py | 22/22 |
| test_v22.py | 18/18 |
| test_v23.py | 23/23 |
| test_v24.py | 16/16 |
| test_v25.py | 13/13 |
| test_v26.py | 26/26 |
| test_v27.py | 23/23 |

**Total 245/245 verificações em 13 suítes.**

A suíte v2.6 verifica abertura, arraste, restauração, armazenamento e retorno ao modo fixo dos três laboratórios, ausência de erros JavaScript e existência das rotinas da IA. Os testes de IA são estruturais, não um teste exaustivo de eficácia tática.

**Pendências:** validação da persistência real após reiniciar Chromium no Windows, desempenho sob muitos bots, cobertura com obstáculos complexos.
Suíte de avatares legada atualizada para aceitar o novo nome de exportação `wmk-avatar-v2.json`; PNGs e persistência foram testados com armazenamento simulado. Não foi validado o reinício de navegador no Windows.
