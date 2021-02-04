import re
import nltk 
import urllib3
import pymysql
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from nltk.stem import RSLPStemmer

# Criando dicionario com dados de conexao
conecta_sql= {
    'host' :'localhost',
    'user' : '',
    'passwd' : '',
    'db' : ''
    }

# Inclusao das palavras no documento
def inserePalavraLocalizacao(idurl, idpalavra, localizacao):
    conexao = pymysql.connect(conecta_sql, autocommit = True)
    cursor = conexao.cursor()
    cursor.execute('insert into palavra_localizacao (idurl, idpalavra, localizacao) values (%s, %s, %s)', (idurl, idpalavra, localizacao))
    idpalavra_localizacao = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpalavra_localizacao

# Mapeamento das urls direcionadas
def insertUrlLigacao(idurl_origem, idurl_destino):
    conexao = pymysql.connect(conecta_sql, autocommit = True)
    cursor = conexao.cursor()
    cursor.execute('insert into url_ligacao (idurl_origem, idurl_destino) values (%s, %s)', (idurl_origem, idurl_destino))
    idurl_ligacao = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idurl_ligacao

#insertUrlLigacao(1, 2)   

# Inserindo o id da Palavra   
def insertUrlPalavra(idpalavra, idurl_ligacao):
    conexao = pymysql.connect(conecta_sql, autocommit = True)
    cursor = conexao.cursor()
    cursor.execute('insert into url_palavra (idpalavra, idurl_ligacao) values (%s, %s)', (idpalavra, idurl_ligacao))
    idurl_palavra = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idurl_palavra

#insertUrlPalavra(244, 1) 

# Verificando ligacao entre duas urls
def getIdUrlLigacao(idurl_origem, idurl_destino):
    idurl_ligacao = - 1
    conexao = pymysql.connect(conecta_sql)
    cursor = conexao.cursor()
    cursor.execute('select idurl_ligacao from url_ligacao where idurl_origem = %s and idurl_destino = %s', (idurl_origem, idurl_destino))
    if cursor.rowcount > 0:
        idurl_ligacao = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return idurl_ligacao

#getIdUrlLigacao(1, 2)
    
def getIdUrl(url):
    idurl = - 1
    conexao = pymysql.connect(conecta_sql, use_unicode = True, charset = 'utf8mb4')
    cursor = conexao.cursor()
    cursor.execute('select idurl from urls where url = %s', url)
    if cursor.rowcount > 0:
        idurl = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return idurl
  
#getIdUrl('https://pt.wikipedia.org/wiki/International_Standard_Serial_Numb')

# Insercao das palavras no indice do Banco de Dados MySql
def inserePalavra(palavra):
    conexao = pymysql.connect(conecta_sql, autocommit = True, use_unicode = True, charset = 'utf8mb4')
    cursor = conexao.cursor()
    cursor.execute("insert into palavras (palavra) values (%s)", palavra)
    idpalavra = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpalavra

# Verificando palavras indexadas no banco de dados MySql
def palavraIndexada(palavra):
    retorno = - 1 # Nao existe a palavra no indice
    conexao = pymysql.connect(conecta_sql, use_unicode = True, charset = 'utf8mb4')
    cursor = conexao.cursor()
    cursor.execute("select idpalavra from palavras where palavra = %s",palavra)
    if cursor.rowcount > 0:
        #print("Palavra ja cadastrada!")
        retorno = cursor.fetchone()[0]
    else:
        #print("Palavra nao cadastrada!")
        retorno
    cursor.close()
    conexao.close()
    return retorno

#palavraIndexada("teste")

# Funcao para preencher a tabela do banco de dados MySql
def inserePagina(url):
    conexao = pymysql.connect(conecta_sql, autocommit = True, use_unicode = True, charset = 'utf8mb4')
    cursor = conexao.cursor()
    cursor.execute("insert into urls (url) values (%s)", url)
    idpagina = cursor.lastrowid # Retorna ultimo id e nao funciona para multi-usuarios
    cursor.close()
    conexao.close()
    return idpagina

