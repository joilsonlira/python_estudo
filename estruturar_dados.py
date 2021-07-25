import csv

jogo_csv = "assets/csv/mega_sena.csv"


concurso_mega = []
del concurso_mega[:]

concurso_loto_facil = []
del concurso_loto_facil[:]

concurso_loto_mania = []
del concurso_loto_facil[:]


def estrutura_concurso(a):
    if jogo_csv == "assets/csv/mega_sena.csv":
        qt_dezenas = 6

    elif jogo_csv == "assets/csv/loto_facil.csv":
        qt_dezenas = 15

    elif jogo_csv == "assets/csv/loto_mania.csv":
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
        if jogo_csv == "assets/csv/mega_sena.csv":
            concurso_mega.append(estrutura_concurso(row))

        elif jogo_csv == "assets/csv/loto_facil.csv":
            concurso_loto_facil.append(estrutura_concurso(row))

        elif jogo_csv == "assets/csv/loto_mania.csv":
            concurso_loto_mania.append(estrutura_concurso(row))

        i = i + 1
        