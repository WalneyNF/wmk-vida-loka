# WMK Vida Loka — Roadmap

## v2.1 — Biblioteca compartilhada e confiabilidade
- [x] Módulo `js/wmk-core.js` para diagnóstico dos recursos
- [x] Biblioteca de consulta: mapas, missões, bots, armas, objetos, avatares, sprites
- [x] Detector de referências e IDs quebrados
- [x] Backup JSON de auditoria, sem modificação automática
- [x] Testes automatizados e documentação em português
- [ ] Validar recarregamento real e armazenamento HTTP no Windows

## v2.2 — World Studio profissional
- [ ] Separação adicional do motor e dos editores em módulos
- [ ] Multisseleção, hierarquia, grupos e prefabs compostos
- [ ] Editor de tilesets e depurador de colisões expandido

## v2.3 — IA e partidas por equipes
- [ ] Navegação A* com avoidance entre agentes
- [ ] Comportamentos de cobertura, investigação e patrulha
- [ ] Rounds, respawn e placar

## v2.4 — Cidade viva
- [ ] Trânsito, pedestres e NPCs com rotinas
- [ ] Garagem, veículos JSON e economia W$ persistente
- [ ] Interiores e eventos

## v2.5 — Criadores
- [ ] Missões por nós com ramificações
- [ ] Sprites por camadas e animações
- [ ] Campanhas entre mapas

## v3.0 — Distribuição
- [ ] Pacotes versionados e jogo HTML independente
- [ ] Multiplayer experimental após estabilização offline


## v2.2 — Funcionalidades entregues
- [x] Seleção múltipla Ctrl/Shift
- [x] Agrupar, mover seleção, desagrupar e duplicar
- [x] Prefabs compostos com importação/exportação JSON
- [x] 144 verificações automatizadas; testes HTTP reais ainda pendentes


## v2.3 — World Studio: hierarquia e transformação coletiva
- [x] Árvore clicável de objetos, grupos e bots
- [x] Camadas com visibilidade e bloqueio individual
- [x] Pivô central/objeto ativo, escala e rotação coletivas
- [x] JSON de mapas retrocompatível com layerSettings
- [x] 23 testes específicos e regressão geral no Chromium
- [ ] Árvore aninhada, seleção por caixa, autotile e pivô persistente


## v2.4 — World Studio (entregue)
- [x] Seleção por retângulo de bots e objetos
- [x] Grupos superiores com hierarquia e salvamento JSON
- [x] Presets de terreno: grama/asfalto/areia/água/pedra/terra
- [x] Painel de propriedades recolhível
- [x] Testes de regressão Chromium
- [ ] Atlas de tiles/spritesheet, autotile e pincel contínuo
- [ ] Drag-and-drop na árvore e testes de persistência real por HTTP no Windows

## v2.5 — World Studio
- [x] Atlas PNG (grade regular, prévia clicável, pintura, JSON)
- [x] Painéis móveis e redimensionáveis, com layout local
- [x] Busca de abrigo experimental para bots feridos
- [x] Testes automatizados v2.5

## Futuro
- [ ] Atlas com autotile, TMX/TSX e metadados
- [ ] Painéis móveis nos outros editores
- [ ] IA tática avançada e medição de desempenho
- [ ] Persistência real em Windows e migração para IndexedDB
