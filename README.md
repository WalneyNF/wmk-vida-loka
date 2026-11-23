

## v2.2.0 — World Studio: grupos e prefabs compostos

- **Ctrl/Shift+clique** na cena e Ctrl/Shift na lista permitem selecionar várias entidades.
- **Selecionar todos**, **Agrupar**, **Desagrupar** e **Duplicar seleção**.
- Objetos agrupados compartilham `groupId`, que é salvo no mapa JSON; arrastar desloca o grupo selecionado.
- **Salvar conjunto como prefab** guarda múltiplos objetos com coordenadas relativas. **Inserir conjunto** cria instâncias em outros mapas.
- Importação e exportação da biblioteca em formato `wmk-composite-prefabs`; os conjuntos também são armazenados localmente.
- Testes automatizados: 18/18 novos e 126/126 antigos, total **144/144** no Chromium por scripts de interação.

### Teste rápido

1. Menu → World Studio → duplique Terminal Zero.
2. Insira duas barreiras, selecione ambas com Ctrl+clique e pressione **Agrupar seleção**.
3. Arraste uma delas para mover ambas e pressione **Duplicar seleção**.
4. Selecione duas peças, use **Salvar conjunto como prefab** e dê um nome.
5. Mude de mapa, escolha o prefab e pressione **Inserir conjunto no mapa**.
6. Exporte **JSON do mapa** e **biblioteca de conjuntos JSON** para backup.

**Limitações:** hierarquia aninhada, escala/rotação coletiva, autotile/atlas, bloqueio de camadas e persistência após recarregar o navegador em HTTP/Windows não foram concluídos ou validados. O ZIP contém o teste completo e os manuais atualizados.

Consulte [Manual World Studio v2.2](manual-world-studio-v2.2.html).

# WMK Vida Loka v2.2.0 — Jogo e Estúdio de Criação 2D

**WMK Vida Loka** é um protótipo de mundo aberto 2D top-down em HTML5 Canvas, com quatro cenários iniciais, bots, missões, veículos, combate em arena e editores.

**Créditos das adaptações:** Walney Moreira Klein — walneyk@hotmail.com.

## Instalação e execução

1. Baixe em **Code → Download ZIP** e extraia todo o projeto, incluindo as pastas `assets/` e `js/`.
2. Inicie pela pasta do projeto com `py -m http.server 8000` ou use XAMPP.
3. Acesse `http://localhost:8000` no navegador.
4. Selecione Baía Nova, Costa Dourada, Serra Brava ou Terminal Zero e clique **Iniciar Jogo**.
5. Comandos principais: WASD, Shift, E e Espaço. Na arena, mouse para mirar/disparar, R para recarregar e Esc para voltar ao menu.

## Editores

| Editor | Funções |
|---|---|
| World Studio | Criar, editar e duplicar mapas, inserir objetos, bots, gizmos, sprites, colisões e patrulhas |
| Editor de Missões | Contratos, recompensas W$, mapas permitidos e condições de vitória |
| Bot Lab | Equipes, atributos, arma, comportamento, avatar e patrulhas |
| Object Lab | Prefabs, aparência, dimensões, colisões |
| Arsenal Lab | Catálogo de armas fictícias com atributos |
| Avatar Lab | Aparência e perfis de avatares |
| Game Creator | Exportar e importar pacotes JSON de conteúdo para o motor WMK |
| **Biblioteca & Diagnóstico (v2.1)** | Visualização centralizada de recursos, dependências quebradas e exportação de backup de auditoria |

## Novidades v2.1

- `js/wmk-core.js`: primeiro módulo JavaScript separado, responsável por inspeção de recursos e geração de cópias de auditoria.
- Biblioteca no menu principal, com contagem de mapas, missões, bots, objetos posicionados, prefabs, armas, avatares e sprites.
- Validação de IDs ausentes ou duplicados, além de referências a armas, avatares, sprites e mapas inexistentes.
- Navegação direta para os editores correspondentes e exportação JSON do inventário atual.
- Testes automatizados e guia HTML [Arquitetura v2.1](arquitetura-v2.1.html).

**Importante:** o backup `wmk-vida-loka-library` é **somente para auditoria**, não é aceito diretamente pelo importador de projeto. Para um backup restaurável, use **Exportar Projeto** no menu principal.

## Documentação

- [Manual do Jogador](manual-jogador.html)
- [Manual do Desenvolvedor](manual-desenvolvedor.html)
- [Arquitetura e biblioteca v2.1](arquitetura-v2.1.html)
- [Guia de evolução](evolucao.html)
- [Roadmap](roadmap.html)
- [Relatório de testes](testes/RELATORIO.md)
- [Pesquisa](pesquisa.html)

## Testes

As sete suítes de regressão executadas somaram **126/126 verificações aprovadas** no Chromium headless. A navegação direta via HTTP e `file://` foi bloqueada no ambiente de validação, portanto o carregamento real pelo servidor e a persistência após reiniciar o navegador ainda devem ser conferidos no Windows. Veja o relatório.

## Limitações

O projeto ainda concentra parte considerável da lógica em `index.html`: a migração modular é incremental. Não há multiplayer, exportação independente de HTML executável, nem editor de missão ramificado ou animação completa de personagens. O armazenamento local pode esgotar, especialmente com sprites. Faça backups regularmente.

## Licença e autoria

Há um arquivo `LICENSE` com texto MIT. **A licença do código-base original precisa ser confirmada antes de afirmar que toda a obra pode ser redistribuída como MIT.** Assets de terceiros conservam licenças próprias. Créditos das alterações: **Walney Moreira Klein — walneyk@hotmail.com**.

Projeto: https://github.com/WalneyNF/wmk-vida-loka
