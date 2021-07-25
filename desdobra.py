"""
*******ESCOPO*******

1. Gerara dezenas aleatoriamente sem criterios. [FEITO]
2. verificar se tem e eliminar conjuntos repetidos.

"""
from random import sample
from verify import *
from estruturar_dados import *


conjunto = [2,16,27, 40, 47, 48]


def full_aleatorio(range_inicio,range_fim,quantidade_dezenas,quantidade_aposta):

    """
    descrição: cria apostas aleatorias sem criterios
    entrada: int range_inicio, int range_fim, int quantidade_dezenas, int quantidade_aposta
    saida: int array
    """

    dezenas_aleatorias=[]
    del dezenas_aleatorias[:]

    for i in range(quantidade_aposta):
        dezenas_aleatorias.append(sorted(sample(range(range_inicio, range_fim + 1), quantidade_dezenas)))

    return dezenas_aleatorias





p = full_aleatorio(1,25,15,10)

for i in range(len(p)):
    print(p[i])