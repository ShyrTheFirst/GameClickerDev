import pygame, sys

pygame.init()

largura = 800
altura = 600
cor_ativa = (0,0,255)
cor_passiva = (255,0,0)
cor = cor_passiva
cor_chao = (0,66,37)
posx = 350
posy = 350
ativo = False
game_on = False
display_class = False
novo_mob = False
game_level = 1
nivel_char = 1
input_usuario = " "
escolha_classe = False
guerreiro = False
mago = False
arqueiro = False
aprendiz = True
botao_posx = 600

def sair_do_jogo():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
