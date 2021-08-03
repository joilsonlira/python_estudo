"""
*******ESCOPO*******

1. Gerara dezenas aleatoriamente sem criterios. [FEITO]
2. verificar se tem e eliminar conjuntos repetidos.

"""
from random import sample
from verify import *


conjunto = [2,16,27]


def full_aleatorio(range_inicio,range_fim,quantidade_dezenas,quantidade_aposta):

    dezenas_aleatorias=[]
    del dezenas_aleatorias[:]

    for i in range(quantidade_aposta):
        dezenas_aleatorias.append(sorted(sample(range(range_inicio, range_fim + 1), quantidade_dezenas)))

    return dezenas_aleatorias


p = full_aleatorio(1,25,15,10)

for i in range(len(p)):
    print(p[i])