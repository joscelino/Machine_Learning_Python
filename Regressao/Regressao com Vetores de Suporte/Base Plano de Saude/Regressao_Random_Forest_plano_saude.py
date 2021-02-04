# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
y = base.iloc[:, 1].values

# Criando o Modelo
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 15)
regressor.fit(X, y)
score = regressor.score(X, y)

# Grafico
import numpy as np
X_teste = np.arange(min(X), max(X), 0.1)
X_teste = X_teste.reshape(-1, 1)
plt.scatter(X, y)
plt.plot(X_teste, regressor.predict(X_teste), color = 'red')
plt.title('Regressao com Arvores de Decisao')
plt.xlabel('Idade')
plt.ylabel('Custo')
