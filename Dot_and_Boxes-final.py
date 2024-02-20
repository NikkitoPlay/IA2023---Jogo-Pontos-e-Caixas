import time
import copy
import random
import pygame
import numpy as np
from anytree import Node, RenderTree, PreOrderIter
#implementar busca informada, dist do ponto 5
#minimax ta erradooo
#o no da raiz é a jogada da cpu, nao do player...
class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.pontuacao = 0
    
    def aumentaPontuacao(self):
        self.pontuacao += 1

class Quartos: ##problema
    def __init__(self, id, l, t, r, b, pos) -> None:
        self.id = id

        self.L = l
        self.T = t
        self.R = r
        self.B = b
        self.pos = pos
        self.conquistador = -1

    def _verificaPosicao(self, indice) -> bool: #verifica se a linha já foi desenhada
        if linhas[0][indice] != 0:
            return False
        else:
            return True

    def setLinha(self, direcao) -> bool:
        if direcao == LEFT and self._verificaPosicao(self.L):
            linhas[0][self.L] = 1
            return True
        elif direcao == TOP and self._verificaPosicao(self.T):
            linhas[0][self.T] = 1
            return True
        elif direcao == RIGHT and self._verificaPosicao(self.R):
            linhas[0][self.R] = 1
            return True
        elif direcao == BOTTOM and self._verificaPosicao(self.B):
            linhas[0][self.B] = 1
            return True
        else:
            desenhaMsg(janela, 400, 90, "Jogada inválida!", 30, (255,255,0))
            return False

    def verificaQuarto(self, v_estado) -> bool :#verifica se o quarto atual foi completado      
        if v_estado[self.L] and v_estado[self.T] and v_estado[self.R] and v_estado[self.B]:
           return True

#funcoes
def reinicia_jogo():
    global linhas, nJogadas, level, level_escolhido, player, cpu, listPlayers, quarto, qrtAnterior
    linhas = np.zeros((1, 24))      #um vetor que representa as linhas que liga os pontinhos estão ligadas ou desligadas
    nJogadas = 0                    #representa o número de jogadas já feitas, tem muita importancia para o jogo
    level = 2
    player = Player(PLAYER)
    cpu = Player(CPU)
    listPlayers = [player, cpu]
    quarto = None
    qrtAnterior = None

def setEstado(states, state):
    for pos in range(len(states)):
        states[pos] = 0
    states[state] = 1

def setModo(mode, ind):
    for pos in range(len(mode)):
        mode[pos] = 0
    mode[ind] = 1

def limpaTela(janela):
    janela.fill(cor_fundo)
    pygame.display.flip()
    time.sleep(0.2)

def desenhaMsg(janela, x, y, mensagem, tamFont, cor, font=None): # apresenta uma mensagem na posicao x,y def desenhaMsg(janela, x, y, mensagem, tamFont, cor, estilo_fonte)
    fonte = pygame.font.SysFont(font, tamFont)
    texto = fonte.render(mensagem, True, cor)
    posicaoTexto = texto.get_rect()
    padding = 10  # Define a quantidade de padding ao redor do texto
    posicaoTexto.inflate_ip(padding, padding)
    posicaoTexto.centerx = x
    posicaoTexto.centery = y
    pygame.draw.rect(janela, cor_fundo, posicaoTexto)
    janela.blit(texto, posicaoTexto)

