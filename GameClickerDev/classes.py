import pygame,sys,random
from vars import sair_do_jogo
import vars as v
import itens as i
from dividir_linhas import dividir_linhas
from escrita_por_letra import escrever_por_letra as escrever
from itens import escolher_monstro,escolher_char,lista_nomes_aprendiz,lista_nomes_guerreiro,lista_nomes_mago,lista_nomes_arqueiro,escolher_arma

pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((v.largura,v.altura))
font_default = pygame.font.get_default_font()
fonte = pygame.font.Font(r'fontes\alagard.ttf',25)




#####CLASSES#####

##Classe BOTAO##
class Botao():
    def __init__(self,x,y,transformar,imagem, imagem_press, imagem_emcima=None):
        self.imagem = imagem
        self.imagem_pressionado = imagem_press
        self.imagem_emcima = imagem_emcima
        self.tamanhox,self.tamanhoy = self.imagem.get_rect().size
        self.imagem = pygame.transform.scale(self.imagem,(self.tamanhox*transformar,self.tamanhoy*transformar))
        self.imagem_pressionado = pygame.transform.scale(self.imagem_pressionado,(self.tamanhox*transformar,self.tamanhoy*transformar))
        if self.imagem_emcima != None:
            self.imagem_emcima = pygame.transform.scale(self.imagem_emcima,(self.tamanhox*transformar,self.tamanhoy*transformar))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)
       

    def desenhar(self,tela):
        tela.blit(self.imagem,(self.rect.x,self.rect.y))
    def desenhar_clique(self,tela):
        tela.blit(self.imagem_pressionado,(self.rect.x,self.rect.y))
    def desenhar_emcima(self,tela):
        tela.blit(self.imagem_emcima,(self.rect.x,self.rect.y))
        
##Fim Classe BOTAO##
        
##Classe ITEM##
class Item():
    def __init__(self,nivel=1):
        self.poder = 0
        self.bonus = 0
        self.aumento_poder = 0
        self.item_name = 'Espada matadora de mundos celestial'
        self.imagem_item = escolher_arma(nivel,'aprendiz')
        
    def melhorar_item(self,player):
        self.poder += 1
        self.bonus += 1
        player.aumentar_dano()      

    def gerar_item(self,player,nivel,tela):
        if v.guerreiro:
            self.item_name = lista_nomes_guerreiro()
            self.imagem_item = escolher_arma(nivel,'guerreiro')
            
        if v.mago:
            self.item_name = lista_nomes_mago()
            self.imagem_item = escolher_arma(nivel,'mago')
            
        if v.arqueiro:
            self.item_name = lista_nomes_arqueiro()
            self.imagem_item = escolher_arma(nivel,'arqueiro')
            
        if v.aprendiz:
            self.item_name = lista_nomes_aprendiz()
            self.imagem_item = escolher_arma(nivel,'aprendiz')
            
        self.desenhar_item(tela)
        player.aumentar_dano()

    def desenhar_item(self,tela):
        self.itemx = 675
        self.itemy = 200
        self.nomeitemx = 600
        self.nomeitemy = 300
        tela.blit(self.imagem_item,(self.itemx,self.itemy))
        self.nome_e_bonus_raw = self.item_name + ' ' + '+' + str(self.bonus)
        self.nome_e_bonus = dividir_linhas(self.nome_e_bonus_raw)
        for palavra in self.nome_e_bonus:
            self.blitar_palavra = fonte.render(palavra, 1, (255,255,255))
            tela.blit(self.blitar_palavra,(self.nomeitemx,self.nomeitemy))
            self.nomeitemy += 25
            
        
        

    def limpar_item(self):
       reta_limpar_item = pygame.Rect(550,200,400,200)
       pygame.draw.rect(tela,(65,105,225),reta_limpar_item)

    def item_aleatorio(self,player,tela):
        prob_poder = random.randrange(1,100)
        self.poder += prob_poder
        if v.guerreiro:
            self.item_name = lista_nomes_guerreiro()
            
        if v.mago:
            self.item_name = lista_nomes_mago()
            
        if v.arqueiro:
            self.item_name = v.lista_nomes_arqueiro()
            
        if v.aprendiz:
            self.item_name = lista_nomes_aprendiz()
        self.desenhar_item(tela)
        player.aumentar_dano()
        

        

##Fim Classe ITEM##