# Funcao de Verificacao de paginas indexadas no banco de dados MySql
def paginaIndexada(url):
    retorno = - 1 # Nao existe a pagina
    conexao = pymysql.connect(conecta_sql)
    cursorurl = conexao.cursor()
    cursorurl.execute('select idurl from urls where url = %s', url)
    if cursorurl.rowcount > 0:
        #print("Url cadastrada!")
        idurl = cursorurl.fetchone()[0]
        cursorPalavra = conexao.cursor()
        cursorPalavra.execute('select idurl from palavra_localizacao where idurl= %s', idurl)
        if cursorPalavra.rowcount > 0:
            #print("Url com palavras cadastradas!")
            retorno = - 2 # existe a pagina com palavras cadastradas
        else:
            #print("Url sem palavras cadastradas!")
            retorno = idurl # existe a pagina sem  palavras cadastradas
        cursorPalavra.close()
    else: 
        print("Url nao cadastrada!")
        
    cursorurl.close()
    conexao.close()
    return retorno

# Funcao para separar palavras
def separaPalavras(texto):
    stop = nltk.corpus.stopwords.words('portuguese')
    stemmer = RSLPStemmer()
    splitter = re.compile('\\W+')
    lista_palavras = []
    lista  = [p for p in splitter.split(texto) if p != '']
    for p in lista:
        if p.lower() not in stop:
            if len(p) > 1:
                lista_palavras.append(stemmer.stem(p).lower())
    return lista_palavras

# Gravacao da ligacao entre urls e palavras
def urlLigaPalavra(url_origem, url_destino):
    # Pre processamento dos textos
    texto_url = url_destino.replace('_', '')
    palavras = separaPalavras(texto_url)
    idurl_origem = getIdUrl(url_origem)
    idurl_destino = getIdUrl(url_destino)
    if idurl_destino == - 1:
        idurl_destino = inserePagina(url_destino)
    if idurl_origem == idurl_destino:
        return
    if getIdUrlLigacao(idurl_origem, idurl_destino) > 0:
        return
    idurl_ligacao = insertUrlLigacao(idurl_origem, idurl_destino)
    for palavra in palavras:
        idpalavra = palavraIndexada(palavra)
        if idpalavra == - 1:
            idpalavra = inserePalavra(palavra)
        insertUrlPalavra(idpalavra, idurl_ligacao)
    
# Funcao para decomposicao
def getTexto(sopa):
    # Limpeza de tags
    for tags in sopa(['script', 'style']):
        tags.decompose()
        return  ' '.join(sopa.stripped_strings)

# Indexador
def indexador(url, sopa):
    indexada = paginaIndexada(url)
    if indexada == - 2:
        print('Url ja indexada!')
        return
    elif indexada == - 1:
        idnova_pagina = inserePagina(url)
    elif indexada > 0:
        idnova_pagina = indexada
    print('Indexando '+url)
    
    texto = getTexto(sopa)
    palavras = separaPalavras(texto)
    for i in range(len(palavras)):
        palavra = palavras[i]
        idpalavra = palavraIndexada(palavra)
        if idpalavra == - 1:
            inserePalavra(palavra)
        inserePalavraLocalizacao(idnova_pagina, idpalavra, i)
        
# Definindo a funcao de Crawler
def crawl(paginas, profundidade):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # xclui avisos de erros 
    for i in range(profundidade):
        novas_paginas = set() # Armazena todos os links de uma pagina
        for pagina in paginas:
            http = urllib3.PoolManager()
            try:
                dados_pagina = http.request('GET', pagina)
            except :
                print('Erro ao abrir a pagina: '+ pagina)
                continue
            
            sopa = sopa = BeautifulSoup(dados_pagina.data, "lxml")
            indexador(pagina, sopa)
            links = sopa.find_all('a')
            contador = 1
            for link in links:
                #print(str(link.content)+" - " + str(link.get('href')))
                #print(link.attrs)
                #print('\n')
                if ('href' in link.attrs):
                    url = urljoin(pagina, str(link.get('href')))
                    #if url != link.get('href'):
                        #print(url)
                        #print(link.get('href'))
                    if url.find("'") != -1:
                        continue
                    #print(url)
                    url.split('#')[0]
                    #print(url)
                    #print('\n')
                    if url[0:4] == 'http':
                        novas_paginas.add(url)
                    urlLigaPalavra(pagina, url)
                        
                    contador = contador + 1
            paginas = novas_paginas
            print(contador)

# Listando paginas para o metodo:
listapaginas = ['https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o']#'https://www.climatempo.com.br/']
#['http://e-negocioscidadesp.prefeitura.sp.gov.br/', 'https://www.comprasgovernamentais.gov.br/'] #'http://www.pregao.sp.gov.br/'] #, 'https://www.imprensaoficial.com.br/', 

# Testando
crawl(listapaginas, 2)
