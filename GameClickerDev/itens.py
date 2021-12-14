import random, pygame


def lista_nomes_aprendiz():
    tirar_rand = []
    nome_final = ""
    primeiro_nome = ['Espada', 'Adaga', 'Faca', 'Lamina','Entalhadora','Empaladora','Espinho','Sabre','Punhal','Foice','Segadeira','Espeto','Ponta','Cimitarra']
    segundo_nome = ['matadora','dilaceradora','quebradora','destruidora','assassina','vigilante','traidora','desgraçadora','desoladora','torturante','libertadora','caotica','aclamada','fatiadora', 'abolidora']
    terceiro_nome = ['de mundos','dos anjos','dos demonios','de supernovas','do caos','do clamor','do juramento','da extincao','da abolicao','da virtude','do desespero','da persiguicao','da punicao', 'da alianca','da nobreza']
    quarto_nome = ['celestial','demoniaca','universal','final','iluminada','lendaria','ancestral','aclamada','juramentada','renascida','vingadora','eterna','irada','virtuosa','punitiva','real']
    quant_nomes = random.randrange(1,5)
    lista_listas_nomes = [primeiro_nome,segundo_nome,terceiro_nome,quarto_nome]
    for num1 in range(0,quant_nomes):
        tirar_rand.append(lista_listas_nomes[num1])
    for num2 in range(0,len(tirar_rand)):
        nome_final += " " + random.choice(tirar_rand[num2])
    return nome_final


def lista_nomes_guerreiro():
    tirar_rand = []
    nome_final = ""
    primeiro_nome = ['Machado','Separador','Cerquilha','Retalhadora', 'Machadinha', 'Maça','Berdiche','Bec de Corbin', 'Pernachs','Facha','Alabarda','Franquisque','Machado de Guerra']
    segundo_nome = ['matador','dilacerador','quebrador','destruidor','assassino','vigilante','traidor','desgraçador','desolador','torturante','libertador','caotico','aclamado','fatiador', 'abolidor']
    terceiro_nome = ['de mundos','dos anjos','dos demonios','de supernovas','do caos','do clamor','do juramento','da extincao','da abolicao','da virtude','do desespero','da persiguicao','da punicao', 'da alianca','da nobreza']
    quarto_nome = ['celestial','demoniaco','universal','final','iluminado','lendario','ancestral','aclamado','juramentado','renascido','vingador','eterno','irado','virtuoso','punitivo','real']
    quant_nomes = random.randrange(1,5)
    lista_listas_nomes = [primeiro_nome,segundo_nome,terceiro_nome,quarto_nome]
    for num1 in range(0,quant_nomes):
        tirar_rand.append(lista_listas_nomes[num1])
    for num2 in range(0,len(tirar_rand)):
        nome_final += " " + random.choice(tirar_rand[num2])
    return nome_final

def lista_nomes_arqueiro():
    tirar_rand = []
    nome_final = ""
    primeiro_nome = ['Arco', 'Besta', 'Arpao', 'Balista','Arco Longo','Falconete','Virote','Bodoque','Balesta']
    segundo_nome = ['matador','dilacerador','quebrador','destruidor','assassino','vigilante','traidor','desgraçador','desolador','torturante','libertador','caotico','aclamado','fatiador', 'abolidor']
    terceiro_nome = ['de mundos','dos anjos','dos demonios','de supernovas','do caos','do clamor','do juramento','da extincao','da abolicao','da virtude','do desespero','da persiguicao','da punicao', 'da alianca','da nobreza']
    quarto_nome = ['celestial','demoniaco','universal','final','iluminado','lendario','ancestral','aclamado','juramentado','renascido','vingador','eterno','irado','virtuoso','punitivo','real']
    quant_nomes = random.randrange(1,5)
    lista_listas_nomes = [primeiro_nome,segundo_nome,terceiro_nome,quarto_nome]
    for num1 in range(0,quant_nomes):
        tirar_rand.append(lista_listas_nomes[num1])
    for num2 in range(0,len(tirar_rand)):
        nome_final += " " + random.choice(tirar_rand[num2])
    return nome_final


