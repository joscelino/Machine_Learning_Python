# -*- coding: utf-8 -*-
"""
Consultas de uma palavra
"""
# Importacao das bibliotecas
import nltk 
import pymysql
from nltk.stem import RSLPStemmer

# Parametros de conexao no MySql
# TODO: Inserir lib decouple
host = 'localhost'
id_user = 'root'
password = 'JC137829'
data_base = 'indice'

   
# Capturando o id da pavalavra na consulta do MySQL
def getIdPalavra(palavra):
    retorno = -1
    stemmer = RSLPStemmer()
    conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)
    cursor = conexao.cursor()
    cursor.execute('select idpalavra from palavras where palavra = %s', stemmer.stem(palavra))
    if cursor.rowcount > 0:
        retorno = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return retorno

# Teste da funcao
# getIdPalavra('Programação')

# Buscando n numero de palavras
def buscaMaisPalavras(consulta):
    listacampos = 'p1.idurl'
    listatabelas = ''
    listaclausulas = ''
    palavrasid = []
    palavras = consulta.split(' ')
    numerotabela = 1
    for palavra in palavras:
        idpalavra = getIdPalavra(palavra)
        if idpalavra > 0:
            palavrasid.append(idpalavra)
            if numerotabela > 1:
                listatabelas += ','
                listaclausulas += ' and '
                listaclausulas += 'p%d.idurl = p%d.idurl and ' % (numerotabela - 1, numerotabela)
            listacampos += ', p%d.localizacao' % numerotabela
            listatabelas += ' palavra_localizacao p%d' % numerotabela
            listaclausulas += ' p%d.idpalavra = %d' % (numerotabela, idpalavra)
            numerotabela += 1
    consultacompleta = 'select %s from %s where %s'%(listacampos, listatabelas, listaclausulas)
    conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)
    cursor = conexao.cursor()
    cursor.execute(consultacompleta)
    linhas = [linha for linha in cursor]
    cursor.close()
    conexao.close()
    return linhas, palavrasid

# Teste da funcao
linhas, palavrasid = buscaMaisPalavras('Programação python')

# Definindo o Metodo de busca de uma palavra
def buscaUmaPalavra(palavra):
    idpalavra = getIdPalavra(palavra)
    conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)
    cursor = conexao.cursor()
    cursor.execute('select urls.url from palavra_localizacao plc inner join urls on plc.idurl = urls.idurl where plc.idpalavra = %s', idpalavra)
    paginas = set()
    for url in cursor:
        #print(url[0])
        paginas.add(url[0])
    print('Paginas encontradas : '+ str(len(paginas)))
    for url in paginas:
        print(url)
    cursor.close()
    conexao.close()

# Teste da funcao    
# buscaUmaPalavra('Programação')

# Transformando o id da URL em link
def getUrl(idurl):
    retorno = ''
    conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)
    cursor = conexao.cursor()
    cursor.execute('select url from urls where idurl = %s', idurl)
    if cursor.rowcount > 0:
        retorno = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return retorno

# Teste da funcao
# getUrl(1)

# Verificando a frequencia das palavras no documento
def frequenciaScore(linhas):
    contagem = dict([linha[0], 0] for linha in linhas)    
    for linha in linhas:
        #print(linha)
        contagem[linha[0]] += 1
    return contagem

# Teste da funcao
# frequenciaScore(linhas)   

# Calculo da distancia entre palavras buscadas
def distanciaScore(linhas):
    if len(linhas[0]) <= 2:
        return dict([(linha[0], 1.0) for linha in linhas])
    distancias = dict([(linha[0], 1000000) for linha in linhas])
    for linha in linhas:
        dist = sum([abs(linha[i] - linha[i - 1]) for i in range(2, len(linha))])
        if dist < distancias[linha[0]]:
            distancias[linha[0]] = dist
    return distancias

# Teste da funcao
distanciaScore(linhas)        
    
# Listagem com scores
def pesquisa(consulta):
    linhas, palavrasid = buscaMaisPalavras(consulta)
    # Abaixo diversas maneiras de filtrar a pesquisa 
    #scores = dict([linha[0], 0] for linha in linhas)
    #scores = frequenciaScore(linhas)
    #scores = localizacaoScore(linhas)
    scores = distanciaScore(linhas)
    #for url, score in scores.items():
        #print(str(url) + ' - ' + str(score))
    scores_ordenado = sorted([(score, url) for url, score in scores.items()], reverse = 0)
    for (score, idurl) in scores_ordenado[0: 10]:
        print('%f\t%s'%(score, getUrl(idurl)))

# Teste da funcao
pesquisa('Programação python')

# Posicao das palavras no documento
def localizacaoScore(linhas):
    localizacoes = dict([linha[0], 1000000] for linha in linhas)
    for linha in linhas:
        soma = sum(linha[1:])
        if soma < localizacoes[linha[0]]:
            localizacoes[linha[0]] = soma
    return localizacoes

localizacaoScore(linhas)
 
        