def desenhaHUD(janela, listPlayers, nJogadas):
    pygame.draw.rect(janela, cor_fundo, (0, 20, 800, 50))
    pygame.draw.rect(janela, cor_fundo, (0, 730, 800, 50))   
    if modo_jogo[0]:
        desenhaMsg(janela, 400, 700, "PLAYER VS CPU", 20, (255, 255, 0))
        desenhaMsg(janela, 400, 720, "PLAYER VS PLAYER", 20, (255, 255, 255)) 
        desenhaMsg(janela, 235, 750, "PLAYER: {}".format(listPlayers[0].pontuacao), 39, (255, 255, 255))
        desenhaMsg(janela, 550, 750, "CPU: {}".format(listPlayers[1].pontuacao), 39, (255, 255, 255))
    if modo_jogo[1]:
        if nJogadas == 0:
            desenhaMsg(janela, 400, 40, "Turno do PLAYER 1", 39, (255, 255, 255))
        if nJogadas % 2 == 0:
            desenhaMsg(janela, 400, 40, "Turno do PLAYER 1", 39, (255, 255, 255))
        else:
            desenhaMsg(janela, 400, 40, "Turno do PLAYER 2",39, (255, 255, 255))
        desenhaMsg(janela, 400, 700, "PLAYER VS CPU", 20, (255, 255, 255))  
        desenhaMsg(janela, 400, 720, "PLAYER VS PLAYER", 20, (255, 255, 0)) 
        desenhaMsg(janela, 235, 750, "PLAYER 1: {}".format(listPlayers[0].pontuacao), 39, (255, 255, 255))
        desenhaMsg(janela, 550, 750, "PLAYER 2: {}".format(listPlayers[1].pontuacao), 39, (255, 255, 255)) 
    #desenhaMsg(janela, 400, 740, "F2", 15, (56,155,219)) 
def desenhaTabuleiro(janela, listaQuartos):
    dim = 160
    for j in range (1, 5):
        for i in range(1, 5):
            pygame.draw.circle(janela, (251, 162, 23), (i*dim, j*dim), 5)
    if linhas[0][0]:
        pygame.draw.line(janela, (251, 162, 23), (160, 160), (160, 320), 2)
    if linhas[0][1]:
        pygame.draw.line(janela, (251, 162, 23), (160, 160), (320, 160), 2)
    if linhas[0][2]:
        pygame.draw.line(janela, (251, 162, 23), (320, 160), (320, 320), 2)
    if linhas[0][3]:
        pygame.draw.line(janela, (251, 162, 23), (320, 160), (480, 160), 2)
    if linhas[0][4]:
        pygame.draw.line(janela, (251, 162, 23), (480, 160), (480, 320), 2)
    if linhas[0][5]:
        pygame.draw.line(janela, (251, 162, 23), (480, 160), (640, 160), 2)
    if linhas[0][6]:
        pygame.draw.line(janela, (251, 162, 23), (640, 160), (640, 320), 2)
    if linhas[0][7]:
        pygame.draw.line(janela, (251, 162, 23), (640, 320), (480, 320), 2)
    if linhas[0][8]:
        pygame.draw.line(janela, (251, 162, 23), (640, 320), (640, 480), 2)
    if linhas[0][9]:
        pygame.draw.line(janela, (251, 162, 23), (480, 320), (320, 320), 2)
    if linhas[0][10]:
        pygame.draw.line(janela, (251, 162, 23), (480, 320), (480, 480), 2)
    if linhas[0][11]:
        pygame.draw.line(janela, (251, 162, 23), (320, 320), (160, 320), 2)
    if linhas[0][12]:
        pygame.draw.line(janela, (251, 162, 23), (320, 320), (320, 480), 2)
    if linhas[0][13]:
        pygame.draw.line(janela, (251, 162, 23), (320, 480), (160, 480), 2)
    if linhas[0][14]:
        pygame.draw.line(janela, (251, 162, 23), (160, 480), (160, 320), 2)
    if linhas[0][15]:
        pygame.draw.line(janela, (251, 162, 23), (480, 480), (320, 480), 2)
    if linhas[0][16]:
        pygame.draw.line(janela, (251, 162, 23), (160, 480), (160, 640), 2)
    if linhas[0][17]:
        pygame.draw.line(janela, (251, 162, 23), (640, 480), (480, 480), 2)
    if linhas[0][18]:
        pygame.draw.line(janela, (251, 162, 23), (320, 480), (320, 640), 2)
    if linhas[0][19]:
        pygame.draw.line(janela, (251, 162, 23), (640, 640), (480, 640), 2)
    if linhas[0][20]:
        pygame.draw.line(janela, (251, 162, 23), (480, 480), (480, 640), 2)
    if linhas[0][21]:
        pygame.draw.line(janela, (251, 162, 23), (320, 640), (480, 640), 2)
    if linhas[0][22]:
        pygame.draw.line(janela, (251, 162, 23), (640, 480), (640, 640), 2)
    if linhas[0][23]:
        pygame.draw.line(janela, (251, 162, 23), (160, 640), (320, 640), 2)
    for qrt in listaQuartos:
        if qrt.verificaQuarto(linhas[0]):
            if qrt.conquistador == 1:
                cor_quarto = (205,133,63)# cpu
            if qrt.conquistador == 0:
                cor_quarto = (56,155,219) # player
            desenhaMarcaPonto(janela, qrt, cor_quarto)

