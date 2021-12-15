import pygame, sys, random
from escrita_por_letra import escrever_por_letra as escrever
from classes import Botao, Personagem, Item, Monstro, chao
from vars import sair_do_jogo
import vars as v

import menu_iniciar

##inicializando pygame##

#pygame#
relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption('GameClickerDev')
tela = pygame.display.set_mode((v.largura,v.altura))

#fontes#
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)

#botoes#
botao_iniciar = pygame.image.load(r'imagens\iniciar.png')
botao_iniciar_press = pygame.image.load(r'imagens\iniciar_press.png')
botao_sair = pygame.image.load(r'imagens\sair.png')
botao_sair_press = pygame.image.load(r'imagens\sair_press.png')
botao_aleatorio = pygame.image.load(r'imagens\aleatorio.png')
botao_aleatorio_press = pygame.image.load(r'imagens\aleatorio_press.png')
botao_melhorar = pygame.image.load(r'imagens\melhorar.png')
botao_melhorar_press = pygame.image.load(r'imagens\melhorar_press.png')
botao_guerreiro_sele = pygame.image.load(r'imagens\guerreiro.png')
botao_mago_sele = pygame.image.load(r'imagens\mago.png')
botao_arqueiro_sele = pygame.image.load(r'imagens\arqueiro.png')
botao_guerreiro_press = pygame.image.load(r'imagens\guerreiro_press.png')
botao_mago_press = pygame.image.load(r'imagens\mago_press.png')
botao_arqueiro_press = pygame.image.load(r'imagens\arqueiro_press.png')
botao_espadachim_sele = pygame.image.load(r'imagens\espadachim.png')
botao_espadachim_press = pygame.image.load(r'imagens\espadachim_press.png')


##fim da inicialização do pygame##

#####INICIO DO CODIGO DO JOGO#####
chao = chao()
chao.desenhar_fundo()
chao.desenhar()
nome = fonte.render("Escolha seu nome: ", 1, (255,255,255))
tela.blit(nome, (25,25))
pygame.display.update()

###DEFINIR NOME POR INPUT###
while v.game_on == True:
   
   for event in pygame.event.get():
      sair_do_jogo()
      #receber nome#
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RETURN:
            v.display_class = True
            chao.desenhar_fundo()
            chao.desenhar()
            v.game_on = False
         if event.key == pygame.K_BACKSPACE:
            v.input_usuario = v.input_usuario[:-1]
            chao.desenhar_fundo()
            tela.blit(nome, (25,25))            
            mostrar_texto = fonte.render(v.input_usuario, 1, (255,255,255))
            tela.blit(mostrar_texto,(25,60))
            pygame.display.flip()
         else:
            v.input_usuario += event.unicode
            mostrar_texto = fonte.render(v.input_usuario, 1, (255,255,255))
            tela.blit(mostrar_texto,(25,60))
            pygame.display.flip()
            
   #mostrar nome na tela#          
   #mostrar_texto = fonte.render(v.input_usuario, 1, (255,255,255))
   #tela.blit(mostrar_texto,(25,60))
   pygame.display.flip()
###FIM DA DEFINIÇÃO POR INPUT###
   
###LIMPANDO A TELA E FAZENDO AJUSTES###
tela.fill((0,0,0))
pygame.display.update()
frase = 'Game Start!!   '
escrever(frase,300,260,(255,255,255),tela,200)
pygame.display.update()
v.input_usuario = v.input_usuario[:-1]

###DEFININDO AS CLASSES###
item_arma = Item()
char = Personagem(item_arma)
botao_melhorar = Botao(v.botao_posx,0,1.5,botao_melhorar,botao_melhorar_press)
botao_aleatorio = Botao(v.botao_posx,50,1.5,botao_aleatorio,botao_aleatorio_press)


def blitar_tudo():
   chao.desenhar_fundo()
   chao.desenhar()
   char.mostrar_level()
   char.mostrar_dano()
   char.mostrar_classe()
   char.inventario()
   char.name(v.input_usuario)
   monstro.desenhar_monstro()
   char.desenhar_char()
   item_arma.desenhar_item(tela)        
   monstro.vida()
   botao_melhorar.desenhar(tela)
   botao_aleatorio.desenhar(tela)

###CHAMANDO AS DEF DAS CLASSES###
monstro = Monstro(v.game_level)
blitar_tudo()


