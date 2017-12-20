import mysql.connector

    config = {
      'user': 'root',
      'password': 'ifpbinfo',
      'host': '127.0.0.1',
      'database': 'geekway',
      'raise_on_warnings': True
    }

class UsuarioDAO():

       def __init__(self):
       pass

    def insert(self, usuario):
      cursor=conn.cursor
        cursor.execute = ("""INSERT INTO tb_usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""),(usuario.nome,usuario.email,usuario.senha,usuario.dataNasc,usuario.profissao,usuario.genero,usuario.cidade,usuario.estado,usuario.pais)
    conn.close

    def delete(self, idDelete):
      cursor=conn.cursor
        cursor.execute = ("""DELETE FROM tb_usuario WHERE id_usuario=?""",(idDelete)
        conn.close

        def insert(self, usuario):
      cursor=conn.cursor
        cursor.execute = ("""UPDATTE tb_usuario SET(%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id_usuario=""",
        (usuario.nome,usuario.email,usuario.senha,usuario.dataNasc,usuario.profissao,usuario.genero,usuario.cidade,usuario.estado,usuario.pais)
    conn.close