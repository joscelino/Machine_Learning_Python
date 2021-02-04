# -*- coding: utf-8 -*-
# conda install urllib3
# pip install beautifulsoup4
"""
Exemplo de webscrap, busca de textos em paginas web
"""
# Importacao das bibliotecas
import urllib3

# Criacao de variavel
http = urllib3.PoolManager() ''' Pool manager permite fazer multiplas requisicoes para multiplos hosts'''

# Definindo a pagina onde dados serao buscados
pagina = http.request('GET', 'http://www.pregao.sp.gov.br/')

# Verificar se houve conexao (resultado deve ser 200)
pagina.status

# Pegar dados html da pagina
pagina.data


