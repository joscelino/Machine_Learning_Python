# -*- coding: utf-8 -*-
import pandas as pd

base = pd.read_csv('plano_saude.csv')

X = base.iloc[:, 0].values
y = base.iloc[:, 1].values

# Verificacao da correlacao
import numpy as np
correlacao = np.corrcoef(X, y)

X = X.reshape(-1,1)

# Treinamento do Modelo
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# Coefeciente Angular
regressor.intercept_

# Coeficiente Linear
regressor.coef_

# Plotando grafico
import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor.predict(X), color = 'red')
plt.title('Regressao linear simples')
plt.xlabel('Idade')
plt.ylabel('Custo')

previsao1 = regressor.predict(40)
previsao2 = regressor.intercept_ + regressor.coef_ * 40
score = regressor.score(X, y)

from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(regressor)
visualizador.fit(X, y)
visualizador.poof()
