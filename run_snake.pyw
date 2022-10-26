from back_end import *

try:
    # Inicializa o pygame
    pygame.init()
except:
    print('\033[31mJogo nao pode ser inicializado nessa maquina :(')


gameinit = True
gameloop = False
gameover = False


def start():
    """PARTE INICIAL DO JOGO"""
    global gameinit, gameloop, gameover

    while gameinit:

        # Relogio da tela
        time.tick(30)

        # Responde a eventos da tela
        checa_eventos()

        #
        if menu_inicial():
            gameinit = False
            gameloop = True
            return main()

        # Atualiza a tela a cada passagem
        pygame.display.update()


def main():
    """LOOP PRINCIPAL DO JOGO"""
    global gameinit, gameloop, gameover

    while gameloop:
        time.tick(30)

        # Responde a eventos da tela
        checa_eventos()
        tela.fill(background)

        # Desenha a snake analisando a colisao
        cobra()
        if not colisao():
            gameinit = True
            gameloop = False
            gameover = True
            return fim_do_jogo()

        # Desenha a maca
        maca()

        # Colisao entre a snake e a maca -> soma pontos
        pontos()

        # Cria o placar de pontuacao
        pontuacao()

        # Atualiza a tela a cada passagem
        pygame.display.update()


def fim_do_jogo():
    """FIM DO JOGO"""
    global gameinit, gameloop, gameover

    while gameover:
        time.tick(30)

        # Responde a eventos da tela
        checa_eventos()

        # Chama a tela com menu final
        menu_final()

        if menu_final():
            gameloop = True
            gameover = False
            return main()

        # Atualiza a tela cada passagem
        pygame.display.update()


if __name__ == '__main__':
    start()
