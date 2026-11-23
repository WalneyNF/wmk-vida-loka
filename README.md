# 🚗 WMK Vida Loka v2.0.0 — Mundo aberto e criador de jogos 2D

**Walney Moreira Klein — walneyk@hotmail.com**

Jogo e editor em HTML5 Canvas, CSS e JavaScript. Quatro cenários iniciais: Baía Nova, Costa Dourada, Serra Brava e Terminal Zero. Projeto em português, com moeda fictícia **W$**.

## Executar
1. Baixe o repositório usando **Code → Download ZIP**.
2. Extraia todos os arquivos preservando `assets/`, `testes/` e os manuais.
3. Abra `index.html`. Recomendado servir a pasta por um servidor HTTP local (por exemplo XAMPP) para testar armazenamento local.
4. Escolha o mapa. WASD move, Shift corre, E entra/sai de veículos; no modo arena, mouse mira/dispara e R recarrega.

## Editores disponíveis
- **World Studio:** editar/criar/copiar mapas, posicionar e transformar objetos e bots com gizmos, exportar/importar JSON, usar grade, salvar prefab do objeto selecionado, pintar terreno por blocos, visualizar colisões e desenhar pontos de patrulha.
- **Bot Lab:** equipes, vida, arma, dano, precisão, comportamento, waypoints e avatar visual.
- **Object Lab:** modelos reutilizáveis com colisão, sprite, escala e cor.
- **Arsenal Lab:** armas fictícias por JSON com dano, cadência, alcance e munição.
- **Avatar Lab:** personalização, perfis salvos e aparência reutilizável para bots.
- **Editor de Missões:** criar, duplicar, excluir, testar, definir mapas e recompensas em W$, visualizar fluxo linear de objetivos.
- **WMK Game Creator:** selecionar mapas e missões, gerar/importar pacote JSON, testar o mapa inicial.

## O que mudou na v2.0.0
- Navegação **A*** simples em grade, aplicada aos bots da arena com cache de rotas.
- Ferramenta visual de waypoints no World Studio.
- Depurador de colisões e pincel de terreno retangular.
- Salvamento direto de objetos selecionados como prefabs.
- Biblioteca de avatares e vínculo com bots.
- Visão linear do fluxo de missões.
- Game Creator para importação/exportação de pacotes completos de dados.

## Manuais
- [Manual do jogador](manual-jogador.html)
- [Manual do desenvolvedor](manual-desenvolvedor.html)
- [Laboratório de evolução](evolucao.html)
- [Roadmap](roadmap.html)
- [Pesquisa](pesquisa.html)
- [Relatório de testes](testes/RELATORIO.md)

## Testes
104/104 verificações automatizadas aprovadas nas suítes `test_smoke.py`, `test_gizmos.py`, `test_catalogos.py`, `test_avatar.py`, `test_v20.py` e `test_creator_roundtrip.py`. Não substituem testes em aparelhos reais.

## Limitações honestas
O Game Creator gera um **pacote JSON**, não um executável ou HTML independente. O fluxo de missões é uma visualização, não um editor de grafos com ramificações. A IA ainda não tem cover/avoidance completo. O pincel não tem autotile. Avatares são vetoriais e não possuem spritesheets de oito direções. Sem multiplayer. Faça backups JSON regularmente.

## Licença
O arquivo `LICENSE` contém MIT para o material passível de licenciamento por seus titulares. **É necessário verificar a licença e a autoria do protótipo de origem antes de afirmar que todo o código-base pode ser distribuído como MIT.** Assets externos mantêm as respectivas licenças.

**Repositório:** https://github.com/WalneyNF/wmk-vida-loka
