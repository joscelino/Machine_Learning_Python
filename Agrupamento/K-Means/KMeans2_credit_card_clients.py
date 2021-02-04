# -*- coding: utf-8 -*-
#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Importacao de dados
base = pd.read_csv('../../dados/credit_card_clients.csv', header = 1)
base.head(10)

# Preparando dados
base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3'] +base['BILL_AMT4']

# Base para agrupamento
X = base.iloc[: ,[1, 2, 3, 4, 5, 25]].values
# Normalizando os dados
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Definindo o numero de clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Grafico de Elbow')
plt.xlabel('Numero de clusters')
plt.ylabel('WCSS')
plt.show()

# Criando o Agrupamento
kmeans = KMeans(n_clusters = 4, random_state = 0)
previsoes = kmeans.fit_predict(X)

''' Para este caso nao foi possivel a geracao de grafico do agrupamento'''

# Listando 
lista_clientes = np.column_stack((base, previsoes))

# Ordenando a lista
lista_clientes = lista_clientes[lista_clientes[: , 26].argsort()]