"""
*******ESCOPO*******

1. Gerara dezenas aleatoriamente sem criterios. [FEITO]
2. verificar se tem e eliminar conjuntos repetidos.

"""
from random import sample
from verify import *


def full_aleatorio(range_inicio,range_fim,quantidade_dezenas,quantidade_aposta):

    dezenas_aleatorias=[]
    del dezenas_aleatorias[:]

    for i in range(quantidade_aposta):
        dezenas_aleatorias.append(sorted(sample(range(range_inicio, range_fim + 1), quantidade_dezenas)))

    return dezenas_aleatorias

conf = [0,50,9] #0não - 1sim: quer parImpar, porcentagem de par impar ou multiplos, multiplo de
conf_loteria = [1,25,15,10] #(0- megasena; 1- lotofacil; 2- lotomania)loteria, inicio contagem, fim contagem, quantidade de numeros, quantidade de apostas
conjunto_garantir = [2,16,27] #lista com numeros preferenciais (ignorar ou garantir)
conjunto_ignorar = [20,36,57] #lista com numeros preferenciais (ignorar ou garantir)


def desdobrar(garantir,ignorar,loteria_conf):

    sugestao_aleatorias = []
    del sugestao_aleatorias[:]
    
    sugestao_repetidos= []
    del sugestao_repetidos[:]

    ignorar_estes=[]
    del ignorar_estes[:]

    indice = 0

    tamanho = loteria_conf[1] - len(garantir)

    if ignorar > garantir:
        x = repetidos(garantir,ignorar)
    else:
        x = repetidos(ignorar,garantir)
    

    if x == []:
        for i in range(loteria_conf[3]):
            sugestao_aleatorias.append(sorted(sample(range(loteria_conf[0], tamanho + 1), loteria_conf[2])))
        
        if len(sugestao_aleatorias[0]) >= tamanho:
            for a in range(len(sugestao_aleatorias)):

                garantir_estes = repetidos(garantir,sugestao_aleatorias[a])
                ignorar_estes = repetidos(ignorar,sugestao_aleatorias[a])

                sugestao_repetidos = garantir_estes + ignorar_estes

                if len(sugestao_repetidos)> 0:
                    for k in range(len(sugestao_repetidos)):
                        indice = sugestao_aleatorias.index(sugestao_repetidos[k])
                        if sugestao_aleatorias[indice] >= 60:
                            sugestao_aleatorias[indice] = sugestao_aleatorias[indice] - sample(range(1, 60), 1)
                        else:
                            sugestao_aleatorias[indice] = sugestao_aleatorias[indice] + 1

            return sorted(sugestao_aleatorias + garantir_estes)
        
        else:
            for a in range(len(garantir)):

                garantir_estes = repetidos(garantir,sugestao_aleatorias[a])
                ignorar_estes = repetidos(ignorar,sugestao_aleatorias[a])

                sugestao_repetidos = garantir_estes + ignorar_estes

                if len(sugestao_repetidos)> 0:
                    for k in range(len(sugestao_repetidos)):
                        lista = sugestao_aleatorias[k]
                        indice = lista.index(sugestao_repetidos[k])
                       
                        if sugestao_aleatorias[k][indice] == 60:
                            sugestao_aleatorias[k][indice] = sugestao_aleatorias[a][indice] - sample(range(1, 60), 1)
                        else:
                            # print(type(sugestao_aleatorias[k][indice]))
                            # print(sugestao_aleatorias[k][indice])
                            sugestao_aleatorias[k][indice] = sugestao_aleatorias[a][indice] + 1

                        print('stap',k)
                        print('repetidos:',sugestao_repetidos,'- indice:',indice,'- lista:',lista)
            return sorted(sugestao_aleatorias + garantir_estes)



    elif len(x) == 0:

        for i in range(loteria_conf[3]):

            sugestao_aleatorias.append(sorted(sample(range(loteria_conf[0], tamanho + 1), loteria_conf[2])))

        return sorted(sugestao_aleatorias)
    
    else:
        print("erro")

print(desdobrar(conjunto_garantir,conjunto_ignorar,conf_loteria))