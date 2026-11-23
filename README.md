# 🚘 WMK Vida Loka — v1.3.1 (World Studio)

Jogo experimental 2D de mundo aberto com visão superior, feito com **HTML/CSS/JavaScript/Canvas** e pensado para PCs modestos. **Autor das modificações e documentação WMK:** Walney Moreira Klein — walneyk@hotmail.com.

## 🚀 Executar

1. Baixe os arquivos mantendo a pasta `assets` junto de `index.html`.
2. Abra `index.html` no navegador, ou execute `py -m http.server 8000` na pasta e acesse http://localhost:8000.
3. No **menu principal**, selecione um mapa, clique **Jogar** ou abra um dos editores.

## 🌍 Mapas

| Nome | ID | Características |
|---|---|---|
| Baía Nova | `baia-nova` | Cidade original, avenidas e edifícios |
| Costa Dourada | `costa-dourada` | Praia, água, píer e palmeiras |
| Serra Brava | `serra-brava` | Bosques, galpões e região rural |

O **Editor de Mapas** permite criar/duplicar/excluir mapas do usuário, adicionar, mover e dimensionar prédios, árvores, água, areia, barreiras e sprites importados, configurar rotação, camada, cor, colisão, posição inicial e testar o mapa. É um editor **2D em evolução**, não um editor 3D completo.

O **Editor de Missões** só é acessado pelo menu principal. Crie, edite ou exclua contratos, marque mapas permitidos (vazio = todos), modo, recompensa W$ e checkpoints de coordenadas. As mecânicas de objetivo ainda são simplificadas.

## 🎮 Controles

| Tecla | Ação |
|---|---|
| W/A/S/D e setas | Mover/dirigir |
| Shift | Correr a pé |
| E | Entrar/sair do carro |
| Espaço | Freio de mão |
| ESC | Voltar ao menu principal |

**No editor:** clique insere/seleciona; arraste move; roda faz zoom; botão direito arrastado move câmera; Delete apaga objeto selecionado.

## 🎨 Importar sprites externos

Acesse Editor de Mapas → Importar PNG/JPG/WebP → selecione o sprite → ferramenta **Sprite importado** → clique no mapa → ajuste dimensões, camada e colisão. Limite inicial: **750 KB por imagem**. Modelos GLB/GLTF/OBJ **não são suportados diretamente**; gere um sprite 2D primeiro. Consulte [Kenney Assets](https://kenney.nl/assets) e verifique a licença específica de cada recurso.

## 💾 Salvar e compartilhar

Os dados ficam no **localStorage** do navegador. Exporte mapas individuais, ou o projeto completo (mapas, missões e biblioteca de imagens) em JSON. Na importação completa, os dados existentes são substituídos após confirmação. **Faça backup antes de testar.** A importação de mapas admite JSON válido no formato WMK, não qualquer JSON arbitrário.

## 📖 Documentação

- [Manual do jogador](manual-jogador.html) — passo a passo de mapas, objetos, sprites externos e missões.
- [Manual do desenvolvedor](manual-desenvolvedor.html) — arquitetura, formatos JSON, colisões, persistência, segurança e evolução.
- [Pesquisa de referências](pesquisa.html) — estudos de jogos e assets.
- [Roadmap visual](roadmap.html) e [roadmap Markdown](ROADMAP.md).

## 🧭 Limitações atuais

O tráfego de NPCs, editor de ruas interativo, sistema avançado de eventos, seleção múltipla, undo/redo, 3D e física realista **não estão implementados**. Os mapas extras são cenários demonstrativos no mesmo tamanho de mundo. Imagens importadas são guardadas em Data URLs, sujeitas ao limite de armazenamento do navegador.

## 📜 Licenciamento

O arquivo `LICENSE` contém a proposta MIT para os materiais próprios, **sem comprovação da licença do código-base recebido**. Antes de declarar o repositório inteiro como MIT, verifique a origem/licença do HTML original. Artes de terceiros devem respeitar suas respectivas licenças.

## Repositório

https://github.com/WalneyNF/wmk-vida-loka


## Correções v1.3.1 (23/11/2026)

- Tela inicial redesenhada: menu cinematográfico responsivo, mapa em destaque e seleção de três regiões.
- Navegação verificada em navegador Chromium: jogar, retornar ao menu, abrir editor de mapas e missões.
- Registro de eventos mais tolerante a elementos opcionais ausentes, evitando que um botão removido interrompa toda a inicialização.
- **Se ainda aparecer o erro antigo**, recarregue com Ctrl+F5 e confirme que o endereço aponta ao `index.html` atualizado.
- Painéis de edição continuam exclusivos das opções do menu; o HUD permanece disponível durante o jogo.

**Limitações:** persistência em localStorage (por navegador/dispositivo), sprites importados precisam ser imagens PNG/JPG/WebP, não modelos 3D nativos. Os editores são experimentais, não substituem um motor profissional de jogos.