##Classe PERSONAGEM##
class Personagem():
   def __init__(self,item,classe='aprendiz'):
       self.classe = classe
       self.level = v.game_level
       self.item = item
       self.dano_normal = 1
       self.dano_arma = 0 + item.poder
       self.dano_total = self.dano_normal+self.dano_arma
       self.imagem_char = escolher_char(self.classe)

   def levelup(self):
       self.level = v.game_level
       self.dano_normal += 1

   def aumentar_dano(self):
       self.dano_arma = 0 + self.item.poder
       self.dano_total = self.dano_normal + self.dano_arma
       
   def mostrar_level(self):   
       self.mostrarlevelvar = "Voce esta no level: %s" %(self.level)
       self.mostrarlevel = fonte.render(self.mostrarlevelvar, 1, (255,255,255))
       tela.blit(self.mostrarlevel, (25,60))
       
   def limpar_level(self):        
       sizex,sizey = pygame.font.Font.size(fonte,self.mostrarlevelvar)
       limpar_rect = pygame.Rect(25,60,sizex,sizey)
       pygame.draw.rect(tela,(65,105,225),limpar_rect)

   def mostrar_dano(self):   
       self.mostrardanovar = "Seu dano e: %s" %(self.dano_total)
       self.mostrardano = fonte.render(self.mostrardanovar, 1, (255,255,255))
       tela.blit(self.mostrardano, (25,85))
       
   def limpar_dano(self):        
       sizex_dano,sizey_dano = pygame.font.Font.size(fonte,self.mostrardanovar)
       limpar_dano_rect = pygame.Rect(25,85,sizex_dano,sizey_dano)
       pygame.draw.rect(tela,(65,105,225),limpar_dano_rect)

   def name(self, name):
      name = str(name)
      mostrar_nome = fonte.render(name, 1, (255,255,255))
      tela.blit(mostrar_nome, (30,30))

   def mudar_classe(self,classe):
       self.classe = classe
       
   def mostrar_classe(self):   
       self.mostrarclassevar = "Sua classe e: %s" %(self.classe)
       self.mostrarclasse = fonte.render(self.mostrarclassevar, 1, (255,255,255))
       tela.blit(self.mostrarclasse, (25,110))
       
   def limpar_classe(self):        
       sizex_classe,sizey_classe = pygame.font.Font.size(fonte,self.mostrarclassevar)
       limpar_classe_rect = pygame.Rect(25,85,sizex_classe,sizey_classe)
       pygame.draw.rect(tela,(65,105,225),limpar_classe_rect)
       
       
   def desenhar_char(self):
        self.charx = 25
        self.chary = 200
        tela.blit(self.imagem_char,(self.charx,self.chary))

   def limpar_char(self):
       reta_limpar_char = pygame.Rect(25,200,150,150)
       pygame.draw.rect(tela,(65,105,225),reta_limpar_char)
       
       

##Fim Classe PERSONAGEM##

##Classe MONSTRO##
class Monstro():
   def __init__(self, dificuldade):
        self.posx_monstro = 300
        self.posy_monstro = 200
        self.imagem_monstro,self.imagem_monstro_dano = escolher_monstro()
        self.reta_monstro = self.imagem_monstro.get_rect()
        self.reta_monstro.topleft = self.posx_monstro,self.posy_monstro
        self.posx_mob = self.posx_monstro     
        self.posy_mob = self.posy_monstro
        
        self.dificuldade = dificuldade
        self.set_vida = int(self.dificuldade*10)
       
   def desenhar_monstro(self):
      tela.blit(self.imagem_monstro,(self.posx_mob,self.posy_mob))
      pygame.display.flip()
      
   def limpar_monstro(self):
       reta_limpar_monstro = pygame.Rect(300,200,200,200)
       pygame.draw.rect(tela,(65,105,225),reta_limpar_monstro)

      
   def vida(self):
       self.mostrar_vida = "HP: %i" %(self.set_vida)
       self.mostrar_vida_render = fonte.render(self.mostrar_vida, 1, (255,255,255))
       tela.blit(self.mostrar_vida_render, (340,410))
      
   def clicou(self,player):
      dano_total = player.dano_total
      self.set_vida -= dano_total
      tela.blit(self.imagem_monstro_dano,(self.posx_mob,self.posy_mob))
      pygame.display.flip()
      pygame.time.delay(200)
      if self.set_vida <= 0:
          self.morte(player)
      else:
          self.vida()
      

   def morte(self,player):
       v.game_level += 1
       player.levelup()
       v.novo_mob = True

##Fim Classe MONSTRO##

##Classe CHAO##
class chao():
    def __init__(self):
        self.posx = 0
        self.posy = 400
        self.rect = pygame.Rect(self.posx,self.posy,800,600)

    def desenhar(self):
        self.color = v.cor_chao
        pygame.draw.rect(tela,self.color,self.rect)

##Fim Classe CHAO##