###INICIO DO JOGO###
while v.display_class == True:
    #verificar nivel do jogo#
    if v.game_level == 10 and v.escolha_classe == False:
       
       while v.escolha_classe == False:
          sair_do_jogo()
          tela.fill((0,0,0))
          mensagem_escolha = fonte.render("Escolha sua classe:", 1, (255,255,255))
          tela.blit(mensagem_escolha,(100,100))
          botao_guerreiro = Botao(100,200,1.5,botao_guerreiro_sele,botao_guerreiro_press)
          botao_mago = Botao(250,200,1.5,botao_mago_sele,botao_mago_press)
          botao_arqueiro = Botao(400,200,1.5,botao_arqueiro_sele,botao_arqueiro_press)
          botao_espadachim = Botao(550,200,1.5,botao_espadachim_sele,botao_espadachim_press)
          botao_guerreiro.desenhar(tela)
          botao_mago.desenhar(tela)
          botao_arqueiro.desenhar(tela)
          botao_espadachim.desenhar(tela)
          pygame.display.update()
          ####clicar no botao para escolher a classe####
          reta_guerreiro = botao_guerreiro.rect
          reta_mago = botao_mago.rect
          reta_arqueiro = botao_arqueiro.rect
          reta_espadachim = botao_espadachim.rect
          if pygame.mouse.get_pressed()[0] == 1:
             posicao_mouse = pygame.mouse.get_pos()
             if pygame.Rect.collidepoint(reta_guerreiro,posicao_mouse):
                char.mudar_classe('guerreiro')
                v.guerreiro = True
                v.aprendiz = False
                blitar_tudo()
                v.escolha_classe = True
             if pygame.Rect.collidepoint(reta_mago,posicao_mouse):
                char.mudar_classe('mago')
                v.mago = True
                v.aprendiz = False
                blitar_tudo()
                v.escolha_classe = True
             if pygame.Rect.collidepoint(reta_arqueiro,posicao_mouse):
                char.mudar_classe('arqueiro')
                v.arqueiro = True
                v.aprendiz = False
                blitar_tudo()
                v.escolha_classe = True
             if pygame.Rect.collidepoint(reta_espadachim,posicao_mouse):
                char.mudar_classe('espadachim')
                v.espadachim = True
                v.aprendiz = False
                blitar_tudo()
                v.escolha_classe = True




          
    #CRIAR MOB#
    if v.novo_mob:
        sair_do_jogo()
        monstro = Monstro(v.game_level)
        v.mob_killed += 1
        v.player_nv = round(v.mob_killed/10)
        item_arma.gerar_item(char,v.player_nv,tela)
        blitar_tudo()
        pygame.display.flip()
        v.novo_mob = False
    else:
        #blitar tela do jogo#
        sair_do_jogo()        
        #detectar clique do mouse#
        for event in pygame.event.get():
            if pygame.mouse.get_pressed() == (1,0,0):
                #definir retas para usar collidepoint#
                posicao_mouse = pygame.mouse.get_pos()
                mob_reta = monstro.reta_monstro
                melhorar_reta = botao_melhorar.rect
                aleatorio_reta = botao_aleatorio.rect
                
                #collidepoint para o monstro#
                if pygame.Rect.collidepoint(mob_reta,posicao_mouse):
                    monstro.clicou(char)
                    blitar_tudo()
                if pygame.Rect.collidepoint(melhorar_reta,posicao_mouse):
                    
                    #if char.dinheiro < custo_melhorar:
                    # #aparecer compra negada (botao fica cinza)
                    #else:
                    botao_melhorar.desenhar_clique(tela)
                    pygame.display.flip()
                    item_arma.melhorar_item(char)
                    blitar_tudo()
                    pygame.time.delay(200)
                    #custo_melhorar += 1 ; valor_melhorar = custo_melhorar*custo_melhorar
                    
                if pygame.Rect.collidepoint(aleatorio_reta,posicao_mouse):
                    
                    #if char.dinheiro < custo_aleatorio:
                    # #aparecer compra negada (botao fica cinza)
                    #else:
                    botao_aleatorio.desenhar_clique(tela)
                    pygame.display.flip()
                    item_arma.item_aleatorio(char,tela)
                    blitar_tudo()
                    pygame.time.delay(200)
                    #custo_aleatorio += 1000 ; valor_aleatorio = custo_aleatorio*v.game_level
                    
        
