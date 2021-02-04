import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

base = pd.read_csv('../../dados/credit_card_clients.csv', header = 1)
base.head(10)

base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3'] +base['BILL_AMT4']

X = base.iloc[:, [1, 25]].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Definicao do Modelo
dbscan = DBSCAN(eps=0.2, min_samples=10)
previsoes = dbscan.fit_predict(X)

# Verificando numero de grupos
unicos, quantidade = np.unique(previsoes, return_counts=True)

# Gerando o grafico
plt.scatter(X[previsoes == 0, 0], X[previsoes == 0, 1], s=100, c='red', label = 'Cluster 1')
plt.scatter(X[previsoes == 1, 0], X[previsoes == 1, 1], s=100, c='green', label = 'Cluster 2')
plt.scatter(X[previsoes == 2, 0], X[previsoes == 2, 1], s=100, c='orange', label = 'Cluster 3')
#plt.scatter(X[previsoes == 3, 0], X[previsoes == 3, 1], s=100, c='blue', label = 'Cluster 4')
plt.xlabel('Limite do Cartao de Credito')
plt.ylabel("Gastos")
plt.legend()
plt.show()

# Listando s agrupamentos
lista_clientes = np.column_stack((base, previsoes))

# Ordenando a lista
lista_clientes = lista_clientes[lista_clientes[:, 26].argsort()]