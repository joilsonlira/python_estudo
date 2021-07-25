'''
****ESCOPO GERAL****

1- verificar se tem numeros repetidos.[FEITO]
2- verificar se estes numeros compoem um grupo que se repete.
3- Verificar se tem padroes nestes grupos (tipos de numeros, intervalo de surgimento, etc )

'''
import csv
import numpy as np

jogo_csv = "assets/mega_sena.csv"

concurso_mega = []
del concurso_mega[:]

concurso_loto_facil = []
del concurso_loto_facil[:]

concurso_loto_mania = []
del concurso_loto_facil[:]

def estrutura_concurso(a):
    if jogo_csv == "mega_sena.csv":
        qt_dezenas = 6

    elif jogo_csv == "loto_facil.csv":
        qt_dezenas = 15

    elif jogo_csv == "loto_mania.csv":
        qt_dezenas = 20

        
    dezenas = []
    del dezenas[:]
    d = 2

    aposta = {
            "concurso": int(a[0]),
            "data": str(a[1])
            }
    for p in range(qt_dezenas):

        dezenas.append(int(a[d]))
        d = d + 1

    aposta["dezenas"] = sorted(dezenas)
            
    return aposta


with open(jogo_csv, newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if jogo_csv == "assets/mega_sena.csv":
            concurso_mega.append(estrutura_concurso(row))

        elif jogo_csv == "assets/loto_facil.csv":
            concurso_loto_facil.append(estrutura_concurso(row))

        elif jogo_csv == "assets/loto_mania.csv":
            concurso_loto_mania.append(estrutura_concurso(row))

        i = i + 1
        

def quantas_apareceu(dezena):
    quantidade = 0
    for a in range(i):
        if jogo_csv == "mega_sena.csv":
            quantidade = quantidade + concurso_mega[a]["dezenas"].count(dezena)

        if jogo_csv == "loto_facil.csv":
            quantidade = quantidade + concurso_loto_facil[a]["dezenas"].count(dezena)

        if jogo_csv == "loto_mania.csv":
            quantidade = quantidade + concurso_loto_mania[a]["dezenas"].count(dezena)

    return quantidade

def conjuntos_repetidos(a,b):
    dezenas = []
    del dezenas[:]
    
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i] == b[k]:
                dezenas.append(a[i])

                
    return sorted(dezenas)

conj = [5,33,52]

conc = 0
contador = 0
repeticao = 0
# for i in range(i):
for i in range(len(conj)):
    if concurso_mega[conc]["dezenas"].count(conj[i]):
        contador = contador + 1
if contador == len(conj):
    repeticao = repeticao + 1

print(repeticao)

# if len(conj) >= 4:
#     conjuntos={
#         "conjunto": conj,
#         "repeticoes_conjunto":0,
#         "concursos_conjunto": []
#         }
    





# print(concurso_mega[0])
# print(concurso_loto_facil[0])
# print(concurso_loto_mania[20])
# conj = conjuntos_repetidos(concurso_mega[0]["dezenas"],concurso_mega[1]["dezenas"])
# print(conj)
