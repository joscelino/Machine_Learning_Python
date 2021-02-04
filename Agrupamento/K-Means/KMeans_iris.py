# -*- coding: utf-8 -*-
#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../../dados/iris.csv')
df.head(10)

x = df.iloc[:, [0,1]].values

# Normalizacao dos dados
normalizador = StandardScaler()
x_normalizado = normalizador.fit_transform(x)

# Gerando o Elbow 
Error =[]
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i).fit(x_normalizado)
    kmeans.fit(x_normalizado)
    Error.append(kmeans.inertia_)
    
import matplotlib.pyplot as plt
plt.plot(range(1, 11), Error)
plt.title('Elbow method')
plt.xlabel('No of clusters')
plt.ylabel('Error')
plt.show()

# Agrupamento em 3 clusters
kmeans3 = KMeans(n_clusters=3)
y_kmeans3 = kmeans3.fit_predict(x_normalizado)
centroides_k3 = kmeans3.cluster_centers_
rotulos_k3 = kmeans3.labels_
print(y_kmeans3)
plt.scatter(x_normalizado[:,0], x_normalizado[:, 1], c=y_kmeans3, cmap = 'rainbow')
plt.scatter(centroides_k3[:, 0], centroides_k3[:, 1], marker = "x")
plt.legend()
plt.show()

# Listando 
lista = np.column_stack((df, y_kmeans3))

# Agrupamento em 5 clusters
kmeans5 = KMeans(n_clusters=5)
y_kmeans5 = kmeans5.fit_predict(x_normalizado)
centroides_k5 = kmeans5.cluster_centers_
rotulos_k5 = kmeans5.labels_
print(y_kmeans5)
plt.scatter(x_normalizado[:,0], x_normalizado[:, 1], c=y_kmeans5, cmap = 'rainbow')
plt.scatter(centroides_k5[:, 0], centroides_k5[:, 1], marker = "x")

# Listando os agrupamentos
lista = np.column_stack((df, y_kmeans5))