# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:08:08 2020

@author: Joscelino
"""

import pandas as pd  # carregando a biblioteca pandas

base = pd.read_csv('risco_credito.csv') # importando o arquivo
previsores = base.iloc[:,0:4].values # iniciando o tratamento de dados
classe = base.iloc[:,4].values

# convertendo variaveis uma vez que o Naive Bayes nao aceita strings 
from sklearn.preprocessing import LabelEncoder 
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])

# Efetuando o Aprendizado de Maquina
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(previsores,classe)

# Predicao
# Historico bom, divida alta, sem garantias e renda > 35k
# historico ruim, divida alta, com garatias e renda < 15k
resultado = classificador.predict([[0,0,1,2], [3,0,0,0]])
print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)