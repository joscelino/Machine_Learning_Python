# -*- coding: utf-8 -*-
"""
Exemplo de remocao de tags HTML
"""
# Importacao de bibliotecas
import urllib3
from bs4 import BeautifulSoup

# Criacao de variavel
http = urllib3.PoolManager() 

# Definindo a pagina onde dados serao buscados
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o')

# Criar variavel
sopa = BeautifulSoup(pagina.data, "lxml")

# Limpeza de tags
for tags in sopa(['script', 'style']):
    tags.decompose()

conteudo = ' '.join(sopa.stripped_strings)
