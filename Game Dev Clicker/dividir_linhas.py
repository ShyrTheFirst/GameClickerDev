import pandas as pd

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


def dividir_score(frase):
    frase_split = frase.split()
    frase_junta = []
    frase_junta2 = []
    palavra_junta = ''
    for i in frase_split:
        if i == '0':
            frase_split.remove(i)

    if len(frase_split) > 4:
        frase_split.pop(0)
        frase_split.pop(0)
        frase_split.pop(0)
        frase_split.pop(0)
        frase_split.pop(0)
        for palavra in frase_split:
            frase_junta2.append(palavra)
            frase_junta2.append(',')
                
            
    if len(frase_junta2) > 0:
        frase_junta2.pop(len(frase_junta2)-1)
    return frase_junta2

def topo_score(frase):
    frase_split = frase.split()
    frase_junta = []
    palavra_junta = ''
    for i in frase_split:
        if i == '0':
            frase_split.remove(i)
    frase_junta.append(frase_split[0])
    frase_junta.append(',')
    frase_junta.append(frase_split[1])
    frase_junta.append(',')
    palavra_junta = frase_split[2] + ' ' + frase_split[3]
    frase_junta.append(palavra_junta)
    frase_junta.append(',')
    frase_junta.append(frase_split[4])
    return frase_junta

