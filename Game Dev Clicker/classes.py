import pygame,sys,random
import vars as v
import itens as i
from dividir_linhas import dividir_linhas
from escrita_por_letra import escrever_por_letra as escrever
from itens import escolher_monstro,escolher_char,lista_nomes_aprendiz,lista_nomes_espadachim,lista_nomes_guerreiro,lista_nomes_mago,lista_nomes_arqueiro,escolher_arma

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
    def __init__(self,player,tela,nivel=1):
        self.player = player
        self.tela = tela
        self.poder = 0
        self.bonus = 0
        self.aumento_poder = 0
        self.item_name = 'Sword'
        self.imagem_item = escolher_arma(nivel,'aprendiz')
        
    def melhorar_item(self):
        self.poder += 1
        self.bonus += 1    

    def gerar_item(self,nivel):
        if nivel <= 0:
            self.player_nv = 1
        else:
            self.player_nv = nivel
        if v.guerreiro:
            self.imagem_item = escolher_arma(self.player_nv,'guerreiro')
            
        if v.mago:
            self.imagem_item = escolher_arma(self.player_nv,'mago')
            
        if v.arqueiro:
            self.imagem_item = escolher_arma(self.player_nv,'arqueiro')
            
        if v.espadachim:
            self.imagem_item = escolher_arma(self.player_nv,'espadachim')
            
        if v.aprendiz:
            self.imagem_item = escolher_arma(self.player_nv,'aprendiz')

        self.desenhar_item()

    def desenhar_item(self):
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
            
    def item_aleatorio(self):
        prob_poder = random.randrange(1,100)
        self.poder += prob_poder
        if v.guerreiro:
            self.item_name = lista_nomes_guerreiro()
            
        if v.mago:
            self.item_name = lista_nomes_mago()
            
        if v.arqueiro:
            self.item_name = lista_nomes_arqueiro()
            
        if v.aprendiz:
            self.item_name = lista_nomes_aprendiz()
            
        if v.espadachim:
            self.item_name = lista_nomes_espadachim()
        self.desenhar_item()

    def limpar_item(self):
       reta_limpar_item = pygame.Rect(550,200,400,200)
       pygame.draw.rect(tela,(65,105,225),reta_limpar_item)
        

        

##Fim Classe ITEM##

##Classe PERSONAGEM##
class Personagem():
   def __init__(self,classe='aprendiz'):
       self.dinheiro = 0
       self.classe = classe
       self.level = v.game_level
       self.dano_normal = 1
       self.dano_arma = 0
       self.dano_total = self.dano_normal+self.dano_arma
       self.mostrarlevelvar = ""
       self.mostrardanovar = ""
       self.mostrar_classe = 'apprentice'
       

   def levelup(self):
       self.level = v.game_level
       self.dano_normal += 1

   def inventario(self):       
       self.mostrarinvvar = "You have: %s coins " %(self.dinheiro)       
       self.mostrarinv = fonte.render(self.mostrarinvvar, 1, (255,255,255))
       tela.blit(self.mostrarinv, (25,135))

   def adicionar_inventario(self):
       self.dinheiro += random.randrange(1,10)*self.level

   def limpar_inventario(self):
       limpar_inv = pygame.Rect(25,135,500,25)
       pygame.draw.rect(tela,(65,105,225),limpar_inv)

   def aumentar_dano(self,item):
       self.dano_arma = 0 + item.poder
       self.dano_total = self.dano_normal + self.dano_arma
       
   def mostrar_level(self):   
       self.mostrarlevelvar = "You are level: %s" %(self.level)
       self.mostrarlevel = fonte.render(self.mostrarlevelvar, 1, (255,255,255))
       tela.blit(self.mostrarlevel, (25,60))

   def mostrar_dano(self):   
       self.mostrardanovar = "Your damage: %s" %(self.dano_total)
       self.mostrardano = fonte.render(self.mostrardanovar, 1, (255,255,255))
       tela.blit(self.mostrardano, (25,85))

   def nome(self, nome):
      self.nome_char = str(nome)
      mostrar_nome = fonte.render(self.nome_char, 1, (255,255,255))
      tela.blit(mostrar_nome, (30,30))

   def mudar_classe(self,classe):
       self.classe = classe
       
   def mostrar_classe(self):
       if self.classe == 'espadachim':
           self.mostrar_classe = 'swordman'
       if self.classe == 'arqueiro':
           self.mostrar_classe = 'bowman'
       if self.classe == 'mago':
           self.mostrar_classe = 'mage'
       if self.classe == 'guerreiro':
           self.mostrar_classe = 'warrior'
       self.mostrarclassevar = "Your class: %s" %(self.mostrar_classe)
       self.mostrarclasse = fonte.render(self.mostrarclassevar, 1, (255,255,255))
       tela.blit(self.mostrarclasse, (25,110))       
       
   def desenhar_char(self):
       char_cabeca =escolher_char(self.classe)[0]
       char_olhos =escolher_char(self.classe)[1]
       char_torso =escolher_char(self.classe)[2]
       char_pes =escolher_char(self.classe)[3]
       char_maos =escolher_char(self.classe)[4]
       posx_cabeca,posy_cabeca = 25,220
       posx_olhos,posy_olhos = 25,220
       posx_torso,posy_torso = 25,220
       posx_pes,posy_pes = 25,220
       posx_maos,posy_maos = 25,220
       
       tela.blit(char_cabeca,(posx_cabeca,posy_cabeca))
       tela.blit(char_olhos,(posx_olhos,posy_olhos))
       tela.blit(char_torso,(posx_torso,posy_torso))
       tela.blit(char_pes,(posx_pes,posy_pes))
       tela.blit(char_maos,(posx_maos,posy_maos))
       pygame.display.flip

   def limpar_char(self):
       reta_limpar_char = pygame.Rect(25,220,150,150)
       pygame.draw.rect(tela,(65,105,225),reta_limpar_char)

   def limpar_dano(self):        
       sizex_dano,sizey_dano = pygame.font.Font.size(fonte,self.mostrardanovar)
       limpar_dano_rect = pygame.Rect(25,85,sizex_dano,sizey_dano)
       pygame.draw.rect(tela,(65,105,225),limpar_dano_rect)

   def limpar_level(self):        
       sizex,sizey = pygame.font.Font.size(fonte,self.mostrarlevelvar)
       limpar_rect = pygame.Rect(25,60,sizex,sizey)
       pygame.draw.rect(tela,(65,105,225),limpar_rect)
       
       

