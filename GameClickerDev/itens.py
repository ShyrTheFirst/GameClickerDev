import random, pygame

def lista_nomes_aprendiz():
    tirar_rand = []
    nome_final = ""
    primeiro_nome = ['Espada', 'Adaga', 'Faca']
    segundo_nome = ['matadora','assassina']
    terceiro_nome = ['de mundos']
    quarto_nome = ['celestial','lendaria','real']
    quant_nomes = random.randrange(1,5)
    lista_listas_nomes = [primeiro_nome,segundo_nome,terceiro_nome,quarto_nome]
    for num1 in range(0,quant_nomes):
        tirar_rand.append(lista_listas_nomes[num1])
    for num2 in range(0,len(tirar_rand)):
        nome_final += " " + random.choice(tirar_rand[num2])
    return nome_final
def lista_nomes_espadachim():
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
    if classe == 'aprendiz':
        arma_aprendiz = pygame.image.load(r'armas\armanv1.png')
        return arma_aprendiz
    if nivel_char <= 20:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv1.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv1_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv1_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv1_cajado.png')
            return cajado
            
    if nivel_char <= 30 and nivel_char >= 20:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv2.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv2_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv2_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv2_cajado.png')
            return cajado
            
    if nivel_char >= 30 and nivel_char <= 40:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv3.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv3_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv3_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv3_cajado.png')
            return cajado
            
    if nivel_char >= 40 and nivel_char <= 50:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv4.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv4_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv4_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv4_cajado.png')
            return cajado
            
    if nivel_char >= 50 and nivel_char <= 100 :
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv5.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv5_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv5_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv5_cajado.png')
            return cajado
            
    if nivel_char >= 100 and nivel_char <= 200:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv6.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv6_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv6_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv6_cajado.png')
            return cajado
            
    if nivel_char >= 200 and nivel_char <= 300:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv7.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv7_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv7_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv7_cajado.png')
            return cajado
            
    if nivel_char >= 300 and nivel_char <= 400:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv8.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv8_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv8_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv8_cajado.png')
            return cajado
            
    if nivel_char >= 400 and nivel_char <= 500:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv9.png')
            return arma_espadachim
        if classe == 'guerreiro':
            machado = pygame.image.load(r'armas\armanv9_machado.png')
            return machado
        if classe == 'arqueiro':
            arco = pygame.image.load(r'armas\armanv9_arco.png')
            return arco
        if classe == 'mago':
            cajado = pygame.image.load(r'armas\armanv9_cajado.png')
            return cajado
            
    if nivel_char >= 500:
        if classe == 'espadachim':
            arma_espadachim = pygame.image.load(r'armas\armanv10.png')
            return arma_espadachim
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
        imagem_char_cabeca = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_olhos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_torso = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_pes = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_maos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        cabeca_escolhido = random.choice(imagem_char_cabeca)
        olhos_escolhido = random.choice(imagem_char_olhos)
        torso_escolhido = random.choice(imagem_char_torso)
        pes_escolhido = random.choice(imagem_char_pes)
        maos_escolhido = random.choice(imagem_char_maos)
        imagem_char = (cabeca_escolhido,olhos_escolhido,torso_escolhido,pes_escolhido,maos_escolhido)
        return imagem_char
    if classe == 'guerreiro':
        imagem_char_cabeca = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_olhos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_torso = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_pes = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_maos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        cabeca_escolhido = random.choice(imagem_char_cabeca)
        olhos_escolhido = random.choice(imagem_char_olhos)
        torso_escolhido = random.choice(imagem_char_torso)
        pes_escolhido = random.choice(imagem_char_pes)
        maos_escolhido = random.choice(imagem_char_maos)
        imagem_char = (cabeca_escolhido,olhos_escolhido,torso_escolhido,pes_escolhido,maos_escolhido)
        return imagem_char
    if classe == 'arqueiro':
        imagem_char_cabeca = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_olhos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_torso = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_pes = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_maos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        cabeca_escolhido = random.choice(imagem_char_cabeca)
        olhos_escolhido = random.choice(imagem_char_olhos)
        torso_escolhido = random.choice(imagem_char_torso)
        pes_escolhido = random.choice(imagem_char_pes)
        maos_escolhido = random.choice(imagem_char_maos)
        imagem_char = (cabeca_escolhido,olhos_escolhido,torso_escolhido,pes_escolhido,maos_escolhido)
        return imagem_char
    if classe == 'mago':
        imagem_char_cabeca = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_olhos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_torso = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_pes = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_maos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        cabeca_escolhido = random.choice(imagem_char_cabeca)
        olhos_escolhido = random.choice(imagem_char_olhos)
        torso_escolhido = random.choice(imagem_char_torso)
        pes_escolhido = random.choice(imagem_char_pes)
        maos_escolhido = random.choice(imagem_char_maos)
        imagem_char = (cabeca_escolhido,olhos_escolhido,torso_escolhido,pes_escolhido,maos_escolhido)
        return imagem_char
    if classe == 'espadachim':
        imagem_char_cabeca = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_olhos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_torso = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_pes = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        imagem_char_maos = (pygame.image.load(r'personagens\char_aprendiz.png'),pygame.image.load(r'personagens\char_aprendiz.png'))
        cabeca_escolhido = random.choice(imagem_char_cabeca)
        olhos_escolhido = random.choice(imagem_char_olhos)
        torso_escolhido = random.choice(imagem_char_torso)
        pes_escolhido = random.choice(imagem_char_pes)
        maos_escolhido = random.choice(imagem_char_maos)
        imagem_char = (cabeca_escolhido,olhos_escolhido,torso_escolhido,pes_escolhido,maos_escolhido)
        return imagem_char