def desenhaSelecaoQuarto(janela, quarto, qrtAnterior):
    if qrtAnterior is not None:
        superficie = pygame.Surface((160, 160), pygame.SRCALPHA)
        cor = (94, 10, 11) 
        pygame.draw.rect(superficie, cor, (10, 10, 140, 140))
        janela.blit(superficie, qrtAnterior.pos)    
    
    superficie = pygame.Surface((160, 160), pygame.SRCALPHA)
    cor_transparente = (148, 26, 28, 128)  # RGBA, onde 128 define a transparência (0 é totalmente transparente, 255 é opaco)
    pygame.draw.rect(superficie, cor_transparente, (10, 10, 140, 140))
    janela.blit(superficie, quarto.pos)

def desenhaMarcaPonto(janela, quarto, cor):
    superficie = pygame.Surface((160, 160), pygame.SRCALPHA)
    pygame.draw.rect(superficie, cor, (10, 10, 140, 140))
    janela.blit(superficie, quarto.pos)
    
def selecionaQuarto(listQrt, id) -> Quartos:
    for qrt in listQrt:
        if qrt.id == id:
            return qrt

def getId(x_pos, y_pos) -> int:
            if y_pos >= 160 and y_pos < 320: #primeira linha de quartos
                if x_pos >= 160 and x_pos < 320:#primeiro quarto
                    return 1
                elif x_pos >= 320 and x_pos < 480:#segundo quarto
                    return 2
                elif x_pos >= 480 and x_pos < 640:#terceiro quarto
                    return 3
            elif y_pos >= 320 and y_pos < 480: #segunda linha de quartos
                if x_pos >= 160 and x_pos < 320:
                    return 4
                elif x_pos >= 320 and x_pos < 480: 
                    return 5
                elif x_pos >= 480 and x_pos < 640:
                    return 6
            elif y_pos >= 480 and y_pos < 640: #terceira linha de quartos
                if x_pos >= 160 and x_pos < 320:
                    return 7
                elif x_pos >= 320 and x_pos < 480: 
                    return 8
                elif x_pos >= 480 and x_pos < 640:
                    return 9
            else:
                return 0

def marcaPonto(nJogadas, listaPlayers, lQuartos, vEstados): 
    for quarto in lQuartos:
        if quarto.verificaQuarto(vEstados):
            if nJogadas % 2 == 0 and quarto.conquistador == -1:
                quarto.conquistador = CPU
                listaPlayers[1].aumentaPontuacao()
            elif nJogadas % 2 != 0 and quarto.conquistador == -1:
                quarto.conquistador = PLAYER
                listaPlayers[0].aumentaPontuacao()

