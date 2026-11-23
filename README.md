# WMK Vida Loka v2.4.0 — Jogo e estúdio de criação 2D

**WMK Vida Loka** é um protótipo de mundo aberto 2D top-down com quatro mapas iniciais, bots, missões, veículos, combate em arena e ferramentas de edição.

**Créditos das adaptações:** Walney Moreira Klein — walneyk@hotmail.com.

## Novidades da v2.4.0

- **Seleção por retângulo**: use a ferramenta Selecionar/mover e arraste a partir do chão vazio; Ctrl ou Shift adiciona objetos e bots à seleção.
- **Grupos superiores**: selecione dois grupos e use Criar grupo superior da seleção; a hierarquia pai/filhos é salva no JSON do mapa.
- **Presets de terreno**: grama, asfalto, areia, água, pedra e terra; são blocos coloridos e editáveis, não um atlas com autotile.
- **Propriedades compactas**: seções recolhíveis para posição, dimensões, colisão e camada.
- **Compatibilidade**: mantém os mapas antigos; novas propriedades opcionais `groupParents` e `tilePreset`.
- **Validação**: 183/183 verificações em Chromium. Persistência após reiniciar o navegador Windows via HTTP continua pendente.

Manual: [World Studio 2.4](manual-world-studio-v2.4.html).

## Como jogar

1. Faça o download do ZIP ou use **Code → Download ZIP** no GitHub.
2. Extraia a pasta preservando `index.html`, `assets/` e `js/`.
3. Recomenda-se iniciar por HTTP local: `py -m http.server 8000` na pasta do projeto; então abrir `http://localhost:8000`.
4. Selecione Baía Nova, Costa Dourada, Serra Brava ou Terminal Zero e clique em **Iniciar Jogo**.
5. Use WASD, Shift, E e Espaço. No Terminal Zero, mire/dispare com o mouse e recarregue com R. Pressione Esc para retornar ao menu.

## Editores disponíveis

| Editor | Função |
|---|---|
| World Studio | Mapas, objetos posicionados, gizmos, sprites importados, colisões, cópia de mapas e rotas de patrulha |
| Bot Lab | Equipe, arma, vida, dano, precisão, alcance, comportamento e avatar |
| Object Lab | Prefabs compartilhados, dimensões, aparência e colisão |
| Arsenal Lab | Armas fictícias configuradas em catálogo JSON |
| Avatar Lab | Aparência e perfis reutilizáveis |
| Editor de Missões | Contratos, mapas permitidos, marcadores, tipos e recompensas |
| Game Creator | Exportar/importar pacotes de mapas e missões compatíveis com o motor WMK |
| **Biblioteca & Diagnóstico — novo** | Contar recursos, consultar IDs, navegar para os editores, detectar referências quebradas e exportar backup de auditoria |

## Novidades v2.3.0 — Hierarquia, camadas e transformação coletiva

- **Hierarquia visual** no World Studio: grupos, seus membros e bots; clique para selecionar o grupo ou uma peça, Ctrl/Shift para agregar.
- **Camadas por número (-20 a 20)** com botões 👁/◌ para ocultar na visualização do editor e 🔒/🔓 para bloquear manipulação. Configurações em `map.layerSettings`, mantidas ao salvar/exportar/importar JSON.
- **Gizmos coletivos**: com dois ou mais objetos selecionados, G move, S redimensiona proporcionalmente e R gira posições e ângulos. Bots participam das transformações de posição, mas não têm tamanho ou rotação visual editáveis nesta etapa.
- **Pivô** no centro da seleção ou no objeto ativo. `Ctrl+Z` / `Ctrl+Y` desfazem/refazem transformações e mudanças nas camadas.
- **Compatibilidade**: mapas antigos sem `layerSettings` recebem camadas visíveis e desbloqueadas por padrão. O bloqueio/ocultação é uma ferramenta **do editor**, não remove objetos da física do jogo publicado.
- **Manual específico**: [`manual-world-studio-v2.3.html`](manual-world-studio-v2.3.html). Testes: `testes/test_v23.py`.

### Exemplo de configuração JSON

```json
{"id":"meu-mapa","layerSettings":{"1":{"visible":true,"locked":true},"-2":{"visible":false,"locked":false}}}
```

## Novidades v2.2.0 — World Studio: grupos e prefabs compostos

