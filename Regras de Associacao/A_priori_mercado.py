# -*- coding: utf-8 -*-
# Importando bibliotecas
import pandas as pd
from apyori import apriori

# Importando base de dados
base = pd.read_csv('mercado.csv', header = None)

# Criando lista de transacoes
transacoes = []

for i in range(0, 10):
    transacoes.append([str(base.values[i, j]) for j in range(0, 4)])

# Geracao das regras de associacao
regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.8, min_lift = 2, min_lenght = 2)

resutados = list(regras)
resutados

resultados2 = [list(x) for x in resutados]
resultado_formatado = []
for j in range(0, 3):
    resultado_formatado.append([list(x) for x in resultados2[j][2]])
resultado_formatado

