#Essa etapa o programa iniciará pela função createDB(), fazendo conexão com o MySQL.
#Após terminar a primeira etapa, a segunda será ativada e fazerá login no MySQL e conectando ao banco de dados.
#Criando a primeira coluna de conta como chave primária e logo em seguida, alterando tabela para colocar colunas.

import pymysql


def createDB():
    conexao = pymysql.connect(host='localhost', user='root', password='')

    cursor = conexao.cursor()

    # Criando DATABASE:
    cursor.execute("CREATE DATABASE banco")

    createTable()

def createTable():
    conexao = pymysql.connect(host='localhost', user='root', password='', database = 'banco')

    cursor = conexao.cursor()

    # Criando Tabela clientes:
    cursor.execute("CREATE TABLE clientes(conta INT(255) AUTO_INCREMENT PRIMARY KEY)")

    alterTable()

def alterTable():
    conexao = pymysql.connect(host='localhost', user='root', password='', database='banco')

    cursor = conexao.cursor()

    # Adicionando colunas:
    cursor.execute("ALTER TABLE clientes ADD COLUMN login VARCHAR(255) UNIQUE")
    cursor.execute("ALTER TABLE clientes ADD COLUMN senha VARCHAR(255)")
    cursor.execute("ALTER TABLE clientes ADD COLUMN nome VARCHAR(255)")
    cursor.execute("ALTER TABLE clientes ADD COLUMN cpf VARCHAR(11) UNIQUE")
    cursor.execute("ALTER TABLE clientes ADD COLUMN saldo VARCHAR(255)")

createDB()