# -*- coding: utf-8 -*-
"""
Aplicando regras de associacao a uma base de dados real de pizzaria
"""
# Importando bibliotecas
import pandas as pd
from apyori import apriori

# Importando base de dados
base = pd.read_csv('base_pizzaria.csv', header = None)
del base[4] # excluir a 3 tb

# Criando lista de transacoes
transacoes = []

for i in range(0, 1000):
    transacoes.append([str(base.values[i, j]) for j in range(0, 5)])

# Geracao das regras de associacao
regras = apriori(transacoes, min_support = 0.005, min_confidence = 0.9, min_lift = 2, min_lenght = 2)

resutados = list(regras)
resutados

resultados2 = [list(x) for x in resutados]
resultado_formatado = []
for j in range(0, 6):
    resultado_formatado.append([list(x) for x in resultados2[j][2]])
resultado_formatado
