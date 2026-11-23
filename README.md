# 🚗 WMK Vida Loka — v1.5.0

Jogo de mundo aberto **2D top-down** com quatro mapas iniciais (Baía Nova, Costa Dourada, Serra Brava e Terminal Zero), veículos, combate top-down, bots, missões, moedas W$ e ferramentas de criação.

**Créditos WMK:** Walney Moreira Klein — walneyk@hotmail.com.

## ▶ Executar
Baixe o ZIP em **Code → Download ZIP** no GitHub, extraia e abra `index.html` em um navegador moderno. Para testar persistência e importação, prefira usar um servidor HTTP local. O jogo não precisa ser compilado.

## 🗺 World Studio v1.5
1. No menu principal clique em **WORLD STUDIO**, selecione um mapa e prefira **Duplicar mapa**.
2. Escolha Prédio, Barreira, Árvore, Sprite ou **Inserir bot** e clique no mapa.
3. Selecione qualquer objeto ou bot clicando nele **ou pela lista lateral**.
4. Mude para **Selecionar/mover**. **G**: mover. Alça vermelha move em X, azul move em Y, centro move livre.
5. Para objetos, **S** ativa escala pela alça verde e **R** gira pela alça roxa. Bots podem ser movidos; escala e rotação de bots não são suportadas nesta versão.
6. **Grade 25** alinha posições ao mover; **Ctrl+Z** desfaz e **Ctrl+Y** refaz ações na cena. Histórico dos campos numéricos ainda é parcial.
7. Nas propriedades edite nome, coordenadas, dimensões, rotação, cor, camada e colisão. Bot selecionado abre **Editar bot no Bot Lab**.
8. Clique em **Salvar mapa** e **Testar mapa**. Exporte JSON para backup. PNG/JPG/WebP podem ser importados como sprites 2D; modelos 3D exigem renderização prévia.

## 📋 Editor de Missões
A partir do menu principal, entre no **EDITOR DE MISSÕES**: tela exclusiva compacta com lista de contratos e propriedades; **Regras avançadas** são recolhidas por padrão. Crie/edite/duplique/exclua missões, associe mapas (IDs separados por vírgula; vazio para todos), escolha metas, coordenadas, equipes, tempo e recompensas W$. Salve, teste e exporte JSON.

## ♟ Editor de Bots
Crie bots por mapa e configure nome, equipe, posição, vida, arma fictícia, dano, precisão, alcance, velocidade, visão, comportamento (guarda, patrulha, perseguidor) e waypoints. A IA de navegação com A* e cobertura permanece planejada.

## 🎮 Controles
- Exploração: **WASD** para mover, **E** para entrar/sair dos carros; **ESC** retorna ao menu.
- Terminal Zero: WASD movimenta, mouse mira, clique dispara, **R** recarrega.
- World Studio: **G/S/R**, alças coloridas, **Ctrl+Z/Y**, botão direito para pan, roda para zoom, Delete remove seleção.

## 📚 Documentação
- [Guia de evolução](evolucao.html): exercícios práticos, arquitetura e roadmap, incluindo implementação versus planejamento.
- [Manual do jogador](manual-jogador.html), [manual do desenvolvedor](manual-desenvolvedor.html), [pesquisa](pesquisa.html), [roadmap visual](roadmap.html), [tarefas](ROADMAP.md).
- [Testes de regressão](testes/test_smoke.py) e [testes dos gizmos](testes/test_gizmos.py).

## ✅ Validação
A versão local passou em **39/39 verificações de regressão**, **13/13 verificações dos novos gizmos** e um teste adicional de desfazer/refazer. É necessário testar manualmente colisões depois de rotacionar objetos, sprites grandes, persistência em HTTP e desempenho com muitos bots.

## ⚖ Licenciamento
O arquivo MIT está incluído para as partes originais licenciáveis. A distribuição integral sob MIT **depende de confirmar a licença/autoria do código-base original e dos assets usados**. Pacotes Kenney e outros recursos mantêm suas licenças próprias.

O projeto não é afiliado a GTA, CS ou seus titulares de marca.
