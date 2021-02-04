# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

base = pd.read_csv('credit_data.csv')
base.loc[base.age < 0, 'age'] = 40.92 # Correcao das idades negativas

# Separacao de previsores e classe               
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

# Pre processamento dos valores faltantes
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

# Efetuando o escalonamento (normalizacao)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# Divisao de previsores de treinamento e testes
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

# Predicao
import keras
from keras.models import Sequential
from keras.layers import Dense

# criacao do classificador
classificador = Sequential()
classificador.add(Dense(units = 2, activation = 'relu', input_dim = 3))
classificador.add(Dense(units = 2, activation = 'relu'))
classificador.add(Dense(units = 1, activation = 'sigmoid'))

# Compilando Rede Neural
classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Treinamento da Rede Neural
classificador.fit(previsores_treinamento,classe_treinamento, batch_size = 10, epochs = 100)

# Previsoes
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)

# Matriz de Confusao
from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste,previsoes)
matriz = confusion_matrix(classe_teste,previsoes)

