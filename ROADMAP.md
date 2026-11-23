# Roadmap WMK Vida Loka

## v2.0.0 — Integrado e testado
- [x] Gizmos, bot editor, objetos/armas e quatro mapas editáveis.
- [x] Pincel básico de terreno em blocos e exibição de colisões.
- [x] Prefabs simples a partir de objetos selecionados.
- [x] Rotas de patrulha por clique no World Studio.
- [x] Navegação A* em grade, experimental, para bots da arena.
- [x] Biblioteca de perfis de avatar e vinculação aos bots.
- [x] Visualização linear do fluxo de missões.
- [x] Game Creator com pacote JSON importável/exportável.
- [x] Manuais e testes automatizados.

## Próximas etapas — ainda não implementadas
- [ ] World Studio modular: multisseleção, grupos, outliner, tilesets e autotile.
- [ ] Avatar por partes com animações e equipamento visual.
- [ ] IA tática completa: cobertura, investigação, avoidance e formação.
- [ ] Editor de missões por nós editáveis, condições, escolhas e diálogos.
- [ ] Mundo vivo: NPCs com rotinas, interiores e trânsito simulado.
- [ ] Garagem e veículos por JSON, inventário e economia W$ persistente.
- [ ] Campanhas com progressão entre mapas.
- [ ] Empacotar jogo HTML independente e instaladores.
- [ ] Multiplayer autoritativo, depois de estabilizar o modo offline.

## Qualidade
Antes de cada publicação executar `testes/test_smoke.py`, `testes/test_gizmos.py`, `testes/test_catalogos.py`, `testes/test_avatar.py`, `testes/test_v20.py` e `testes/test_creator_roundtrip.py`.