def criaFilhos(no_pai, dificuldade): #conforme o jogo passa pode ficar mais dificil --- no começo do jogo a arvore nao faz diferença
    indices = np.where(no_pai.estado == 0)[0]
    random.shuffle(indices)
    it = 0
    if dificuldade == 0 or len(indices) == 0: #verifica se esta em um nó folha e adiciona um valor heuristico nele
        ancestrais = no_pai.ancestors
        if no_pai.l_players[CPU].pontuacao >= 5:
            no_pai.heuristica = 50
            return
        else:
            for ancestral in ancestrais:
                no_pai.heuristica += ancestral.custo
            no_pai.heuristica = 2*(no_pai.l_players[1].pontuacao - no_pai.l_players[0].pontuacao) - (root.l_players[1].pontuacao - root.l_players[0].pontuacao)     #diferença entre atual e inicial
            no_pai.heuristica += 3*(5-(5-no_pai.l_players[CPU].pontuacao))#diferença do ponto objetivo = 5
            return  
    if dificuldade > 0:
        for i in indices:
            nome = f"{no_pai.name}-{it}"
            novo_estado = no_pai.estado.copy()
            novo_estado[i] = 1
            novo_filho = Node(nome, parent=no_pai, 
                              estado=novo_estado, 
                              n_jogadas=(no_pai.n_jogadas+1), 
                              l_players=copy.deepcopy(no_pai.l_players), 
                              l_quartos=copy.deepcopy(no_pai.l_quartos),
                              heuristica = 0, custo=0)
            marcaPonto(novo_filho.n_jogadas, novo_filho.l_players, novo_filho.l_quartos, novo_filho.estado)
            
            #adiciona um custo a cada jogada
            if novo_filho.l_players[CPU].pontuacao >= 5:
                novo_filho.custo = 50
            else:
                custo = (novo_filho.l_players[1].pontuacao - novo_filho.l_players[0].pontuacao) - (no_pai.l_players[1].pontuacao - no_pai.l_players[0].pontuacao)
                if custo > 0:
                    novo_filho.custo = 2
                if custo == 0:
                    novo_filho.custo = 1
                if custo < 0:
                    novo_filho.custo = -5
            criaFilhos(novo_filho, (dificuldade-1))
            it += 1
    else:
        return
    
def listarAncestrais(no):
    ancestrais = []

    while no.parent is not None:
        no = no.parent
        ancestrais.append(no.name)
    ancestrais.reverse()
    return ancestrais

def miniMax(node, profundidade): #melhorar
    
    if profundidade == 0 or len(node.children) == 0:
        return node
    
    if node.n_jogadas % 2 != 0:
        # Jogador Maximizador
        melhor_filho = None
        melhor_valor = float('-inf') #qlqr coisa pode ser melhor
        for filho in node.children:
            valor_atual = miniMax(filho, profundidade - 1).heuristica
            if valor_atual > melhor_valor:
                melhor_valor = valor_atual
                melhor_filho = filho
        node.heuristica = melhor_filho.heuristica
        return melhor_filho
    else:
        # Jogador Minimizador
        pior_filho = None
        pior_valor = float('inf')
        for filho in node.children:
            valor_atual = miniMax(filho, profundidade - 1).heuristica
            if valor_atual < pior_valor:
                pior_valor = valor_atual
                pior_filho = filho
        node.heuristica = pior_filho.heuristica
        return pior_filho
    
def miniMax_Phoda(node, profundidade):
    if profundidade == 0 or len(node.children) == 0:
        return node
    
    if node.n_jogadas % 2 != 0:
        # Jogador Maximizador
        melhor_filho = None
        melhor_valor = float('-inf')
        poda1 = 0
        for filho in node.children:
            valor_atual = miniMax_Phoda(filho, profundidade - 1).heuristica
            if valor_atual > melhor_valor:
                melhor_valor = valor_atual
                melhor_filho = filho
            for ancestral in node.ancestors:
                if ancestral.n_jogadas%2 == 0:
                    if ancestral.heuristica <= node.heuristica:
                        poda1 = 1
                        break
            if poda1:
                break
        node.heuristica = melhor_filho.heuristica
        return melhor_filho
    else:
        # Jogador Minimizador
        pior_filho = None
        pior_valor = float('inf')
        poda = 0
        for filho in node.children:
            valor_atual = miniMax_Phoda(filho, profundidade - 1).heuristica
            if valor_atual < pior_valor:
                pior_valor = valor_atual
                pior_filho = filho
            for ancestral in node.ancestors:
                if ancestral.n_jogadas%2 != 0:
                    if ancestral.heuristica >= node.heuristica:
                        poda = 1
                        break
            if poda:
                break
        node.heuristica = pior_filho.heuristica
        return pior_filho


LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

PLAYER = 0
CPU = 1

#dimensoes da janela
largura = 800
altura = 800

cor_fundo = (94, 10, 11)        #dark red
cor_quarto = (205,133,63)# cpu


estados = [0,0,0,0,0] #0 menu inicial -- 1 trocar dificuldade
modo_jogo = [0,0] # 0 pve - 1 pvp
linhas = np.zeros((1, 24))      #um vetor que representa as linhas que liga os pontinhos estão ligadas ou desligadas
nJogadas = 0                    #representa o número de jogadas já feitas, tem muita importancia para o jogo
level = 2
level_escolhido = 0
player = Player(PLAYER)
cpu = Player(CPU)
listPlayers = [player, cpu]
quarto = None
qrtAnterior = None

#inicia os quartos
listQuartos = [] 
listQuartos.append(Quartos(1, 0,1,2,11, (160,160)))
listQuartos.append(Quartos(2, 2,3,4,9, (320,160)))
listQuartos.append(Quartos(3, 4,5,6,7, (480,160)))
listQuartos.append(Quartos(4, 14,11,12,13, (160,320)))
listQuartos.append(Quartos(5, 12,9,10,15, (320,320)))
listQuartos.append(Quartos(6, 10,7,8,17, (480,320)))
listQuartos.append(Quartos(7, 16,13,18,23, (160,480)))
listQuartos.append(Quartos(8, 18,15,20,21, (320,480)))
listQuartos.append(Quartos(9, 20,17,22,19, (480,480)))

#inicia o game
pygame.init()

#definindo a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo dos Pontinhos")

janela.fill(cor_fundo)

# Loop principal do jogo
executando = True
estados[0] = 1
modo_jogo[0] = 1
debug = 0

