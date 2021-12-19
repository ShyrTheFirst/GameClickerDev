import pandas as pd
import vars as v
from dividir_linhas import dividir_linhas, dividir_score, topo_score
from escrita_por_letra import escrever_por_letra as escrever
import pygame


#pygame#
relogio = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption('GameClickerDev')
tela = pygame.display.set_mode((v.largura,v.altura))
tela.fill((65,105,225))


nome = ''
dinheiro = 0
level_do_jogo = 0
classe = ''
conta = [0]

#def para conseguir os dados#

def dados_score(player):
    nome = player.nome_char
    dinheiro = player.dinheiro
    level_do_jogo = v.game_level
    if v.guerreiro:
        classe = 'warrior'
    if v.mago:
        classe = 'mage'
    if v.arqueiro:
        classe = 'bowman'
    if v.espadachim:
        classe = 'swordman'
    if v.aprendiz:
        classe = 'apprentice'
        
    df_score = pd.DataFrame(
    {
        'name':nome,
        'money':dinheiro,
        'max level':level_do_jogo,
        'class':classe
        }, index = conta
    )

    df_score.to_csv('scoreboard.csv',index=False)

def print_scoreboard():
    scoreboard_string = str(pd.read_csv('scoreboard.csv'))
    scoreboard = dividir_score(scoreboard_string)
    scoreboard_topo = topo_score(scoreboard_string)
    escrever(scoreboard_topo,300,235,(255,255,255),tela,200)
    score_x = 300
    score_y = 260
    escrever(scoreboard,score_x,score_y,(255,255,255),tela,200)    
    
