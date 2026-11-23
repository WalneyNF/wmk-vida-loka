# WMK Vida Loka v1.6.0 — Mundo aberto e World Studio

Jogo 2D top-down em HTML5 Canvas, com quatro mapas, missões, bots e editores de mapas, objetos e armas fictícias.

**Créditos das adaptações:** Walney Moreira Klein — walneyk@hotmail.com

## Executar
Baixe o ZIP em **Code → Download ZIP**, extraia os arquivos e abra `index.html` em Chrome ou Edge. Opcionalmente, use XAMPP/Live Server para servir por HTTP. Não há compilação nem dependências JS obrigatórias.

## Mapas
- **Baía Nova:** ruas, prédios, veículos e entregas.
- **Costa Dourada:** praia e marina.
- **Serra Brava:** interior e galpões.
- **Terminal Zero:** arena top-down com combate e bots.

Todos os mapas podem ser duplicados e editados no **World Studio**.

## Editores
| Ferramenta | Recursos |
|---|---|
| World Studio | Colocar objetos/sprites e bots, definir colisões e gizmos para G mover, S escalar objetos, R rotacionar objetos. Exportar/importar mapa JSON |
| Editor de Missões | Criar, editar, duplicar e excluir contratos, escolher mapas e configurar objetivos e recompensas W$ |
| Bot Lab | Equipe (inimigo/aliado/neutro), vida, comportamento, arma, dano, alcance, precisão, velocidade e pontos de patrulha |
| **Object Lab (novo)** | Biblioteca de modelos editáveis: tipo, dimensões, cor, camada, sprite e colisão |
| **Arsenal Lab (novo)** | Armas fictícias com nome, dano, alcance, cadência, capacidade e precisão |

### Inserir bot claramente identificado
1. Menu → **World Studio** → mapa.
2. Ferramenta → **♟ Inserir bot (escolher tipo)**.
3. Aparece uma janela com cartões **🔴 INIMIGO**, **🔵 ALIADO** ou **⚪ NEUTRO**, mostrando nome, comportamento, arma e HP.
4. Escolha o modelo e clique no mapa. O bot pode ser selecionado novamente pela lista lateral e movido com o gizmo.
5. Edite atributos avançados no **Bot Lab**.

### Criar modelo de objeto e inserir em mapas
1. Menu → **▣ EDITOR DE OBJETOS** → Novo.
2. Nome, tipo, largura/altura, rotação, camada, cor, sprite (opcional), colisão.
3. Salve; no World Studio escolha **▣ Objeto da biblioteca**, selecione o modelo e clique no mapa.
4. G/S/R para transformar. Instâncias já colocadas não se atualizam automaticamente após editar o modelo original.

### Criar arma fictícia
1. Menu → **⌖ EDITOR DE ARMAS** → Nova arma.
2. Configure dano, alcance, tiros/segundo, capacidade, precisão e nome.
3. No Bot Lab selecione a arma; **dano, alcance e precisão** são preenchidos como valores iniciais editáveis por bot.
4. A cadência do catálogo controla o intervalo entre tiros dos bots. A capacidade é armazenada, mas **a recarga dos bots ainda não foi implementada**. O jogador usa o equipamento padrão por enquanto.

## Comandos
**Jogo:** WASD, Shift correr, E entrar/sair de carro, Espaço freio, ESC menu. Arena: mouse mira, clique dispara, R recarrega.

**World Studio:** G mover, S escalar objeto, R girar objeto, Ctrl+Z desfazer, Ctrl+Y refazer, scroll zoom, botão direito panorâmica.

## JSON e backup
O jogo salva dados em `localStorage` quando disponível. Exportações: mapa, missões, bots, biblioteca de objetos (`wmk-vida-loka-prefabs`) e armas (`wmk-vida-loka-weapons`). **EXPORTAR PROJETO** inclui todos esses catálogos e sprites. Faça backups: limpar dados do navegador pode apagar progresso.

## Manuais e testes
- [Manual do jogador](manual-jogador.html)
- [Manual do desenvolvedor](manual-desenvolvedor.html)
- [Guia de evolução](evolucao.html)
- [Roadmap](roadmap.html)
- [Relatório de testes](testes/RELATORIO.md)

No Chromium headless, foram aprovados **39 testes gerais + 13 de gizmos + 19 dos novos editores = 71/71 verificações**. Os testes simulam `localStorage`. Persistência real em Windows, desempenho e browsers móveis ainda requerem validação.

## Licença
O arquivo `LICENSE` contém MIT para contribuições próprias. **A licença do protótipo HTML original ainda não foi comprovada; a distribuição do conjunto integral sob MIT depende dos direitos necessários.** Recursos de terceiros mantêm suas licenças. Não inclui arte proprietária de GTA ou Counter-Strike.

## Avatar Lab — personalização do personagem (v1.7)

Abra **◉ EDITOR DE AVATAR** no menu principal. Defina nome, corpo (regular, esbelto ou robusto), penteado (curto, comprido, sem cabelo), acessório de cabeça (nenhum, boné, capacete), mochila e cores de pele, camisa, calça, cabelo e acessórios. O painel direito apresenta uma prévia ampliada em Canvas.

Clique **Salvar avatar** para aplicar imediatamente ao personagem de todos os mapas. **Restaurar padrão** altera primeiro a prévia e exige confirmação em Salvar. **Exportar JSON** cria `wmk-avatar.json`; **Importar JSON** valida e carrega o modelo na prévia antes de salvar. O backup **Exportar Projeto** inclui a configuração do avatar, e Importar Projeto a restaura.

O avatar utiliza um desenho 2D vetorial simples. Não há ainda editor de pixel art, sprites animados, hitbox por tamanho corporal ou skins múltiplas. Os bots mantêm aparências independentes.

### Testes da v1.7

Passaram **12/12 verificações específicas** do Avatar Lab em Chromium usando `page.set_content` e armazenamento simulado. Foram exercitados prévia, alterações, salvar, exportar, restaurar, voltar ao menu e jogar; não equivale a validar persistência real entre sessões em Windows/HTTP.

Consulte [Manual do jogador](manual-jogador.html), [Manual do desenvolvedor](manual-desenvolvedor.html), [Guia de evolução](evolucao.html) e [Relatório de testes](testes/RELATORIO.md).
