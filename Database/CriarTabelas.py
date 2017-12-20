import mysql.connector

config = {
      'user': 'root',
      'password': 'ifpbinfo',
      'host': '127.0.0.1',
      'database': 'TrabExtra',
      'raise_on_warnings': True
}

def criarTabelas():
    conn = mysql.connector.connect(**config )
    cursor=conn.cursor()
    cursor.execute(""" CREATE TABLE tb_usuario(
        id_usuario integer PRIMAARY KEY,
        nome VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        senha VARCHAR(50) NOT NULL,
        dataNasc VARCHAR(50) NOT NULL,
        profissao VARCHAR(50) NOT NULL,
        genero VARCHAR(50) NOT NULL,
        cidade VARCHAR(50) NOT NULL,
        estado VARCHAR(50) NOT NULL,
        pais VARCHAR(50) NOT NULL""")

    cursor.execute("""CREATE TABLE tb_mensagem(
    id_mensagem INTEGER PRIMARY KEY AUTOINCREMENT,
    id_remetente VARCHAR (50) not NULL),
    data_hora DATETIME,
    texto VARCHAR (256)""")

    conn.close()
