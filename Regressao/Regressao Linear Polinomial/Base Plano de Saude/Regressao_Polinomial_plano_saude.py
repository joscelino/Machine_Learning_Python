# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
y = base.iloc[:, 1].values

# Regressao Lienar Simples
from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(X, y)
score1 = regressor1.score(X, y)

# Previsao com 1 valor
regressor1.predict(np.array(40).reshape(1, -1))

# Grafico da Regressao Linear
import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor1.predict(X), color = 'red')
plt.title('Regressao Linear')
plt.xlabel('Idade')
plt.ylabel('Custo')

# Regressao Polinomial
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 5)
X_poly = poly.fit_transform(X)
regressor2 = LinearRegression()
regressor2.fit(X_poly, y)
score2 = regressor2.score(X_poly, y)

# Previsao com 1 valor
regressor2.predict(poly.transform(np.array(40).reshape(1, -1)))

# Grafico da Regressao Polinomial
plt.scatter(X, y)
plt.plot(X, regressor2.predict(poly.fit_transform(X)), color = 'red')
plt.title('Regressao Linear Polinomial')
plt.xlabel('Idade')
plt.ylabel('Custo')