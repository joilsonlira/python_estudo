import csv

jogo_csv = ["assets/csv/mega_sena.csv","assets/csv/loto_facil.csv","assets/csv/loto_mania.csv"]


concurso_mega = []
del concurso_mega[:]

concurso_loto_facil = []
del concurso_loto_facil[:]

concurso_loto_mania = []
del concurso_loto_facil[:]


def estrutura_concurso(loteria,aposta_lista):
    """[Informando o indice da loteria e o indice da aposta, a função retorna todas as apostas estruturadas e ordenadas.]

    Args:
        loteria (INT): [0 para Megasena; 1 para LotoFacil; 2 para LotoMania]
        aposta_lista (LIST): [lista com uma aposta(concurso, data, dezena 1, dezena 2 ...) da loteria escolhida]

    Returns:
       aposta [DICT]: [retorna um dicionario estruturado: concurso, data, dezenas (ordenadas do menor ao meior digito)]
    """

    if jogo_csv[loteria] == "assets/csv/mega_sena.csv":
        qt_dezenas = 6

    elif jogo_csv[loteria] == "assets/csv/loto_facil.csv":
        qt_dezenas = 15

    elif jogo_csv[loteria] == "assets/csv/loto_mania.csv":
        qt_dezenas = 20

    #limpa a lista
    dezenas = []
    del dezenas[:]

    #determina o inicio de contagem da lista de dezenas apartir do index 2 da lista que esta a aposta
    d = 2

    aposta = {
            "concurso": int(aposta_lista[0]),
            "data": str(aposta_lista[1])
            }
    for p in range(qt_dezenas):

        dezenas.append(int(aposta_lista[d]))
        d = d + 1

    aposta["dezenas"] = sorted(dezenas)
            
    return aposta


def csv_dados(loteria):
    """[Função que retorna uma lista com todos os concursos de uma determinada loteria usando os indices da lista de loterias como valor entrada]

    args:
        loteria (INT): [0 para Megasena; 1 para LotoFacil; 2 para LotoMania]

    Returns:
       concurso [LIST]: [Retornar uma lista com todos os jogos da loteria escolhida, organizada com dicionario. concurso, data, dezenas]
    """

    #limpa as listas
    concurso_mega=[]
    del concurso_mega[:]

    concurso_loto_facil=[]
    del concurso_loto_facil[:]

    concurso_loto_mania=[]
    del concurso_loto_mania[:]

    with open(jogo_csv[loteria], newline='') as f:
        reader = csv.reader(f)
        i = 0
        
        if jogo_csv[loteria]:
            for row in reader:
                concurso_mega.append(estrutura_concurso(loteria,row))
                i = i + 1
            return concurso_mega
            

        elif jogo_csv[loteria]:
            for row in reader:
                concurso_loto_facil.append(estrutura_concurso(loteria,row))
                i = i + 1
            return concurso_loto_facil
                

        elif jogo_csv[loteria]:
            for row in reader:
                concurso_loto_mania.append(estrutura_concurso(loteria,row))
                i = i + 1
            return concurso_loto_mania
            


                

