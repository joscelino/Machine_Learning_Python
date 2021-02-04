# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pandas as pd 
base = pd.read_csv('original.csv')          # carrega arquivo de dados
base.describe()                             # mostra algumas estatisticas do arquivo (usar Crtl + enter)
base.loc[base['age'] <0]                    # atributo loc do pandas localiza dado
# tecnicas para tratar valores errados em 'age'
# apagar os dados (nao se trata de boa tecnica)
base.drop('age', 1, inplace=True)
# apagar somente linhas com problema (nao se trata de boa tecnica)
base.drop(base[base.age < 0].index, inplace=True)
# preencher os valores manualmente (nem sempre sera viavel, apesar de ser tecnica mais interessante)
# preencher os valores automaticamente (com media, por exemplo)
base.mean()                                 # traz medias de todos os atributos da base
base['age'].mean()                          # traz media do atributo especifico
base['age'][base.age > 0].mean()            # exclui valores abaixo de zero do calculo da media
base.loc[base.age < 0, 'age'] = base['age'][base.age > 0].mean()        # atribui novos valores 

pd.isnull(base['age'])                      # localiza valores NULL imprimindo toda lista 
base.loc[pd.isnull(base['age'])]            # localiza somente valores NULL

previsores = base.iloc[:, 1:4].values       # separa dados previsores da base de dados em uma variavel
classe = base.iloc[:, 4].values             # separa vaores de saida da base de dados

# Dica: Crtl + I traz ajuda sobre comandos
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0) # calcula novos valores para dados incorretos
imputer = imputer.fit(previsores[:, 0:3])
previsores[:,0:3] = imputer.transform(previsores[:, 0:3]) # Substitui dados incorretos

# Abaixo sera feita o escalonamento (Padronizacao / Normalizacao) dos atributos 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

