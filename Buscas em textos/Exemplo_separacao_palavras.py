# -*- coding: utf-8 -*-
"""
Separacao de caracteres
"""
# Importacao das bibliotecas
import re
import nltk 
#nltk.download()

# Stop words
stop1 = ['é']
stop2 = nltk.corpus.stopwords.words('portuguese')

# Criacao das variaveis
splitter = re.compile('\\W+')
lista_palavras = []

# Criando lista de palavras conforme regras
lista  = [p for p in splitter.split('Este lugar é apavorante a b c c++') if p != '']

# Visualizando resultados
for p in lista:
    if p.lower() not in stop2:
        if len(p) > 1:
            lista_palavras.append(p.lower())

