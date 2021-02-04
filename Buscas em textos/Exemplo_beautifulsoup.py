# -*- coding: utf-8 -*-
# pip install beautifulsoup4
"""
Exemplo de webscrap, busca de textos em paginas web
"""
# Importacao das bibliotecas
import urllib3
from bs4 import BeautifulSoup

# Desabilitando warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Criacao de variavel
http = urllib3.PoolManager() ''' Pool manager permite fazer multiplas requisicoes para multiplos hosts'''

# Definindo a pagina onde dados serao buscados
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o')

# Verificar se houve conexao (resultado deve ser 200)
pagina.status

# Pegar dados html da pagina
pagina.data

# Criar variavel
sopa = BeautifulSoup(pagina.data, "lxml")
sopa

# Nome da pagina
sopa.title.string

# Links que existem na pagina
links = sopa.find_all('a')
len(links)
for link in links:
    print(link.get('href'))
    print(link.contents)