# WMK Vida Loka v1.4.0 🚗 🎯

**Jogo de mundo aberto 2D top-down com World Studio, editor de missões, editor de bots e arena de combate.**

**Créditos:** Walney Moreira Klein — walneyk@hotmail.com

## Como jogar
1. Baixe o repositório por **Code → Download ZIP**, extraia e abra `index.html`.
2. Selecione um dos quatro mapas no menu e clique em **Iniciar jogo**.
3. Em mapas urbanos: WASD mover/dirigir, E entrar/sair, Shift correr e Espaço freio de mão.
4. Em Terminal Zero: WASD mover, mouse mirar, botão esquerdo disparar, R recarregar e Escape voltar ao menu.

## Mapas editáveis
- **Baía Nova:** cidade original com 28 prédios definidos como objetos editáveis.
- **Costa Dourada:** marina, praia, lojas e paisagem costeira.
- **Serra Brava:** floresta, casas, armazéns e exploração.
- **Terminal Zero:** arena top-down, contêineres, obstáculos, cinco bots iniciais e equipes.

Todos os mapas podem ser editados ou duplicados no World Studio: selecionar mapa → **Duplicar mapa** → ajustar objetos, dimensões, colisões, sprites e bots → Salvar → Testar. Os mapas originais não precisam ser sobrescritos.

## Editores no menu
**World Studio:** criar, editar, duplicar, excluir mapas personalizados; inserir objetos, bots, imagens PNG/JPG/WebP; configurar colisões, camada, rotação, largura, altura e spawn; JSON de importação/exportação.

**Editor de Missões:** criar, duplicar, editar e excluir; ativar apenas nos mapas escolhidos ou em todos; tipos de coleta, entrega, fuga, corrida, checkpoints, eliminação de bots e sobrevivência; W$, temporização e quantidade de inimigos.

**Editor de Bots:** configurar equipe (vermelha, azul, neutra), vida, dano, alcance, visão, precisão, velocidade, arma fictícia, comportamento guarda/patrulha/perseguidor e pontos de patrulha. Importar/exportar JSON.

## Assets externos / Kenney
Importar arquivos PNG, JPG e WebP de até 750 KB no World Studio. A colisão não é gerada da imagem — configure-a manualmente. Para pacotes 3D GLB/OBJ/FBX, renderize os modelos com câmera superior para sprites. Veja [Kenney Topdown Shooter](https://kenney.nl/assets/topdown-shooter) (CC0; confira licença individual).

## Documentação
- [Manual do Jogador](manual-jogador.html)
- [Manual do Desenvolvedor](manual-desenvolvedor.html)
- [Pesquisa](pesquisa.html)
- [Roadmap](roadmap.html)
- [Relatório de testes](testes/RELATORIO.md)

## Testes
A suíte do ZIP local passou **39/39** verificações automatizadas no Chromium, cobrindo interface, duplicação de mapas, bot, JSON, missão, disparos, recarga e condições de vitória. Persistência real entre sessões não foi verificada devido a bloqueio de navegação local no ambiente de teste; o armazenamento foi simulado. Bots ainda podem ficar presos em cobertura: não há A*.

## Licença
MIT para contribuições WMK cuja autoria é conhecida. **A licença/autoria do código HTML original ainda não foi comprovada**: não é possível garantir que a obra derivada inteira seja MIT até resolver essa condição. Os assets externos possuem licenças independentes.

## Contato
Walney Moreira Klein — walneyk@hotmail.com
