# -*- coding: utf-8 -*-
import pandas as pd

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
y = base.iloc[:, 1].values

# Criando o Modelo
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)
score = regressor.score(X, y)

# Grafico 
import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor.predict(X), color = 'red')
plt.title('Regressao com Arvores de Decisao')
plt.xlabel('Idade')
plt.ylabel('Custo')

import numpy as np
X_teste = np.arange(min(X), max(X), 0.1)
X_teste = X_teste.reshape(-1, 1)
plt.scatter(X, y)
plt.plot(X_teste, regressor.predict(X_teste), color = 'red')
plt.title('Regressao com Arvores de Decisao')
plt.xlabel('Idade')
plt.ylabel('Custo')


# Predicao
idade_predicao = 40
regressor.predict(np.array(idade_predicao).reshape(1, -1))