while executando: 
    pygame.display.flip()
    cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
    if estados[0] and not estados[1] and not estados[2] and not estados[3] and not estados[4]: #menu inicial
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 300 and y > 325 and x < 500 and y < 360: 
                    reinicia_jogo()
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 3)
                    break
                elif x > 250 and y > 380 and x < 550 and y < 415:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 1)
                    break
                elif x > 325 and y > 435 and x < 475 and y < 470:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 2)
                    break
            x,y = pygame.mouse.get_pos()
            if x > 300 and y > 325 and x < 500 and y < 360:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[0] = (56,155,219)
            elif x > 250 and y > 380 and x < 550 and y < 415:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[1] = (56,155,219)
            elif x > 325 and y > 435 and x < 475 and y < 470:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[2] = (56,155,219)
            else:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
            desenhaMsg(janela, 400, 150, "Dot&Boxes!", 80, (251, 162, 23), "straight")
            desenhaMsg(janela, 400, 350, "Iniciar", 40, cor_menu[0], "ocra")
            desenhaMsg(janela, 400, 400, "Dificuldade", 40, cor_menu[1], "ocra")
            desenhaMsg(janela, 400, 450, "Ajuda", 40, cor_menu[2], "ocra")
    if estados[1] and not estados[0] and not estados[2] and not estados[3] and not estados[4]:#tela de ajustar dificuldade
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 300 and y > 325 and x < 500 and y < 360:
                    limpaTela(janela)
                    pygame.display.flip()
                    level_escolhido = 0
                    setEstado(estados, 0)
                    break
                elif x > 250 and y > 380 and x < 550 and y < 415:
                    limpaTela(janela)
                    pygame.display.flip()
                    level_escolhido = 1
                    setEstado(estados, 0)
                    break
                elif x > 325 and y > 435 and x < 475 and y < 470:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 0)
                    break
            x,y = pygame.mouse.get_pos()
            if x > 300 and y > 325 and x < 500 and y < 360:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[0] = (56,155,219)
            elif x > 250 and y > 380 and x < 550 and y < 415:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[1] = (56,155,219)
            elif x > 325 and y > 435 and x < 475 and y < 470:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[2] = (56,155,219)
            else:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
            desenhaMsg(janela, 400, 250, "DIFICULDADE", 50, (251, 162, 23), "ocrb10")
            desenhaMsg(janela, 400, 350, "Normal", 40, cor_menu[0], "ocra")
            desenhaMsg(janela, 400, 400, "Insano", 40, cor_menu[1], "ocra")
            desenhaMsg(janela, 400, 460, "Voltar", 30, cor_menu[2], "ocra")
    if estados[2] and not estados[1] and not estados[0] and not estados[3] and not estados[4]:#tela de ajuda
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 325 and y > 435 and x < 475 and y < 470:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 0)
                    break
            x,y = pygame.mouse.get_pos()
            if x > 325 and y > 435 and x < 475 and y < 470:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[2] = (56,155,219)
            else:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
            desenhaMsg(janela, 410, 50, "Dot and Boxes e um jogo estrategico onde os jogadores", 20, (251, 162, 23), "ocra")
            desenhaMsg(janela, 410, 80, "se alternam para conectar pontos adjacentes no tabuleiro", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 110, "com linhas, formando quadrados. Cada vez que um jogador", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 140, "completa um quadrado, ele ganha um ponto. O objetivo e", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 170, "conquistar a maior quantidade de quadrados possivel, ", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 200, "bloqueando o adversario e evitando que ele faca o mesmo.", 20, (251, 162, 23), "ocra") 

            desenhaMsg(janela, 410, 250, "Como jogar? Primeiramente voce deve selecionar um", 20, (251, 162, 23), "ocra")
            desenhaMsg(janela, 410, 280, "espaco entre 4 pontos do tabuleiro usando um clique", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 310, "do mouse. Em seguida, para realizar uma jogada,", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 340, "voce deve usar as teclas W, A, S, D. Cada tecla", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 370, "corresponde a aresta (linha) do espaco previamente", 20, (251, 162, 23), "ocra") 
            desenhaMsg(janela, 410, 400, "selecionado que sera desenhada.", 20, (251, 162, 23), "ocra") 

            desenhaMsg(janela, 400, 460, "Voltar", 30, cor_menu[2], "ocra")
            (251, 162, 23)   
        pass
    if estados[3] and not estados[1] and not estados[2] and not estados[0] and not estados[4]: 
        for evento in pygame.event.get():# verifica todos os eventos
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                idQuarto = getId(x, y)
                if idQuarto:
                    pygame.draw.rect(janela, cor_fundo, (0, 75, 800, 30))
                    quarto = selecionaQuarto(listQuartos, idQuarto)
                    desenhaSelecaoQuarto(janela, quarto, qrtAnterior)
                    qrtAnterior = quarto
                else:
                    desenhaMsg(janela, 400, 90, "Fora dos Limites!", 30, (255,255,0))
            elif evento.type == pygame.KEYDOWN:
                pygame.draw.rect(janela, cor_fundo, (0, 75, 800, 30)) # limpa o espaço de desenho do avisos
                if evento.key == pygame.K_ESCAPE:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 4)
                    break
                elif evento.key == pygame.K_F2:
                    if modo_jogo[0]:
                        setModo(modo_jogo, 1)
                    elif modo_jogo[1]:
                        setModo(modo_jogo, 0)
                elif evento.key == pygame.K_F1:
                    if debug:
                        debug = 0
                    else:
                        debug = 1
                elif quarto is not None and quarto.conquistador == -1:
                    if evento.key == pygame.K_a:
                        if quarto.setLinha(LEFT):
                            nJogadas += 1
                    elif evento.key == pygame.K_w:
                        if quarto.setLinha(TOP):
                            nJogadas += 1
                    elif evento.key == pygame.K_d:
                        if quarto.setLinha(RIGHT):
                            nJogadas += 1
                    elif evento.key == pygame.K_s:
                        if quarto.setLinha(BOTTOM):
                            nJogadas += 1
                    marcaPonto(nJogadas, listPlayers, listQuartos, linhas[0])
                    #aumenta dificuldade
                    if nJogadas%2 != 0 and modo_jogo[0]:
                        if nJogadas > 10:
                            level = 3
                        if level_escolhido:
                            if nJogadas > 14:
                                level = 5
                            if nJogadas > 16:
                                level = 6
                    root = Node("A", estado=linhas[0].copy(), 
                            n_jogadas=nJogadas, 
                            l_players=copy.deepcopy(listPlayers), 
                            l_quartos=copy.deepcopy(listQuartos),
                            heuristica=0, custo=0)
                    criaFilhos(root, level)
                    if nJogadas%2 != 0:
                        melhor_jogada = miniMax(root, level)
                        linhas[0] = melhor_jogada.estado
                        listPlayers = melhor_jogada.l_players
                        listQuartos = melhor_jogada.l_quartos
                        nJogadas += 1
                    if debug:
                        for pre, _, node in RenderTree(root):
                            print("%s%s" % (pre, str(node.heuristica)))
                        print("numero de jogadas: {}".format(nJogadas))
                        print("nivel: {}".format(level_escolhido))
                        print("melhor jogada: {}, {}".format(melhor_jogada.heuristica, melhor_jogada.estado))
                else:
                    desenhaMsg(janela, 400, 90, "Nada Selecionado!", 30, (255,255,0))
            desenhaTabuleiro(janela, listQuartos)
            desenhaHUD(janela, listPlayers, nJogadas)
    if estados[4] and not estados[1] and not estados[2] and not estados[3] and not estados[0]:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 280 and y > 325 and x < 510 and y < 360:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 3)
                    break
                elif x > 280 and y > 380 and x < 500 and y < 415:
                    limpaTela(janela)
                    pygame.display.flip()
                    reinicia_jogo()
                    setEstado(estados, 3)
                    break
                elif x > 230 and y > 435 and x < 550 and y < 470:
                    limpaTela(janela)
                    pygame.display.flip()
                    setEstado(estados, 0)
                    break
            x,y = pygame.mouse.get_pos()
            if x > 280 and y > 325 and x < 510 and y < 360:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[0] = (56,155,219)
            elif x > 280 and y > 380 and x < 500 and y < 415:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[1] = (56,155,219)
            elif x > 230 and y > 435 and x < 550 and y < 470:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
                cor_menu[2] = (56,155,219)
            else:
                cor_menu = [(255,255,0), (255,255,0), (255,255,0)]
            desenhaMsg(janela, 400, 150, "PAUSE!", 80, (255,255,0), "ocrb10")
            desenhaMsg(janela, 400, 350, "Continuar", 40, cor_menu[0], "ocra")
            desenhaMsg(janela, 400, 400, "Resetar", 40, cor_menu[1], "ocra")
            desenhaMsg(janela, 400, 450, "Menu Pricipal", 40, cor_menu[2], "ocra")   
    if nJogadas == 24:
        janela.fill(cor_fundo)
        if listPlayers[0].pontuacao > listPlayers[1].pontuacao:
            desenhaMsg(janela, 400, 400, "PLAYER GANHOU!", 50, (255,255,0))
            desenhaMsg(janela, 235, 750, "PLAYER: {}".format(listPlayers[0].pontuacao), 39, (255, 255, 255))
            desenhaMsg(janela, 550, 750, "CPU: {}".format(listPlayers[1].pontuacao), 39, (255, 255, 255))
        else:
            desenhaMsg(janela, 400, 400, "PERDEU PLAYBOY!", 50, (255,255,0))
            desenhaMsg(janela, 235, 750, "PLAYER: {}".format(listPlayers[0].pontuacao), 39, (255, 255, 255))
            desenhaMsg(janela, 550, 750, "CPU: {}".format(listPlayers[1].pontuacao), 39, (255, 255, 255))
    pygame.display.flip()
# Encerrar o Pygame
pygame.quit()
