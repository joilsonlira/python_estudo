'''
****ESCOPO GERAL****

1- verificar se tem numeros repetidos.[FEITO]
2- verificar se estes numeros compoem um grupo que se repete.
3- Verificar se tem padroes nestes grupos (tipos de numeros, intervalo de surgimento, etc )

'''
from estruturar_dados import csv_dados

def quantas_apareceu(loteria,dezena):
    """[Conta quantas vezes uma dezena apareceu no histórico de uma loteria espesifica.]

    Args:
        loteria (INT): [0 para Megasena; 1 para LotoFacil; 2 para LotoMania.]
        dezena (INT): [dezena que deseja verificar quantas vezes apareceu no historico da loteria desejada.]

    Returns:
        quantidade [INT]: [quantidade de vezes que a dezena informada apareceu em todos os jogos da loteria desejada.]
    """

    p = csv_dados(loteria)
    quantidade = 0

    for a in range(len(p)):
            quantidade = quantidade + p[a]["dezenas"].count(dezena)

    return quantidade




def repetidos(sorteados, aposta):
    """[Verifica se tem numeros repetidos entre os números sorteados e os números apostados]

    Args:
        sorteados (LIST INT): [Lista com os numeros sorteados]
        aposta (LIST INT): [Lista com os numeros apostados]

    Returns:
        [LIST INT]: [Dezenas que se repetiram entre os números sorteados e os números apostados]
    """

    dezenas = []
    del dezenas[:]
    
    for i in range(len(sorteados)):
        for k in range(len(aposta)):
            if sorteados[i] == aposta[k]:
                dezenas.append(sorteados[i])

                
    return sorted(dezenas)



def par_impar(numero):
    if (numero%2) == 0:
        return True
    else:
        return False

def multiploDe(numero,multiplo):
    if not (numero%multiplo):
        return True
    else:
        return False
















