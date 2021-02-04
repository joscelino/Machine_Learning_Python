# -*- coding: utf-8 -*-
import pandas as np
import pandas as pd
import MetaTrader5 as mt5
import time

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()
##base = pd.read_excel('dolar.xlsx')
base = mt5.copy_rates_from_pos("WDOK20",mt5.TIMEFRAME_M1,0,1000)
mt5.shutdown()
for rate in base:
    print(base)
 
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(base)
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')


# Pre processamento dos valores faltantes
for i in range(999,0):
    if rates_frame['open'][i]<rates_frame['close'][i-1]:
        teste=-1
    elif rates_frame['open'][i]>rates_frame['close'][i-1]:
        teste=2
    elif rates_frame['open'][i]==rates_frame['close'][i-1]:
        teste=0
    print(teste)
    print(i)
    print(i-1)
    print(rates_frame['open'][i])
    print(rates_frame['close'][i-1])
    
previsores[:, 4:12] = imputer.transform(previsores[:, 4:12])
print(imputer.transform(previsores[:, 4:12]))

previsores = rates_frame.iloc[:, 1:7].values                                 # separa dados previsores da base de dados em uma variavel
classe = rates_frame.iloc[:, 0].values                                         # separa vaores de saida da base de dados

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_previsores = LabelEncoder()

previsores[:, 0] = labelencoder_previsores.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 2] = labelencoder_previsores.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 4] = labelencoder_previsores.fit_transform(previsores[:, 4])

onehotencoder = OneHotEncoder(categories='auto')
previsores = onehotencoder.fit_transform(previsores).toarray()

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

# Efetuando o escalonamento (normalizacao)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# Divisao de previsores de treinamento e testes
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

# Treinamento do algoritmo
# Treinamento do algoritmo
from sklearn.svm import SVC
classificador = SVC(kernel='sigmoid', random_state=1, C=1.0)
classificador.fit(previsores_treinamento,classe_treinamento)

# Efetuar a predicao
previsoes = classificador.predict(previsores_teste)

# Analise do nivel de acertos
from sklearn.metrics import confusion_matrix,accuracy_score
precisao = accuracy_score(classe_teste,previsoes)
matriz = confusion_matrix(classe_teste,previsoes)

