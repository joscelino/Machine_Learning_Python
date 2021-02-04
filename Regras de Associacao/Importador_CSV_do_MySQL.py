# -*- coding: utf-8 -*-
"""
Regras de Associacao mercado com integracao ao MySql
"""
# Importacao das bibliotecas
import pymysql

# Parametros de conexao no MySql
host = 'localhost'
id_user = 'root'
password = 'JC137829'
data_base = 'mercado'

# Criando variavel para receber importacao
base = ' '

# Criando variavel de conexao
conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)

# Criando cursores
cursor = conexao.cursor()
cursorVendas = conexao.cursor()
cursorVendasProdutos = conexao.cursor()

# Efetuando comandos no MySql
cursorVendas.execute('select * from vendas')
for vendas in cursorVendas:
    print(vendas)
    quantidade = cursorVendasProdutos.execute('select prd.nome from venda_produtos vpr inner join produtos prd on vpr.idproduto = prd.idproduto where vpr.idvenda = ' + str(vendas[0]))
    i = 1
    for produtos in cursorVendasProdutos:
        print(produtos)
        
        if (i == quantidade):
            base = base + produtos[0]
        else:
            # Inserindo virgula entre os itens
            base = base + produtos[0] + ','
        i += 1
    base = base + '\n'

# Importando arquivo CSV do MySQL
arquivo = open("base_importada.csv", "w")
arquivo.write(base)
arquivo.close()

# Encerrando conexao
cursor.close()
cursorVendas.close()
cursorVendasProdutos.close()
conexao.close()
