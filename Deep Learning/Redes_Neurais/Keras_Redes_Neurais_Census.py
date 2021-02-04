# -*- coding: utf-8 -*-
import pandas as pd
base = pd.read_csv('census.csv')                                        # carrega arquivo de dados
base.describe()                                                         # mostra algumas estatisticas do arquivo (usar Crtl + enter)

previsores = base.iloc[:, 0:14].values                                  # separa dados previsores da base de dados em uma variavel
classe = base.iloc[:, 14].values                                        # separa vaores de saida da base de dados

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_previsores = LabelEncoder()

previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[:, 6])
previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[:, 7])
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[:, 13])

from sklearn.compose import ColumnTransformer
onehotencoder = ColumnTransformer([("Previsores", OneHotEncoder(), [1, 3, 5, 6, 7, 8, 9, 13])], remainder = 'passthrough')
previsores = onehotencoder.fit_transform(previsores).toarray()

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

# importação da biblioteca
import keras
from keras.models import Sequential
from keras.layers import Dense
classificador = Sequential()
classificador.add(Dense(units = 55, activation = 'relu', input_dim = 108))
classificador.add(Dense(units = 55, activation = 'relu'))

# Camada de Saida
classificador.add(Dense(units = 1, activation = 'sigmoid'))

# Compilacao da rede
classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 10, epochs = 100)

# criacao do classificador
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste,previsoes)
matriz = confusion_matrix(classe_teste,previsoes)
