# -*- coding: utf-8 -*-
"""
Aplicacao do algoritmo a priori em base de dados real vestibular
Note-se que o algoritmo nao foi capaz de gerar padroes relevantes 
"""
# Importando bibliotecas
import pandas as pd
from apyori import apriori

# Importando base de dados
base = pd.read_csv('vestibular.csv', header = None)
del base[1] 
del base[6] 
del base[7] 
del base[13] 
del base[14] 
del base[15] 

# Criando lista de transacoes
transacoes = []

for i in range(0, 1326):
    transacoes.append([str(base.values[i, j]) for j in range(0, 12)])

# Geracao das regras de associacao
regras = apriori(transacoes, min_support = 0.09, min_confidence = 0.9, min_lift = 2, min_lenght = 2)

resutados = list(regras)
resutados

resultados2 = [list(x) for x in resutados]
resultado_formatado = []
for j in range(0, 5):
    resultado_formatado.append([list(x) for x in resultados2[j][2]])
resultado_formatado


