import pygame, sys, random
from escrita_por_letra import escrever_por_letra as escrever
from classes import Botao, Personagem, Item, Monstro, chao
import vars as v
from scoreboard import dados_score, print_scoreboard

import menu_iniciar

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
botao_iniciar = pygame.image.load(r'imagens\iniciar.png')
botao_iniciar_press = pygame.image.load(r'imagens\iniciar_press.png')
botao_sair = pygame.image.load(r'imagens\sair.png')
botao_sair_press = pygame.image.load(r'imagens\sair_press.png')
botao_score = pygame.image.load(r'imagens\score.png')
botao_score_press = pygame.image.load(r'imagens\score_press.png')

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
nome = fonte.render("Choose a name: ", 1, (255,255,255))
tela.blit(nome, (25,25))
pygame.display.update()

###DEFINIR NOME POR INPUT###
while v.game_on == True:
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      #receber nome#
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RETURN:
            v.display_class = True
            tela.fill((65,105,225))
            v.game_on = False
         if event.key == pygame.K_BACKSPACE:
            v.input_usuario = v.input_usuario[:-1]
            tela.fill((65,105,225))
            tela.blit(nome, (25,25))
            pygame.display.flip()
         else:
            v.input_usuario += event.unicode
            
   #mostrar nome na tela#          
   mostrar_texto = fonte.render(v.input_usuario, 1, (255,255,255))
   lim_sizex, lim_sizey = 800,800
   mostrar_texto_limpar = pygame.Rect(25,60,lim_sizex,lim_sizey)
   pygame.draw.rect(tela,(65,105,225),mostrar_texto_limpar)
   tela.blit(mostrar_texto,(25,60))
   pygame.display.update()
   
###FIM DA DEFINIÇÃO POR INPUT###

###LIMPANDO A TELA E FAZENDO AJUSTES###
tela.fill((65,105,225))
pygame.display.update()
frase = 'Game Start!!   '
escrever(frase,300,260,(255,255,255),tela,200)
tela.fill((65,105,225))
pygame.display.update()
v.input_usuario = v.input_usuario[:-1]

###DEFININDO AS CLASSES###
char = Personagem()
item_arma = Item(tela,char)
monstro = Monstro(v.game_level)
botao_melhorar = Botao(v.botao_posx,0,1.5,botao_melhorar,botao_melhorar_press)
botao_aleatorio = Botao(v.botao_posx,50,1.5,botao_aleatorio,botao_aleatorio_press)
botao_sair_jogo = Botao(600,500,1.5,botao_sair,botao_sair_press)

###CHAMANDO AS CLASSES###
monstro.escolher_monstro()
char.nome(v.input_usuario)
char.desenhar_char()
char.inventario()
char.mostrar_dano()
item_arma.desenhar_item()
monstro.vida()

