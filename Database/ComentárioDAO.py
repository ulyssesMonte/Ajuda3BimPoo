import mysql.connector

    config = {
      'user': 'root',
      'password': 'ifpbinfo',
      'host': '127.0.0.1',
      'database': 'geekway',
      'raise_on_warnings': True
    }

class ComentarioDAO():

    def __init__(self):
       pass

    def insert(self, comentario):
      cursor=conn.cursor()
        cursor.execute = ("""INSERT INTO tb_comentario(id_usuario,id_publicacao, mensagem, data_hora, curtidas)
                VALUES(%s, %s, %s, %s, %s)"""),(comentario.idPublicacao, comentario.idRemetente, comentario.mensagem.id, comentario.dataHora, comentario.curtidas)
    conn.close

