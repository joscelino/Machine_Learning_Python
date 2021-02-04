# -*- coding: utf-8 -*-
import pandas as pd
from keras.layers import Dense, Dropout, Activation, Input
from keras.models import Model

base = pd.read_csv('games.csv')

# Exclusao de colunas que nao serao utilizadas
base = base.drop('Other_Sales', axis=1)
base = base.drop('Global_Sales', axis=1)
base = base.drop('Developer', axis=1)

# Excluindo linhas com valores NaN
base = base.dropna(axis = 0) 

# Apagando dados irrelevantes
base = base.loc[base['NA_Sales'] > 1]
base = base.loc[base['EU_Sales'] > 1]

# Verificando a variabilidade do atributo
base['Name'].value_counts()
nome_jogos = base.Name
base = base.drop('Name', axis=1)

# Divisao de previsores 
previsores = base.iloc[:, [0, 1, 2, 3, 7, 8, 9, 10, 11]].values
venda_na = base.iloc[:, 4].values
venda_eu = base.iloc[:, 5].values
venda_jp = base.iloc[:, 6].values

# Pre-processamento dos dados
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])


from sklearn.compose import ColumnTransformer
onehotencoder = ColumnTransformer([("Previsores", OneHotEncoder(), [0, 2, 3, 8])], remainder = 'passthrough')
previsores = onehotencoder.fit_transform(previsores).toarray()

# Criacao da Rede Neural
# Camada de entrada
camada_entrada = Input(shape=(61, ))

# Camadas Ocultas
camada_oculta1 = Dense(units = 32, activation = 'sigmoid')(camada_entrada)
camada_ocuta2 = Dense(units = 32, activation = 'sigmoid')(camada_oculta1)

# Camadas de Saida
camada_saida_1 = Dense(units = 1, activation = 'linear')(camada_ocuta2)
camada_saida_2 = Dense(units = 1, activation = 'linear')(camada_ocuta2)
camada_saida_3 = Dense(units = 1, activation = 'linear')(camada_ocuta2)

regressor = Model(inputs = camada_entrada, 
                  outputs = [camada_saida_1, camada_saida_2, camada_saida_3])

# Compilacao da rede Neural
regressor.compile(optimizer = 'adam',
                  loss = 'mse')

# Treinamento da Rede
regressor.fit(previsores, [venda_na, venda_eu, venda_jp],
              epochs = 5000, batch_size = 100)

previsao_na, previsao_eu, previsao_jp = regressor.predict(previsores)
