import pygame, sys, random
from escrita_por_letra import escrever_por_letra as escrever
from classes import Botao
import vars as v
from scoreboard import print_scoreboard


##inicializando pygame##

#pygame#
relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption('GameClickerDev')
tela = pygame.display.set_mode((v.largura,v.altura))
tela.fill((65,105,225))

#fontes#
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)

#botoes#
botao_iniciar_normal = pygame.image.load(r'imagens\iniciar.png')
botao_iniciar_press = pygame.image.load(r'imagens\iniciar_press.png')
botao_sair_normal = pygame.image.load(r'imagens\sair.png')
botao_sair_press = pygame.image.load(r'imagens\sair_press.png')
botao_score_normal = pygame.image.load(r'imagens\score.png')
botao_score_press = pygame.image.load(r'imagens\score_press.png')

#inicializar botoes#
botao_iniciar = Botao(25,300,1.5,botao_iniciar_normal,botao_iniciar_press)
botao_sair = Botao(25,500,1.5,botao_sair_normal,botao_sair_press)
botao_score = Botao(25,400,1.5,botao_score_normal,botao_score_press)

botao_iniciar.desenhar(tela)
botao_sair.desenhar(tela)
botao_score.desenhar(tela)
pygame.display.update()

iniciar_colli = botao_iniciar.rect
sair_colli = botao_sair.rect
score_colli = botao_score.rect

frase = 'Game Clicker Dev'
escrever(frase,300,160,(255,255,255),tela,50)
menu = True
while menu:   
    
    botao_iniciar.desenhar(tela)
    botao_sair.desenhar(tela)
    botao_score.desenhar(tela)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (1,0,0):
            posicao_mouse = pygame.mouse.get_pos()
            if pygame.Rect.collidepoint(iniciar_colli,posicao_mouse):
                botao_iniciar.desenhar_clique(tela)
                pygame.display.flip()
                pygame.time.delay(200)
                v.game_on = True
                menu = False
            if pygame.Rect.collidepoint(sair_colli,posicao_mouse):
                botao_sair.desenhar_clique(tela)
                pygame.display.flip()
                pygame.time.delay(200)
                pygame.quit()
                sys.exit()
            if pygame.Rect.collidepoint(score_colli,posicao_mouse):
                botao_score.desenhar_clique(tela)
                pygame.display.flip()
                v.mostrar_score = True
                pygame.time.delay(200)
                #desenhar na tela o score#
                
                tela.fill((65,105,225))
                pygame.display.update()
                botao_sair_score = Botao(25,500,1.5,botao_sair_normal,botao_sair_press)
                print_scoreboard()
                pygame.display.flip()
                while v.mostrar_score:
                    botao_sair_score.desenhar(tela)
                    pygame.display.flip()
                    
                    sair_score_colli = botao_sair_score.rect
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if pygame.mouse.get_pressed()[0] == 1:
                            posicao_mouse = pygame.mouse.get_pos()
                            if pygame.Rect.collidepoint(sair_score_colli,posicao_mouse):
                                botao_sair_score.desenhar_clique(tela)
                                pygame.display.flip()
                                pygame.time.delay(200)
                                v.mostrar_score = False
                                escrever(frase,300,160,(255,255,255),tela,50)
                
