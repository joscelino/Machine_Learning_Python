# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('house_prices.csv')

# Pre-processamento da base de dados
X = base.iloc[:, 3:19].values
y = base.iloc[:, 2].values

from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

# Criando o Modelo
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 100)
regressor.fit(X_treinamento, y_treinamento)

# Checando o score
score = regressor.score(X_treinamento, y_treinamento)

# Efetuando as previsoes
previsoes = regressor.predict(X_teste)

# Verificando a precisao
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_teste, previsoes)

# Score na base de Teste
regressor.score(X_teste, y_teste)