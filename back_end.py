from random import randrange
from time import sleep

import pygame
import sys

try:
    pygame.init()
except:
    print('\033[31mJogo nao pode ser inicializado nessa maquina :(')

# Cores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Configuracoes da tela
info = pygame.display.Info()  # Obtem as informacoes necessarias da tela
largura, altura = 600, 400
janela = [largura, altura]
background = black
tela = pygame.display.set_mode([largura, altura])
tela.fill(background)
pygame.display.set_caption('Snake')
time = pygame.time.Clock()

# Configuracoes da cobra
tamanho = 10
pos_x = randrange(0, largura - tamanho, 10)
pos_y = randrange(0, altura - tamanho, 10)
velocidade_x = 0
velocidade_y = 0
cobraXY = []
cobracomp = 1
# Configuracoes da maca
tamanho = 10
maca_x = randrange(0, largura - tamanho, 10)
maca_y = randrange(0, altura - tamanho, 10)

# LOOPS DO JOGO
gameover = False


def texto(msg, cor, x, y, tam=20):
    """Escreve uma mensagem na tela."""
    font = pygame.font.SysFont(None, tam)
    txt = font.render(msg, True, cor)
    tela.blit(txt, [x, y])


def menu_inicial():
    """Menu inicial"""
    tamx = 200
    tamy = 50
    x = 200
    y = 100

    # Iniciar
    pygame.draw.rect(tela, white, [x, y, tamx, tamy])
    texto('INICIAR JOGO', green, x + 30, y + 20, 30)
    #####################################################
    y += 100
    # Sair
    pygame.draw.rect(tela, white, [x, y, tamx, tamy])
    texto('SAIR', green, x + 70, y + 20, 30)

    # Eventos na tela inicial
    if eventos_tela_inicial():
        return True
    else:
        return False


def eventos_tela_inicial():
    """Responde aos eventos na tela inicial."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(' :( ')
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if 200 < x < 400 and 100 < y < 150:
                print('iniciar')
                pygame.mouse.set_visible(False)
                return True
            elif 200 < x < 400 and y > 200 and y < 250:
                print('sair')
                pygame.mouse.set_visible(False)
                sys.exit()

def checa_eventos():
    """Responde aos eventos da tela."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(' :) ')
        if event.type == pygame.KEYDOWN:
            cobra_eventos(event)


def cobra():
    """Desenha a cobra na tela."""
    global pos_x, pos_y, cobraXY, cobracomp, gameover
    pos_x += velocidade_x
    pos_y += velocidade_y
    for XY in cobraXY:
        pygame.draw.rect(tela, green, [XY[0], XY[1], tamanho, tamanho])

    # Controlando as bordas
    if pos_x + tamanho > largura:
        pos_x = 0 - tamanho
    elif pos_x < 0:
        pos_x = largura - tamanho
    if pos_y + tamanho > altura:
        pos_y = 0 - tamanho
    elif pos_y < 0:
        pos_y = altura - tamanho



    # Crescimento da snake
    global cobra_inicio
    cobra_inicio = []
    cobra_inicio.append(pos_x)
    cobra_inicio.append(pos_y)
    cobraXY.append(cobra_inicio)
    if len(cobraXY) > cobracomp:
        del cobraXY[0]


turn = 0
def cobra_eventos(event):
    """Responde aos eventos da cobra."""
    global pos_x, pos_y, velocidade_x, velocidade_y, cobracomp, turn
    if event.key == pygame.K_UP and velocidade_y != tamanho:
        velocidade_x = 0
        velocidade_y = -tamanho

        # hack
        if turn == 0:
            cobracomp += 1
            turn = 1
    elif event.key == pygame.K_DOWN and velocidade_y != -tamanho:
        velocidade_x = 0
        velocidade_y = tamanho

        # hack
        if turn == 0:
            cobracomp += 1
            turn = 1
    if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
        velocidade_y = 0
        velocidade_x = tamanho

        # hack
        if turn == 0:
            cobracomp += 1
            turn = 1
    elif event.key == pygame.K_LEFT and velocidade_x != tamanho:
        velocidade_y = 0
        velocidade_x = -tamanho

        # hack
        if turn == 0:
            cobracomp += 1
            turn = 1


def colisao():
    """Responde a colisao da snake com a snake"""
    global cobra_inicio, pos_x, pos_y
    # Controlando as bordas
    """
    if pos_x  > largura:
        return False
    elif pos_x < 0:
        return False
    if pos_y > altura:
        return False
    elif pos_y < 0:
        return False
    """

    if any(bloco == cobra_inicio for bloco in cobraXY[:-1]):
        print('game over')
        sleep(0.2)
        return False
    else:
        return True


def maca():
    """Desenha a maca na tela."""
    global maca_x, maca_y
    pygame.draw.rect(tela, red, [maca_x, maca_y, tamanho, tamanho])


def pontos():
    """Responde a colisoes."""
    # Colisao da snake e maca
    global pos_x, pos_y, maca_x, maca_y, cobracomp
    if pos_x == maca_x and pos_y == maca_y:
        maca_x = randrange(0, largura - tamanho, 10)
        maca_y = randrange(0, altura - tamanho, 10)
        cobracomp += 1


def pontuacao():
    """Faz a contagem da pontuacao"""
    texto(f'{cobracomp - 1}', white, largura - 50, 10, 40)


def menu_final():
    """Menu final"""
    tela.fill(background)
    texto('GAME OVER', red, largura / 3, 10, 50)

    # Reiniciar
    pygame.draw.rect(tela, white, [50, 200, 200, 50])
    texto('REINICIAR', green, 100, 215, 30)

    # Sair
    pygame.draw.rect(tela, white, [350, 200, 200, 50])
    texto('SAIR', green, 425, 215, 30)

    # Pontuacao
    texto(f'{cobracomp} POINTS', blue, largura / 3 + 50, 100, 30)

    # Eventos na tela inicial
    if eventos_tela_final():
        return True
    else:
        return False


def eventos_tela_final():
    """Responde aos eventos na tela inicial."""
    pygame.mouse.set_visible(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(' :( ')
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if 50 < x < 250 and 200 < y < 250:
                print('reiniciar')
                redifine()
                pygame.mouse.set_visible(False)
                return True
            elif 350 < x < 550 and 200 < y < 250:
                print('sair')
                pygame.mouse.set_visible(False)
                sys.exit()


def redifine():
    """Redifine o jogo pra iniciar."""
    global pos_x, pos_y, \
        maca_x, maca_y, \
        velocidade_x, velocidade_y, \
        cobraXY, cobracomp, \
        turn, gameover

    # Configuracoes da cobra
    tamanho = 10
    pos_x = randrange(0, largura - tamanho, 10)
    pos_y = randrange(0, altura - tamanho, 10)
    velocidade_x = 0
    velocidade_y = 0
    cobraXY = []
    cobracomp = 1

    # Configuracoes da maca
    tamanho = 10
    maca_x = randrange(0, largura - tamanho, 10)
    maca_y = randrange(0, altura - tamanho, 10)

    # LOOPS DO JOGO
    turn = 0
    gameover = False