- **Ctrl+clique** ou **Shift+clique** adiciona/remove entidades da seleção no mapa. No painel à direita, a lista suporta seleção múltipla com Ctrl/Shift.
- **Selecionar todos**, **Agrupar seleção**, **Desagrupar** e **Duplicar seleção** disponíveis no painel esquerdo.
- Grupos de objetos usam `groupId`; clicar em uma peça do grupo seleciona suas peças. Ao arrastar, a seleção se desloca em conjunto.
- **Salvar conjunto como prefab** captura dois ou mais objetos, com coordenadas relativas ao centro do grupo; o botão **Inserir conjunto no mapa** posiciona a composição perto do spawn, com novo ID de grupo.
- **Exportar/Importar biblioteca de conjuntos JSON** (`wmk-composite-prefabs`) para copiar composições entre navegadores e computadores.
- Persistência `groupId` incluída na sanitização, duplicação e importação/exportação de mapas JSON.
- Histórico básico de desfazer/refazer foi preservado; os conjuntos persistem no armazenamento local separadamente dos mapas. **Exporte a biblioteca de conjuntos como backup adicional.**
- `manual-world-studio-v2.2.html` e teste `testes/test_v22.py` (18 verificações).

### Tutorial rápido: criar uma garagem como prefab composto

1. Menu principal → World Studio → selecione um mapa ou duplique-o.
2. Crie pelo menos dois objetos, como um prédio e uma barreira.
3. Escolha **Selecionar/mover**, segure Ctrl e clique em cada objeto (ou use a lista múltipla).
4. Pressione **Agrupar seleção**. Arraste uma peça para mover as selecionadas juntas.
5. Clique em **Salvar conjunto como prefab**, digite um nome e salve.
6. Abra outro mapa, selecione o conjunto no campo **Prefabs compostos** e clique em **Inserir conjunto no mapa**.
7. Faça alterações e salve o mapa; exporte tanto o **JSON do mapa** quanto a **biblioteca de conjuntos**.

**Limitações honestas:** não há ainda árvore hierárquica aninhada, transformações múltiplas de escala/rotação, grupos com pivô próprio, nem tileset/atlas com autotile. A escala e rotação por gizmo continuam aplicadas à entidade primária. O armazenamento local não substitui um backup exportado.

## Novidades v2.3.0

- Núcleo independente `js/wmk-core.js` para inspecionar recursos compartilhados.
- Painel **Biblioteca & Diagnóstico**, acessível exclusivamente pelo menu principal.
- Detecção de IDs duplicados e ausentes, sprites inexistentes nos mapas, armas e avatares ausentes nos bots, mapas não encontrados nas missões.
- Visão centralizada das quantidades de mapas, missões, bots, instâncias, prefabs, armas, avatares e sprites.
- Exportação JSON de snapshot da biblioteca (`wmk-vida-loka-library`). **Este formato é de auditoria e não é restaurável diretamente pelos importadores existentes.** Use **Exportar Projeto** para backup restaurável.
- Novo tutorial [Arquitetura v2.1](arquitetura-v2.1.html) e suíte `testes/test_v21.py`.

## Como testar

Instale Python 3 e Playwright para executar os scripts, além do Chromium disponível no ambiente:

```powershell
py -m pip install playwright
py testes/test_smoke.py
py testes/test_v20.py
py testes/test_v21.py
```

Os testes de interface podem requerer ajuste do caminho do Chromium no Windows. O relatório de execução está em [testes/RELATORIO.md](testes/RELATORIO.md). Testes com navegação HTTP e recuperação real após reinício permanecem pendentes, pois o navegador de validação disponível bloqueou navegação HTTP e `file://` neste ambiente.

## Documentação em português

- [Manual do Jogador](manual-jogador.html)
- [Manual do Desenvolvedor](manual-desenvolvedor.html)
- [Guia da Arquitetura v2.1](arquitetura-v2.1.html)
- [Guia de Evolução](evolucao.html)
- [Roadmap Visual](roadmap.html)
- [Pesquisa de referências](pesquisa.html)

## Organização

```text
index.html                 Interface e jogo atual
js/wmk-core.js             Núcleo independente de diagnóstico
assets/                    Identidade visual
exemplos/                  Exemplos de dados JSON
testes/                    Testes Playwright e relatório
*.html                     Manuais e documentação
LICENSE                    Proposta de licença MIT
```

## Limitações conhecidas

O núcleo compartilhado é um **primeiro módulo**: o motor e vários editores ainda estão integrados em `index.html`, para reduzir risco de regressão. A biblioteca é um painel de consulta e auditoria, não edita dados diretamente. Não há multiplayer, exportação de executável, árvore de comportamento avançada ou animações completas. Salvamento local depende do navegador e possui limite de tamanho; faça backups do projeto regularmente.

## Direitos autorais e licença

Este repositório contém um arquivo `LICENSE` MIT. **A aplicação da MIT ao código-base inicial depende de confirmar sua origem e permissões; não se pode relicenciar automaticamente código de terceiros.** Recursos importados (inclusive Kenney) conservam suas próprias licenças. Não considere a presença do arquivo MIT prova de que todos os ativos e código-base são livres para redistribuição.

Repositório: https://github.com/WalneyNF/wmk-vida-loka