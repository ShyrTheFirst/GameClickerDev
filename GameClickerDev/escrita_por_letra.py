import pygame, sys, random, time
import vars as v
from vars import sair_do_jogo


#fontes#
pygame.font.init()
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)
tela = pygame.display.set_mode((v.largura,v.altura))
tela_escura = tela



def esperar(milissegundos):
    time = pygame.time.get_ticks()
    tempo_de_espera = time+milissegundos
    while time <= tempo_de_espera:
        time = pygame.time.get_ticks()

def escrever_por_letra(frase,posx,posy,cor,tela,tempo,fundo=tela_escura):
    escrever = ' '
    for letra in frase:
        escrever += letra
        mostrar_escrita = fonte.render(escrever,1,cor)
        tela.blit(fundo,(0,0))
        tela.blit(mostrar_escrita,(posx,posy))
        pygame.display.update()
        sair_do_jogo()
        esperar(tempo)
        

###EXEMPLO DE USO############################################
#frase = "Frase de teste para verificar se a def funciona " #
#escrever_por_letra(frase,100,100,(255,255,255),tela,200)   #
#############################################################
