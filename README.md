# Documentação do Jogo Pontos e Caixas

O Jogo dos Pontinhos (Dot and Boxes) é um jogo estratégico em que os jogadores alternam entre si para conectar pontos adjacentes no tabuleiro com linhas, formando quadrados. Cada vez que um jogador completa um quadrado, ele ganha um ponto. O objetivo é conquistar a maior quantidade de quadrados possível, bloqueando o adversário e evitando que ele faça o mesmo.

## Dependências

O jogo utiliza as seguintes bibliotecas:

- **time**: para controlar o tempo de exibição das mensagens.
- **copy**: para fazer cópias de objetos.
- **random**: para embaralhar a ordem de escolha dos quartos.
- **pygame**: para criar a interface gráfica do jogo.
- **numpy**: para criar e manipular vetores multidimensionais.
- **anytree**: para construir a árvore de estados do jogo.

## Classes

### Player

Representa um jogador no jogo.

**Atributos:**
- **id**: identificador do jogador (PLAYER ou CPU).
- **pontuacao**: pontuação do jogador.

**Métodos:**
- **aumentaPontuacao()**: incrementa a pontuação do jogador em 1.

### Quartos

Representa um quarto no tabuleiro.

**Atributos:**
- **id**: identificador do quarto.
- **L, T, R, B**: índices dos pontos que formam o quarto.
- **pos**: posição (coordenadas) do quarto no tabuleiro.
- **conquistador**: identificador do jogador que conquistou o quarto (-1 para nenhum jogador).

**Métodos:**
- **_verificaPosicao(indice)**: verifica se a linha correspondente ao índice já foi desenhada.
- **setLinha(direcao)**: faz a jogada no vetor que representa cada linha.
- **verificaQuarto(v_estado)**: verifica se o quarto foi completado.

## Funções

- **reinicia_jogo()**: reinicia os estados do jogo.
- **setEstado(states, state)**: habilita um estado específico do jogo.
- **setModo(mode, ind)**: habilita um modo de jogo (dificuldade máxima).
- **limpaTela(janela)**: limpa a tela com uma cor de fundo.
- **desenhaMsg(janela, x, y, mensagem, tamFont, cor, font=None)**: apresenta uma mensagem na tela.
- **desenhaHUD(janela, listPlayers, nJogadas)**: desenha os elementos da interface do jogo.
- **desenhaTabuleiro(janela, listaQuartos)**: desenha o tabuleiro do jogo.
- **desenhaSelecaoQuarto(janela, quarto, qrtAnterior)**: desenha a seleção do quarto.
- **desenhaMarcaPonto(janela, quarto, cor)**: desenha o quarto na cor correspondente ao jogador que obteve o ponto.
- **selecionaQuarto(listQrt, id)**: retorna o objeto Quartos correspondente ao ID fornecido.
- **getId(x_pos, y_pos)**: retorna o ID do quarto selecionado a partir das coordenadas do mouse.
- **marcaPonto(nJogadas, listaPlayers, lQuartos, vEstados)**: marca o ponto para o jogador correto.
- **criaFilhos(no_pai, dificuldade)**: cria os filhos de um nó na árvore de estados.
- **listarAncestrais(no)**: retorna uma lista com os nomes dos ancestrais de um nó.
- **miniMax(node, profundidade)**: aplica o algoritmo minimax na árvore de estados.
- **miniMax_Phoda(node, profundidade)**: aplica o algoritmo minimax com poda alfa-beta na árvore de estados.
