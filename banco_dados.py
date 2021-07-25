'''

****ESCOPO GERAL****
1- Estabelecer link com origem dos dados [FEITO]
2- Isolar e Limpar as dezenas
3- classificar ou segmentar dezenas

'''
#imports
import csv
import sqlite3

#conecotor
conn = sqlite3.connect('DB/lot_base.db')
cursor = conn.cursor()

with open('mega_sena.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO megasena (data_concurso, d1, d2, d3, d4, d5, d6)
        VALUES (?,?,?,?,?,?,?)
        
        """,(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        i = i + 1
        print("MEGASENA - concurso:",i)


with open('loto_facil.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO lotofacil (data_concurso, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
        i = i + 1
        print("LOTOFACIL - concurso:",i)


with open('loto_mania.csv', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        
        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO lotomania (data_concurso, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]))
        i = i + 1
        print("LOTOMANIA - concurso:",i)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
