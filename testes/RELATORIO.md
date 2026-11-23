# Relatório v1.5 — WMK Vida Loka

- 39/39 verificações de regressão da v1.4 aprovadas no Chromium.
- 13/13 verificações do novo Editor e gizmos aprovadas no Chromium.
- Desfazer/refazer e checkbox Grade 25 testados adicionalmente.
- JavaScript validado com `node --check`.

**Não garantido pelos testes:** colisão após rotação em ângulos extremos, sprites grandes, persistência HTTP real, uso em dispositivos móveis, performance de muitos bots.

Executar: `python -m pip install playwright`, `python -m playwright install chromium`, `python testes/test_smoke.py`, `python testes/test_gizmos.py`. No ZIP local, o teste de gizmos contém cenários adicionais.