def escolher_monstro():
    monstro_cabeca = (pygame.image.load(r'monstros\cabeca1.png'),pygame.image.load(r'monstros\cabeca2.png'),pygame.image.load(r'monstros\cabeca3.png'),pygame.image.load(r'monstros\cabeca4.png'),pygame.image.load(r'monstros\cabeca5.png'),pygame.image.load(r'monstros\cabeca6.png'),pygame.image.load(r'monstros\cabeca7.png'),pygame.image.load(r'monstros\cabeca8.png'),pygame.image.load(r'monstros\cabeca9.png'),pygame.image.load(r'monstros\cabeca10.png'),pygame.image.load(r'monstros\cabeca11.png'),pygame.image.load(r'monstros\cabeca12.png'))
    monstro_olhos = ((pygame.image.load(r'monstros\olhos1.png'),pygame.image.load(r'monstros\olhos_dano1.png')),(pygame.image.load(r'monstros\olhos2.png'),pygame.image.load(r'monstros\olhos_dano1.png')),(pygame.image.load(r'monstros\olhos3.png'),pygame.image.load(r'monstros\olhos_dano1.png')),(pygame.image.load(r'monstros\olhos4.png'),pygame.image.load(r'monstros\olhos_dano2_1.png')),(pygame.image.load(r'monstros\olhos5.png'),pygame.image.load(r'monstros\olhos_dano2_2.png')),(pygame.image.load(r'monstros\olhos6.png'),pygame.image.load(r'monstros\olhos_dano2_3.png')),(pygame.image.load(r'monstros\olhos7.png'),pygame.image.load(r'monstros\olhos_dano3_1.png')),(pygame.image.load(r'monstros\olhos8.png'),pygame.image.load(r'monstros\olhos_dano3_2.png')),(pygame.image.load(r'monstros\olhos9.png'),pygame.image.load(r'monstros\olhos_dano3_3.png')),(pygame.image.load(r'monstros\olhos10.png'),pygame.image.load(r'monstros\olhos_dano4_1.png')),(pygame.image.load(r'monstros\olhos11.png'),pygame.image.load(r'monstros\olhos_dano4_2.png')),(pygame.image.load(r'monstros\olhos12.png'),pygame.image.load(r'monstros\olhos_dano4_3.png')))
    monstro_torso = (pygame.image.load(r'monstros\torso1.png'),pygame.image.load(r'monstros\torso2.png'),pygame.image.load(r'monstros\torso3.png'),pygame.image.load(r'monstros\torso4.png'),pygame.image.load(r'monstros\torso5.png'),pygame.image.load(r'monstros\torso6.png'),pygame.image.load(r'monstros\torso7.png'),pygame.image.load(r'monstros\torso8.png'),pygame.image.load(r'monstros\torso9.png'),pygame.image.load(r'monstros\torso10.png'),pygame.image.load(r'monstros\torso11.png'),pygame.image.load(r'monstros\torso12.png'))
    monstro_pes = (pygame.image.load(r'monstros\pes1.png'),pygame.image.load(r'monstros\pes2.png'),pygame.image.load(r'monstros\pes3.png'),pygame.image.load(r'monstros\pes4.png'),pygame.image.load(r'monstros\pes5.png'),pygame.image.load(r'monstros\pes6.png'),pygame.image.load(r'monstros\pes7.png'),pygame.image.load(r'monstros\pes8.png'),pygame.image.load(r'monstros\pes9.png'),pygame.image.load(r'monstros\pes10.png'),pygame.image.load(r'monstros\pes11.png'),pygame.image.load(r'monstros\pes12.png'))
    monstro_maos = (pygame.image.load(r'monstros\maos1.png'),pygame.image.load(r'monstros\maos2.png'),pygame.image.load(r'monstros\maos3.png'),pygame.image.load(r'monstros\maos4.png'),pygame.image.load(r'monstros\maos5.png'),pygame.image.load(r'monstros\maos6.png'),pygame.image.load(r'monstros\maos7.png'),pygame.image.load(r'monstros\maos8.png'),pygame.image.load(r'monstros\maos9.png'),pygame.image.load(r'monstros\maos10.png'),pygame.image.load(r'monstros\maos11.png'),pygame.image.load(r'monstros\maos12.png'))
    
    cabeca_escolhido = random.choice(monstro_cabeca)
    olhos_escolhido = random.choice(monstro_olhos)
    torso_escolhido = random.choice(monstro_torso)
    pes_escolhido = random.choice(monstro_pes)
    maos_escolhido = random.choice(monstro_maos)
    lista_escolhido = (cabeca_escolhido,olhos_escolhido,torso_escolhido,pes_escolhido,maos_escolhido)
    
    return lista_escolhido
