import pygame, sys, random, time
import vars as v


#fontes#
pygame.font.init()
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)
tela = pygame.display.set_mode((v.largura,v.altura))



def esperar(milissegundos):
    time = pygame.time.get_ticks()
    tempo_de_espera = time+milissegundos
    while time <= tempo_de_espera:
        time = pygame.time.get_ticks()

def escrever_por_letra(frase,posx,posy,cor,tela,tempo):
    escrever = ' '
    for letra in frase:
        escrever += letra
        mostrar_escrita = fonte.render(escrever,1,cor)
        limpar_escrita_anterior = pygame.Rect(posx,posy,v.largura,v.altura)
        pygame.draw.rect(tela,(65,105,225),limpar_escrita_anterior)
        tela.blit(mostrar_escrita,(posx,posy))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        esperar(tempo)
        

###EXEMPLO DE USO############################################
#frase = "Frase de teste para verificar se a def funciona " # 
#escrever_por_letra(frase,100,100,(255,255,255),tela,200)   #  
#############################################################
