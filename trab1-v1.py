import pygame
import numpy as np

class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.pontuacao = 0
    
    def aumentaPontuacao(self):
        self.pontuacao += 1

class Quartos:
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

    def verificaQuarto(self) -> bool :#verifica se o quarto atual foi completado      
        if linhas[0, self.L] and linhas[0, self.T] and linhas[0, self.R] and linhas[0, self.B]:
           return True

#funcoes
def desenhaMsg(janela, x, y, mensagem, tamFont, cor): # apresenta uma mensagem na posicao x,y
    fonte = pygame.font.SysFont(None, tamFont)
    texto = fonte.render(mensagem, True, cor)
    posicaoTexto = texto.get_rect()
    posicaoTexto.centerx = x
    posicaoTexto.centery = y
    pygame.draw.rect(janela, cor_fundo, posicaoTexto)
    janela.blit(texto, posicaoTexto)

def desenhaHUD(janela, listPlayers, nJogadas):
    pygame.draw.rect(janela, cor_fundo, (0, 20, 800, 50))
    if nJogadas == 0:
        desenhaMsg(janela, 400, 40, "Turno do PLAYER!", 39, (255, 255, 255))
    elif nJogadas % 2 == 0:
        desenhaMsg(janela, 400, 40, "Turno do PLAYER!", 39, (255, 255, 255))
    else:
        desenhaMsg(janela, 400, 40, "Turno da CPU!",39, (255, 255, 255))
    desenhaMsg(janela, 235, 750, "PLAYER: {}".format(listPlayers[0].pontuacao), 39, (255, 255, 255))
    desenhaMsg(janela, 550, 750, "CPU: {}".format(listPlayers[1].pontuacao), 39, (255, 255, 255))

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
        if qrt.verificaQuarto():
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
        
def marcaPonto(lQuartos, nJogadas, listaPlayers):
    for quarto in lQuartos:
        if quarto.verificaQuarto():
            if nJogadas % 2 == 0 and quarto.conquistador == -1:
                quarto.conquistador = CPU
                listaPlayers[1].aumentaPontuacao()
            elif nJogadas % 2 != 0 and quarto.conquistador == -1:
                quarto.conquistador = PLAYER
                listaPlayers[0].aumentaPontuacao()
 
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

LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

PLAYER = 0
CPU = 1

#dimensoes da janela
largura = 800
altura = 800

cor_fundo = (94, 10, 11) #dark red

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

linhas = np.zeros((1, 24)) #representa as linhas que liga os pontinhos
nJogadas = 0

player = Player(PLAYER)
cpu = Player(CPU)
listPlayers = [player, cpu]
print(listPlayers)
qrtAnterior = None

janela.fill(cor_fundo)

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
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
                quarto = None
                desenhaMsg(janela, 400, 90, "Espaço inválido!", 30, (255,255,0))
        elif evento.type == pygame.KEYDOWN:
            pygame.draw.rect(janela, cor_fundo, (0, 75, 800, 30)) # limpa o espaço de desenho do avisos
            if quarto is not None and quarto.conquistador == -1:
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
                marcaPonto(listQuartos, nJogadas, listPlayers)
                for pl in listPlayers:
                    print(pl.pontuacao)
            else:
               desenhaMsg(janela, 400, 90, "Espaço inválido!", 30, (255,255,0)) 
    desenhaTabuleiro(janela, listQuartos)
    desenhaHUD(janela, listPlayers, nJogadas)
    pygame.display.update()
# Encerrar o Pygame
pygame.quit()
