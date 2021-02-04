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

# Treinamento do algoritmo
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
resultados = cross_val_score(classificador, previsores, classe, cv=10)
media = resultados.mean()
desvio = resultados.std()