def lista_nomes_mago():
    tirar_rand = []
    nome_final = ""
    primeiro_nome = ['Cajado', 'Mangual', 'Punhos', 'Porrete','Cetro','Clava','Bastao','Taco','Varinha','Vara','Graveto','Tronco']
    segundo_nome = ['matador','dilacerador','quebrador','destruidor','assassino','vigilante','traidor','desgraçador','desolador','torturante','libertador','caotico','aclamado','fatiador', 'abolidor']
    terceiro_nome = ['de mundos','dos anjos','dos demonios','de supernovas','do caos','do clamor','do juramento','da extincao','da abolicao','da virtude','do desespero','da persiguicao','da punicao', 'da alianca','da nobreza']
    quarto_nome = ['celestial','demoniaco','universal','final','iluminado','lendario','ancestral','aclamado','juramentado','renascido','vingador','eterno','irado','virtuoso','punitivo','real']
    quant_nomes = random.randrange(1,5)
    lista_listas_nomes = [primeiro_nome,segundo_nome,terceiro_nome,quarto_nome]
    for num1 in range(0,quant_nomes):
        tirar_rand.append(lista_listas_nomes[num1])
    for num2 in range(0,len(tirar_rand)):
        nome_final += " " + random.choice(tirar_rand[num2])
    return nome_final


  
def escolher_arma(nivel_char,classe):
    if nivel_char == 1:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv1.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv1_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv1_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv1_cajado.png')
            return cajado
            
    if nivel_char == 2:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv2.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv2_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv2_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv2_cajado.png')
            return cajado
            
    if nivel_char == 3:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv3.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv3_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv3_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv3_cajado.png')
            return cajado
            
    if nivel_char == 4:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv4.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv4_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv4_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv4_cajado.png')
            return cajado
            
    if nivel_char == 5:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv5.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv5_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv5_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv5_cajado.png')
            return cajado
            
    if nivel_char == 6:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv6.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv6_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv6_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv6_cajado.png')
            return cajado
            
    if nivel_char == 7:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv7.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv7_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv7_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv7_cajado.png')
            return cajado
            
    if nivel_char == 8:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv8.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv8_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv8_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv8_cajado.png')
            return cajado
            
    if nivel_char == 9:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv9.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv9_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv9_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv9_cajado.png')
            return cajado
            
    if nivel_char == 10:
        if classe == 'aprendiz':
            arma_aprendiz = pygame.image.load(r'armas\armanv10.png')
            return arma_aprendiz
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv10_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv10_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv10_cajado.png')
            return cajado


def escolher_char(classe='aprendiz'):
    if classe == 'aprendiz':
        imagem_char = pygame.image.load(r'personagens\char_aprendiz.png')
        return imagem_char
    if classe == 'guerreiro':
        imagem_char = pygame.image.load(r'personagens\char_guerreiro.png')
        return imagem_char
    if classe == 'arqueiro':
        imagem_char = pygame.image.load(r'personagens\char_arqueiro.png')
        return imagem_char
    if classe == 'mago':
        imagem_char = pygame.image.load(r'personagens\char_mago.png')
        return imagem_char

def escolher_monstro():
    monstro_1 = (pygame.image.load(r'monstros\monstro_1.png'), pygame.image.load(r'monstros\monstro_1_dano.png'))
    monstro_2 = (pygame.image.load(r'monstros\monstro_2.png'), pygame.image.load(r'monstros\monstro_2_dano.png'))
    monstro_3 = (pygame.image.load(r'monstros\monstro_3.png'), pygame.image.load(r'monstros\monstro_3_dano.png'))
    monstro_4 = (pygame.image.load(r'monstros\monstro_4.png'), pygame.image.load(r'monstros\monstro_4_dano.png'))
    monstro_5 = (pygame.image.load(r'monstros\monstro_5.png'), pygame.image.load(r'monstros\monstro_5_dano.png'))
    monstro_6 = (pygame.image.load(r'monstros\monstro_6.png'), pygame.image.load(r'monstros\monstro_6_dano.png'))
    monstro_7 = (pygame.image.load(r'monstros\monstro_7.png'), pygame.image.load(r'monstros\monstro_7_dano.png'))
    monstro_8 = (pygame.image.load(r'monstros\monstro_8.png'), pygame.image.load(r'monstros\monstro_8_dano.png'))
    monstro_9 = (pygame.image.load(r'monstros\monstro_9.png'), pygame.image.load(r'monstros\monstro_9_dano.png'))
    monstro_10 = (pygame.image.load(r'monstros\monstro_10.png'), pygame.image.load(r'monstros\monstro_10_dano.png'))
    lista_monstro = (monstro_1,monstro_2,monstro_3,monstro_4,monstro_5,monstro_6,monstro_7,monstro_8,monstro_9,monstro_10)
    monstro_escolhido = random.choice(lista_monstro)
    return monstro_escolhido
        
                