###INICIO DO JOGO###
while v.display_class == True:
    for event in pygame.event.get():       
      if event.type == pygame.QUIT:
         dados_score(char)
         pygame.quit()
         sys.exit()
    v.player_nv = round((v.game_level)/10)
    #verificar nivel do jogo#
    if v.game_level == 10 and v.escolha_classe == False:
       tela.fill((65,105,225))
       pygame.display.update()
       pygame.time.delay(100)
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
       while v.escolha_classe == False:
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          botao_guerreiro = Botao(300,200,1.5,botao_guerreiro_sele,botao_guerreiro_press)
          botao_mago = Botao(300,300,1.5,botao_mago_sele,botao_mago_press)
          botao_arqueiro = Botao(300,400,1.5,botao_arqueiro_sele,botao_arqueiro_press)
          botao_espadachim =Botao(300,500,1.5,botao_espadachim_sele,botao_espadachim_press)
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
                botao_guerreiro.desenhar_clique(tela)
                pygame.display.flip()
                pygame.time.delay(200)
                char.mudar_classe('guerreiro')
                v.guerreiro = True
                v.aprendiz = False
                v.escolha_classe = True
                tela.fill((65,105,225))
                pygame.display.update()
                frase_01 = "You choose: %s" %('warrior')
                escrever(frase_01,300,260,(255,255,255),tela,200)
                pygame.display.flip()
                pygame.time.delay(200)
                tela.fill((65,105,225))
                pygame.display.update()
             if pygame.Rect.collidepoint(reta_mago,posicao_mouse):
                botao_mago.desenhar_clique(tela)
                pygame.display.flip()
                pygame.time.delay(200)
                char.mudar_classe('mago')
                v.mago = True
                v.aprendiz = False
                v.escolha_classe = True
                tela.fill((65,105,225))
                pygame.display.update()
                frase_01 = "You choose: %s" %('mage')
                escrever(frase_01,300,260,(255,255,255),tela,200)
                pygame.display.flip()
                pygame.time.delay(200)
                tela.fill((65,105,225))
                pygame.display.update()
             if pygame.Rect.collidepoint(reta_arqueiro,posicao_mouse):
                botao_arqueiro.desenhar_clique(tela)
                pygame.display.flip()
                pygame.time.delay(200)
                char.mudar_classe('arqueiro')
                v.arqueiro = True
                v.aprendiz = False
                v.escolha_classe = True
                tela.fill((65,105,225))
                pygame.display.update()
                frase_01 = "You choose: %s" %('bowman')
                escrever(frase_01,300,260,(255,255,255),tela,200)
                pygame.display.flip()
                pygame.time.delay(200)
                tela.fill((65,105,225))
                pygame.display.update()
             if pygame.Rect.collidepoint(reta_espadachim,posicao_mouse):
                botao_espadachim.desenhar_clique(tela)
                pygame.display.flip()
                pygame.time.delay(200)
                char.mudar_classe('espadachim')
                v.espadachim = True
                v.aprendiz = False
                v.escolha_classe = True
                tela.fill((65,105,225))
                pygame.display.update()
                frase_01 = "You choose: %s" %('swordman')
                escrever(frase_01,300,260,(255,255,255),tela,200)
                pygame.display.flip()
                pygame.time.delay(200)
                tela.fill((65,105,225))
                pygame.display.update()

          
    #CRIAR MOB#
    if v.novo_mob:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              dados_score(char)
              pygame.quit()
              sys.exit()   
        monstro = Monstro(v.game_level)
        monstro.escolher_monstro()
        item_arma.gerar_item(v.player_nv)
        v.novo_mob = False
    else:
        #blitar tela do jogo#
        monstro.limpar_monstro()
        monstro.desenhar_monstro()
        char.limpar_level()
        char.mostrar_level()        
        char.limpar_char()
        char.desenhar_char()
        char.limpar_inventario()
        char.inventario()
        char.limpar_dano()
        char.mostrar_dano()
        item_arma.limpar_item()
        item_arma.desenhar_item()
        monstro.limpar_vida()
        monstro.vida()
        botao_melhorar.desenhar(tela)  
        botao_aleatorio.desenhar(tela)
        botao_sair_jogo.desenhar(tela)
        sizex_custo,sizey_custo = 500,25
        limpar_custo = pygame.Rect(550,10,sizex_custo,sizey_custo)
        pygame.draw.rect(tela,(65,105,225),limpar_custo)
        mostrarcustovar = "Cost: %s" %(v.custo)
        mostrarcusto = fonte.render(mostrarcustovar, 1, (255,255,255))
        tela.blit(mostrarcusto, (550,10))
        sizex_custo_aleatorio,sizey_custo_aleatorio = 500,25
        limpar_custo_aleatorio = pygame.Rect(550,60,sizex_custo_aleatorio,sizey_custo_aleatorio)
        pygame.draw.rect(tela,(65,105,225),limpar_custo_aleatorio)
        mostrarcusto_aleatoriovar = "Cost: %s" %(v.custo_aleatorio)
        mostrarcusto_aleatorio = fonte.render(mostrarcusto_aleatoriovar, 1, (255,255,255))
        tela.blit(mostrarcusto_aleatorio, (550,60))
        
        #detectar clique do mouse#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dados_score(char)
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed() == (1,0,0):
                #definir retas para usar collidepoint#
                posicao_mouse = pygame.mouse.get_pos()
                mob_reta = monstro.reta_monstro_cabeca
                melhorar_reta = botao_melhorar.rect
                aleatorio_reta = botao_aleatorio.rect
                sair_reta = botao_sair_jogo.rect
                #collidepoint para o monstro#
                if pygame.Rect.collidepoint(mob_reta,posicao_mouse):
                    monstro.clicou(char)
                    char.limpar_level()
                    char.mostrar_level()
                    char.limpar_dano()
                    char.mostrar_dano()
                #collidepoint para o botao melhorar#
                if pygame.Rect.collidepoint(melhorar_reta,posicao_mouse):
                    if char.dinheiro < v.custo:
                       frase_comprar = "You can't buy it"
                       compra_negada = fonte.render(frase_comprar, 1, (255,255,255))
                       tela.blit(compra_negada, (v.botao_posx,120))
                       pygame.display.flip()
                       pygame.time.delay(400)
                       limpar_compranegada = pygame.Rect(v.botao_posx,100,400,50)
                       pygame.draw.rect(tela,(65,105,225),limpar_compranegada)
                    else:
                       botao_melhorar.desenhar_clique(tela)
                       char.dinheiro -= v.custo
                       char.limpar_inventario()
                       char.inventario()
                       item_arma.melhorar_item()
                       item_arma.limpar_item()
                       char.aumentar_dano(item_arma)
                       item_arma.desenhar_item()
                       char.limpar_dano()
                       char.mostrar_dano()
                       pygame.time.delay(200)
                       v.custo += v.game_level*v.custo
                #collidepoint para o botao aleatorio#    
                if pygame.Rect.collidepoint(aleatorio_reta,posicao_mouse):
                    if char.dinheiro < v.custo_aleatorio:
                       frase_comprar = "You can't buy it"
                       compra_negada = fonte.render(frase_comprar, 1, (255,255,255))
                       tela.blit(compra_negada, (v.botao_posx,120))
                       pygame.display.flip()
                       pygame.time.delay(400)
                       limpar_compranegada = pygame.Rect(v.botao_posx,100,400,50)
                       pygame.draw.rect(tela,(65,105,225),limpar_compranegada)
                    else:
                       botao_aleatorio.desenhar_clique(tela)
                       char.dinheiro -= v.custo_aleatorio
                       char.limpar_inventario()
                       char.inventario()
                       item_arma.item_aleatorio()
                       item_arma.limpar_item()
                       item_arma.desenhar_item()
                       char.aumentar_dano(item_arma)
                       char.limpar_dano()
                       char.mostrar_dano()
                       pygame.time.delay(200)
                       v.custo_aleatorio += v.game_level*v.custo_aleatorio
                if pygame.Rect.collidepoint(sair_reta,posicao_mouse):
                   botao_sair_jogo.desenhar_clique(tela)
                   pygame.display.flip()
                   pygame.time.wait(200)
                   dados_score(char)
                   pygame.quit()
                   sys.exit()
                    
        pygame.display.update()
