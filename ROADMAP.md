# WMK Vida Loka — Roadmap

## ✅ v1.5 implementado
- World Studio: seleção de objetos e bots na cena e lista
- Gizmos para mover X/Y/livre; escala e rotação para objetos
- Grade opcional de 25 unidades e histórico básico Ctrl+Z/Ctrl+Y
- Editor de Missões compacto em tela dedicada
- Testes Chromium: 39 regressões e 13 verificações dos gizmos
- Guia HTML de estudo e evolução

## Planejamento
- v1.6: multisseleção, grupos, camadas visíveis, prefabs, pivôs, copiadora e biblioteca de sprites.
- v1.7: bots A*, comportamentos de estados, navegação de waypoints e cobertura.
- v1.8: equipes, rounds, placar, respawn e modos de jogo.
- v1.9: editor de missões por nós, eventos, diálogos e condições.
- v2.0: campanhas, inventário, economia W$, veículos e personagens JSON.
- Futuro: WMK Game Creator e multiplayer.

Consulte [evolucao.html](evolucao.html) para o estudo prático de cada etapa.
## WMK v1.6.0 — Implementado
- Seletor de bots por cartões com 🔴 inimigo, 🔵 aliado e ⚪ neutro.
- Object Lab: biblioteca de prefabs com sprites, colisões, camada e dimensões.
- Arsenal Lab: armas fictícias com dano, alcance, cadência, capacidade e precisão.
- World Studio insere modelos do Object Lab e Bot Lab seleciona armas cadastradas.
- Exportação/importação JSON por catálogo e inclusão no backup completo.

## Prioridades futuras
- IA com A*, waypoints e patrulhas visuais; controle de armas do jogador, munição e recarga dos bots.
- Manipulação completa de personagens (sprites, animações), grupos e camadas.
- Empacotamento de projetos e validação de persistência real no Windows.
