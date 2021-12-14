def dividir_linhas(frase):
    frase_split = frase.split()
    frase_junta = []
    palavra_junta = ''
    palavra_junta2 = ''
    if len(frase_split) == 6:
        for palavra in range(0,len(frase_split)):
            if palavra == 0:
                frase_junta.append(frase_split[palavra])
            if palavra == 1:
                frase_junta.append(frase_split[palavra])
            if palavra == 2:
                palavra_junta += frase_split[palavra]
            if palavra == 3:
                palavra_junta += ' ' + frase_split[palavra]
                frase_junta.append(palavra_junta)
            if palavra == 4:
                palavra_junta2 += frase_split[palavra]
            if palavra == 5:
                palavra_junta2 += ' ' + frase_split[palavra]
                frase_junta.append(palavra_junta2)
        
    if len(frase_split) == 5:
        for palavra in range(0,len(frase_split)):
            if palavra == 0:
                frase_junta.append(frase_split[palavra])
            if palavra == 1:
                frase_junta.append(frase_split[palavra])
            if palavra == 2:
                palavra_junta += frase_split[palavra]
            if palavra == 3:
                palavra_junta += ' ' + frase_split[palavra]
                frase_junta.append(palavra_junta)
            if palavra == 4:
                palavra_junta2 += frase_split[palavra]
                frase_junta.append(palavra_junta2)
                
    if len(frase_split) == 4:
        for palavra in range(0,len(frase_split)):
            if palavra == 0:
                frase_junta.append(frase_split[palavra])
            if palavra == 1:
                frase_junta.append(frase_split[palavra])
            if palavra == 2:
                palavra_junta += frase_split[palavra]
            if palavra == 3:
                palavra_junta += ' ' + frase_split[palavra]
                frase_junta.append(palavra_junta)
                
    if len(frase_split) == 3:
        for palavra in range(0,len(frase_split)):
            if palavra == 0:
                frase_junta.append(frase_split[palavra])
            if palavra == 1:
                frase_junta.append(frase_split[palavra])
            if palavra == 2:
                palavra_junta += frase_split[palavra]
                frase_junta.append(palavra_junta)
                
    if len(frase_split) == 2:
        for palavra in range(0,len(frase_split)):
            if palavra == 0:
                frase_junta.append(frase_split[palavra])
            if palavra == 1:
                frase_junta.append(frase_split[palavra])
                
        

    frase_final = frase_junta
    return frase_final
