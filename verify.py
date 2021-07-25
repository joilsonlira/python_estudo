'''
****ESCOPO GERAL****

1- verificar se tem numeros repetidos.[FEITO]
2- verificar se estes numeros compoem um grupo que se repete.
3- Verificar se tem padroes nestes grupos (tipos de numeros, intervalo de surgimento, etc )

'''
from estruturar_dados import *


def quantas_apareceu(dezenas):
    quantidade = 0
    for a in range(i):
        if jogo_csv == "mega_sena.csv":
            quantidade = quantidade + concurso_mega[a]["dezenas"].count(dezenas)

        if jogo_csv == "loto_facil.csv":
            quantidade = quantidade + concurso_loto_facil[a]["dezenas"].count(dezenas)

        if jogo_csv == "loto_mania.csv":
            quantidade = quantidade + concurso_loto_mania[a]["dezenas"].count(dezenas)

    return quantidade


def repetidos(sorteados, aposta):
    """
    descrição: removendo conjuntos existentes 
    valores de entrada: int array

    """
    dezenas = []
    del dezenas[:]
    
    for i in range(len(sorteados)):
        for k in range(len(aposta)):
            if sorteados[i] == aposta[k]:
                dezenas.append(sorteados[i])

                
    return sorted(dezenas)



conj = [5,33,52]

conc = 0
contador = 0
repeticao = 0

concursos_repeticoes = []
del concursos_repeticoes[:]

for i in range(len(conj)):
    if concurso_mega[conc]["dezenas"].count(conj[i]):
        contador = contador + 1
        if contador == len(conj):
            repeticao = repeticao + 1
            concursos_repeticoes.append(concurso_mega[conc]["concurso"])

print(repeticao)

if len(conj) >= 4:
    conjuntos={
        "conjunto": conj,
        "repeticoes_conjunto":repeticao,
        "concursos_conjunto": sorted(concursos_repeticoes)
        }
    





# print(concurso_mega[0])
# print(concurso_loto_facil[0])
# print(concurso_loto_mania[20])
# conj = conjuntos_repetidos(concurso_mega[0]["dezenas"],concurso_mega[1]["dezenas"])
# print(conj)
