# 🚘 WMK Vida Loka — World Studio (v1.3.0)

**Mundo aberto 2D, com mapas personalizáveis e missões criadas pela comunidade.** Desenvolvido em HTML, CSS e JavaScript (Canvas 2D), com foco em computadores modestos. Este projeto é inspirado no **gênero** de jogos urbanos de mundo aberto; não é GTA, não utiliza sua marca e não pretende reproduzir seus mapas, personagens ou conteúdo.

**Adaptação, desenvolvimento WMK e documentação:** Walney Moreira Klein — **walneyk@hotmail.com**.

> **Estado:** protótipo em evolução. Os três mapas, editor 2D, editor de contratos e importação de sprites demonstram os fluxos; não representam ainda um motor profissional completo. Consulte [limitações](#-limitações-conhecidas) e [roadmap](roadmap.html).

## 📌 Índice

1. [Iniciar](#-como-instalar-e-jogar)
2. [Menus e modos](#-menu-principal-e-modos)
3. [Mapas disponíveis](#-três-mapas-iniciais)
4. [Controles](#-controles)
5. [Editor de mapas](#-editor-de-mapas-world-studio)
6. [Criar e importar objetos](#-objetos-e-assets-externos)
7. [Colisões](#-colisões)
8. [Editor de missões](#-editor-de-missões)
9. [Salvar, importar e exportar JSON](#-salvamento-e-compartilhamento)
10. [Desenvolvimento](#-para-desenvolvedores)
11. [Licenças](#-licença-e-direitos)
12. [Manuais](#-manuais-e-documentação)

## 📦 Download do código-fonte completo

**Baixar ZIP diretamente do GitHub:** abra [Download ZIP da branch main](https://github.com/WalneyNF/wmk-vida-loka/archive/refs/heads/main.zip) ou clique em **Code → Download ZIP** na página do repositório. Esse pacote inclui o código-fonte e a documentação que estiverem publicados na branch principal.

**Instalação:** descompacte o arquivo, abra a pasta `wmk-vida-loka-main` e execute `index.html` no navegador. Para testar com servidor local, execute `py -m http.server 8000` dentro da pasta e acesse `http://localhost:8000/`.

**Atenção:** esse é o código-fonte, não um instalador do Windows. A versão do ZIP do GitHub acompanha os commits; arquivos criados ou salvos pelo editor dentro do navegador precisam ser exportados separadamente em JSON.

## 🚀 Como instalar e jogar

**Opção A, sem instalar nada:** baixe o repositório em **Code → Download ZIP**, descompacte e abra `index.html` em um navegador moderno. Mantenha as pastas e os arquivos juntos.

**Opção B, servidor local (recomendado):** no terminal dentro da pasta do projeto, execute:

```powershell
py -m http.server 8000
```

Acesse **http://localhost:8000/**. Para interromper o servidor pressione **Ctrl+C**. Python é necessário apenas para esta alternativa; a lógica do jogo roda no navegador. O projeto não exige banco de dados ou chave de API.

## 🏠 Menu principal e modos

O **menu principal** reúne **Jogar**, **Selecionar Mapa**, **Editor de Mapas** e **Editor de Missões**. Os editores são ferramentas de criação, não painéis permanentes durante a partida. Dentro do jogo, **Esc** retorna ao menu.

1. Escolha um cenário na lista.
2. Clique em **Jogar** para iniciar a cidade escolhida.
3. Para personalizar a cidade, volte ao menu e abra **Editor de Mapas**.
4. Para criar contratos, volte ao menu e abra **Editor de Missões**.
5. Exporte o projeto JSON quando quiser compartilhar ou fazer backup.

## 🌍 Três mapas iniciais

| Mapa | ID | Ambientação | Ideias de gameplay |
| --- | --- | --- | --- |
| **Baía Nova** | `baia-nova` | Metrópole original, quadras, avenidas e prédios | Entregas, perseguições, trânsito urbano |
| **Costa Dourada** | `costa-dourada` | Praia, mar, píer e palmeiras | Turismo, entregas costeiras, corridas |
| **Serra Brava** | `serra-brava` | Campo, bosques, galpões | Resgate rural, exploração e desafios de direção |

Os mapas extras são **demonstrações no motor 2D**, não recriações de cidades reais. Os mapas fornecidos inicialmente são protegidos contra exclusão direta: **duplique** para criar uma variante sua. Os mapas criados e salvos ficam disponíveis no seletor do menu, no mesmo navegador.

## 🎮 Controles

| Tecla | Jogando | Editor de mapas |
| --- | --- | --- |
| W/A/S/D ou setas | Andar/dirigir | — |
| Shift | Correr a pé | — |
| E | Entrar/sair do carro próximo | — |
| Espaço | Freio de mão | — |
| Esc | Menu principal | — |
| Clique esquerdo | — | Inserir/selecionar |
| Arrastar | — | Reposicionar objeto |
| Roda do mouse | — | Zoom |
| Arrastar com botão direito | — | Pan da câmera |
| Delete | — | Remover objeto selecionado |

As teclas podem variar conforme o foco de um campo no editor. Não digite comandos de jogo enquanto um campo de texto estiver selecionado.

## 🗺 Editor de Mapas (World Studio)

**Objetivo:** permitir que qualquer pessoa crie um mundo próprio sem modificar o código-fonte.

### Primeiro mapa do zero

1. Menu principal → **Editor de Mapas**.
2. Crie um mapa novo ou **duplique** um dos três exemplos.
3. Defina nome e características disponíveis no painel.
4. Escolha um tipo de objeto, como prédio, árvore, água, areia ou barreira.
5. Clique no terreno para posicioná-lo.
6. Selecione o objeto e configure **X/Y, largura, altura, rotação, cor, camada e colisão**.
7. Ajuste a posição inicial do personagem.
8. **Salve**, volte ao menu e selecione seu mapa para testá-lo.
9. Exporte o JSON para compartilhar.

### Organização dos objetos

Cada objeto pertence ao mapa e possui propriedades editáveis. Use camadas para controlar a composição visual. A posição X/Y corresponde às coordenadas do mundo 2D, não latitude/longitude. O projeto não é um sistema GIS e o editor não possui ainda malha 3D, terreno de altura ou iluminação física.

**Ferramentas presentes:** seleção, inserção, arraste, transformações simples, sprites, colisão configurável, cópia por duplicação de mapa, salvamento local e exportação/importação. **Não disponíveis ainda:** seleção múltipla, histórico Undo/Redo, edição viária em nós, tilemap avançado, materiais PBR ou scripts arbitrários por objeto.

## 🎨 Objetos e assets externos

### Importar imagem PNG/JPG/WebP

1. Baixe ou produza uma imagem **2D**, preferencialmente PNG com transparência.
2. Entre no **Editor de Mapas** e use **Importar PNG/JPG/WebP**.
3. Selecione a imagem no computador (limite inicial aproximado: **750 KB por imagem**).
4. Escolha a ferramenta **Sprite importado**.
5. Clique no mapa para posicioná-lo.
6. Configure tamanho, rotação, camada e colisão conforme o objeto.
7. Salve e exporte o projeto JSON para não perder seu conteúdo.

**Exemplo:** sprite de um quiosque; posicione no calçadão, marque colisão para impedir que o personagem atravesse sua área e coloque uma missão de coleta perto dele.

### Assets Kenney

Veja [Kenney Assets](https://kenney.nl/assets) e [RPG Urban Kit](https://kenney-assets.itch.io/rpg-urban-kit). **Importante:** verifique a licença do pacote individual antes de redistribuir arquivos. Kits 3D como o Car Kit **não entram diretamente** no Canvas 2D: primeiro gere uma renderização em imagem (sprite top-down) em um programa 3D. **GLB/GLTF/OBJ não são importados diretamente na versão atual.**

**Boa prática:** mantenha o sprite original com transparência, use proporções compatíveis com a câmera superior e teste a área de colisão separadamente do desenho. Não copie imagens protegidas de jogos comerciais.

## 🧱 Colisões

Ao selecionar um objeto no World Studio, habilite **colisão** quando ele deve bloquear deslocamento (prédios, barreiras, rochas). Desabilite para decoração (marcas no chão, sombras, alguns detalhes). As colisões atuais são **aproximadas por retângulos/volumes simples em 2D**: rotação e formato visual irregular não implicam uma malha de colisão exata.

**Teste sugerido:** insira uma barreira, ative colisão, salve, entre no mapa e tente atravessá-la a pé e de carro. Depois desligue a colisão e repita. Se a aparência e a física divergirem, ajuste a posição e as dimensões do objeto.

## 📜 Editor de Missões

Menu principal → **Editor de Missões**. Você pode **criar, selecionar, editar, salvar, excluir, testar, importar e exportar contratos**, dependendo das opções disponíveis no painel. A missão armazena nome, descrição, tipo/modo, recompensa **W$**, checkpoints e filtro de mapas.

### Como criar uma missão

1. Entre no editor e use **Nova missão**.
2. Informe o nome: *Entrega do Píer*, por exemplo.
3. Escolha o tipo/modo implementado, descrição e recompensa (ex.: **W$ 350**).
4. Defina os pontos de objetivo nas coordenadas **X/Y**.
5. Em **Mapas permitidos**, informe `costa-dourada` para restringir essa missão à praia.
6. Salve; use a opção de **testar**; confira se os marcadores aparecem em locais acessíveis.
7. Exporte JSON para distribuir seu catálogo.

### Missão para vários mapas

O campo **Mapas permitidos** aceita IDs separados por vírgulas: `baia-nova, serra-brava`. **Vazio significa todos os mapas**. Verifique sempre as coordenadas nos cenários selecionados, porque as mesmas posições podem cair dentro de prédios, água ou outros obstáculos em mapas diferentes.

As missões iniciais incluem coleta, deslocamento/checkpoints e fuga simplificada. **Não existe ainda um sistema completo de eventos cinematográficos, falas de NPC, árvores de diálogo, inventário ou scripts customizados.** O editor trabalha com dados declarativos, não executa JavaScript recebido por JSON.

## 💾 Salvamento e compartilhamento

- **Salvamento local:** dados de mapas/missões e assets ficam no `localStorage` deste navegador/perfil.
- **Exportar mapa:** gera JSON do cenário selecionado.
- **Exportar projeto completo:** inclui mapas, missões e biblioteca de imagens, conforme recursos disponíveis.
- **Importar:** recebe arquivos JSON do **formato WMK**, não qualquer estrutura JSON de outro editor.
- **Atenção:** a importação completa pode **substituir dados existentes**, após confirmação; faça exportação de backup primeiro.
- **Não sincroniza dispositivos:** para usar em outro PC ou navegador, exporte e importe o projeto.
- **Imagens em Data URL:** o armazenamento do navegador tem limite; sprites grandes podem esgotá-lo.

### Exemplo ilustrativo de objeto JSON

```json
{
  "id": "quiosque-01",
  "type": "sprite",
  "x": 560,
  "y": 420,
  "w": 90,
  "h": 70,
  "rotation": 0,
  "layer": 2,
  "collision": true
}
```

**Este fragmento é didático, não um arquivo importável completo.** O formato efetivamente aceito pelo programa deve ser obtido em **Exportar JSON**, pois é validado pelo código.

## 🛠 Para desenvolvedores

### Estrutura

```text
wmk-vida-loka/
├── index.html                   # Jogo, interface e World Studio
├── assets/
│   └── logo.svg                # Identidade visual
├── README.md                   # Visão geral e tutoriais
├── manual-jogador.html         # Passo a passo do jogador/criador
├── manual-desenvolvedor.html   # Arquitetura e extensões
├── pesquisa.html               # Referências do gênero e assets
├── roadmap.html                # Plano visual
├── ROADMAP.md                  # Backlog em Markdown
└── LICENSE                     # Consulte a seção de direitos
```

### Arquitetura atual e evolução

O projeto ainda concentra boa parte dos sistemas em `index.html`. O Canvas desenha os mapas e o jogo; estruturas JS mantêm estados de jogador, veículos, missões, câmera e dados do editor. O World Studio trabalha com JSON declarativo e persistência no navegador. A recomendação para evolução é separar módulos: `core/`, `world/`, `entities/`, `physics/`, `missions/`, `editor/`, `ui/`, `assets/`.

**Para adicionar uma categoria de objeto:** defina a representação serializável, implementação do desenho, propriedades editáveis, comportamento de colisão, validação de entrada e compatibilidade com export/import. **Para adicionar um tipo de missão:** defina contrato de dados, condição de início, progresso, conclusão/falha, renderização do objetivo, seleção de mapas e testes. Evite `eval` e execução de código importado.

**Testes mínimos:** navegue pelos três mapas, entre e saia de um carro, teste colisão, crie e exclua mapa do usuário, teste missão em um mapa e em todos, exporte/importe backup e recarregue a página.

**Desempenho:** mantenha sprites pequenos, limite elementos simultâneos, desenhe apenas o que está visível, evite alocar objetos a cada frame e considere particionamento espacial quando crescer a cidade. Futuras melhorias devem incluir testes automatizados, versionamento de schemas e migração do armazenamento para IndexedDB.

## ⚠ Limitações conhecidas

A v1.3.0 é uma base experimental: **não** possui tráfego urbano autônomo completo, multidões/NPCs complexos, editor completo de ruas, física realista, undo/redo, multiplayer, conversão automática de modelos 3D ou mapas gigantes com streaming. Os três mapas demonstram cenários diferentes dentro das limitações atuais do Canvas. O funcionamento visual de todas as ferramentas precisa de testes no navegador de destino.

## 📖 Manuais e documentação

| Documento | Conteúdo |
| --- | --- |
| [Manual do jogador](manual-jogador.html) | Jogar, escolher mapa, editor de missões e mapas, importar imagens, backup |
| [Manual do desenvolvedor](manual-desenvolvedor.html) | Estrutura, objetos, colisões, JSON, extensibilidade, validação, limites |
| [Pesquisa](pesquisa.html) | Referências de jogos do gênero, diferenças e Kenney |
| [Roadmap visual](roadmap.html) | Etapas de evolução |
| [ROADMAP.md](ROADMAP.md) | Backlog técnico |

## 📜 Licença e direitos

O objetivo é disponibilizar a **contribuição original WMK** sob os termos da **licença MIT**. Porém, o arquivo original do jogo foi fornecido sem informação suficiente de autoria/licenciamento. **A presença de um arquivo `LICENSE` não comprova que todo o código-base pode ser relicenciado.** Antes de afirmar que o repositório inteiro é MIT, verifique e documente a licença de origem; preserve os avisos exigidos. Assets externos mantêm suas próprias licenças, mesmo quando usados em um projeto MIT. GTA, GTA V e GTA VI são referências de gênero, não marcas ou recursos deste projeto.

## 🔗 Repositório e contato

**Código:** https://github.com/WalneyNF/wmk-vida-loka

**Autor das modificações/documentação:** Walney Moreira Klein — **walneyk@hotmail.com**

Contribuições são bem-vindas: descreva a alteração, seu objetivo, como testar e a procedência/licença de novos assets.
