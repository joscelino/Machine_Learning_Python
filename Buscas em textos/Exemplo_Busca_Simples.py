# -*- coding: utf-8 -*-
"""
Exemplo de extracao de conteudo
"""
# Importacao das bibliotecas
import urllib3
from bs4 import BeautifulSoup

# Criacao de variavel
http = urllib3.PoolManager() ''' Pool manager permite fazer multiplas requisicoes para multiplos hosts'''

# Definindo a pagina onde dados serao buscados
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Lista_de_linguagens_de_programa%C3%A7%C3%A3o')

# Verificar se houve conexao (resultado deve ser 200)
pagina.status

sopa = BeautifulSoup(dados_pagina.data, "lxml")
for tags in sopa(['script', 'style']):
    tags.decompose()
conteudo = ' '.join(sopa.stripped_strings)
    