##Fim Classe PERSONAGEM##

##Classe MONSTRO##
class Monstro():
   def __init__(self, dificuldade):
        
        self.dificuldade = dificuldade
        self.set_vida = int(self.dificuldade*10)

   def escolher_monstro(self):
       
       self.monstro_cabeca =escolher_monstro()[0]
       self.monstro_olhos,self.monstro_olhos_dano =escolher_monstro()[1]
       self.monstro_torso =escolher_monstro()[2]
       self.monstro_pes =escolher_monstro()[3]
       self.monstro_maos =escolher_monstro()[4]
       
       self.posx_cabeca,self.posy_cabeca = 290,218
       self.posx_olhos,self.posy_olhos = 290,220
       self.posx_torso,self.posy_torso = 290,220
       self.posx_pes,self.posy_pes = 290,220
       self.posx_maos,self.posy_maos = 290,220
       
   def desenhar_monstro(self):
       
       tela.blit(self.monstro_cabeca,(self.posx_cabeca,self.posy_cabeca))
       tela.blit(self.monstro_olhos,(self.posx_olhos,self.posy_olhos))
       tela.blit(self.monstro_torso,(self.posx_torso,self.posy_torso))
       tela.blit(self.monstro_pes,(self.posx_pes,self.posy_pes))
       tela.blit(self.monstro_maos,(self.posx_maos,self.posy_maos))
       pygame.display.flip
       
       self.reta_monstro_cabeca = pygame.Rect(290,218,200,200)
       self.reta_monstro_torso = pygame.Rect(290,220,200,200)
       self.reta_monstro_pes = pygame.Rect(290,220,200,200)
       self.reta_monstro_maos =  pygame.Rect(290,220,200,200)

   def desenhar_monstro_dano(self):
       tela.blit(self.monstro_cabeca,(self.posx_cabeca-10,self.posy_cabeca-10))
       tela.blit(self.monstro_olhos_dano,(self.posx_olhos-10,self.posy_olhos-10))
       tela.blit(self.monstro_torso,(self.posx_torso-10,self.posy_torso-10))
       tela.blit(self.monstro_pes,(self.posx_pes-10,self.posy_pes-10))
       tela.blit(self.monstro_maos,(self.posx_maos-10,self.posy_maos-10))
       pygame.display.flip
      
   def vida(self):
       self.mostrar_vida = "HP: %i" %(self.set_vida)
       self.mostrar_vida_render = fonte.render(self.mostrar_vida, 1, (255,255,255))
       tela.blit(self.mostrar_vida_render, (340,410))

   def limpar_vida(self):
       self.posx_vida,self.posy_vida = 500,25
       limpar_vida_rect = pygame.Rect(340,410,self.posx_vida,self.posy_vida)
       pygame.draw.rect(tela,(65,105,225),limpar_vida_rect)

   def limpar_monstro(self):
       reta_limpar_monstro = pygame.Rect(300,200,200,200)
       pygame.draw.rect(tela,(65,105,225),reta_limpar_monstro)
      
   def clicou(self,player):
      dano_total = player.dano_total
      self.set_vida -= dano_total
      self.limpar_monstro()
      self.desenhar_monstro_dano()
      pygame.display.flip()
      pygame.time.delay(200)
      if self.set_vida <= 0:
          self.morte(player)
      else:
          self.vida()
      

   def morte(self,player):
       v.game_level += 1
       player.levelup()
       player.adicionar_inventario()
       v.novo_mob = True

##Fim Classe MONSTRO##

##Classe CHAO##
class chao():
    def __init__(self):
        self.posx_chao = 0
        self.posy_chao = 400
        self.rect = pygame.Rect(self.posx_chao,self.posy_chao,800,600)

    def desenhar(self):
        self.imagem_chao = pygame.image.load(r'imagens\chao.png').convert()
        tela.blit(self.imagem_chao,(self.posx_chao,self.posy_chao))

##Fim Classe CHAO##
