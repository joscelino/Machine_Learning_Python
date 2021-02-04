# -*- coding: utf-8 -*-
# Importacao das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carregamento da base de dados
base = pd.read_csv('plano_saude2.csv')

X = base.iloc[: , 0:1].values
y = base.iloc[:, 1:2].values

# Normalizacao dos dados para Kernel RBF
scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)

scaler_y = StandardScaler()
y = scaler_y.fit_transform(X)

# Kernel Linear
regressor_linear = SVR(kernel = 'linear')
regressor_linear.fit(X, y.ravel())

# Visualizar no grafico
plt.scatter(X, y)
plt.plot(X, regressor_linear.predict(X), color = 'red')
# Score
regressor_linear.score(X, y)

# Kernel  poly
regressor_poly = SVR(kernel = 'poly', degree = 3, gamma = 'auto')
regressor_poly.fit(X, y.ravel())

# Visualizar no grafico
plt.scatter(X, y)
plt.plot(X, regressor_poly.predict(X), color = 'red')
# Score
regressor_poly.score(X, y)

# Kernel RBF
regressor_rbf = SVR(kernel = 'rbf', gamma = 'auto')
regressor_rbf.fit(X, y.ravel())

# Visualizar no grafico
plt.scatter(X, y)
plt.plot(X, regressor_rbf.predict(X), color = 'red')
# Score
regressor_rbf.score(X, y)

## Revisar abaixo

previsao1 = regressor_linear.predict(scaler_x.transform(np.array(40).reshape(1, -1)))
scaler_y.inverse_transform(np.array(previsao1).reshape(1, -1))
previsao2 = scaler_y.inverse_transform(regressor_poly.predict(scaler_x.transform(np.array(40).reshape(1, -1))))
previsao3 = scaler_y.inverse_transform(regressor_rbf.predict(scaler_x.transform(np.array(40).reshape(1, -1))))
