# -*- coding: utf-8 -*-
# Importando bibliotecas
import pandas as pd
from apyori import apriori

# Importando base de dados
base = pd.read_csv('mercado_real.csv', header = None)

# Criando lista de transacoes
transacoes = []

for i in range(0, 7501):
    transacoes.append([str(base.values[i, j]) for j in range(0, 20)])

# Geracao das regras de associacao
regras = apriori(transacoes, min_support = 0.003, min_confidence = 0.5, min_lift = 3, min_lenght = 2)

resutados = list(regras)
resutados

resultados2 = [list(x) for x in resutados]
resultado_formatado = []
for j in range(0, 5):
    resultado_formatado.append([list(x) for x in resultados2[j][2]])
resultado_formatado
