from model.Usuario import Usuario
from model.Comentario import Comentario
from Database.UsuarioDAO import UsioarioDAO
from Database.ComentarioDAO import ComentarioDAO
from Database.CriarTabelas import criarTabelas
import datetime

userfeed=Usuario()

def signUp():
    print('========================================================================================================================')
        NovoUsuario = Usuario()
        NovoUsuario.nome = input('Digite o nome de usuário')
        NovoUsuario.email = input('Digie seu E-mail')
        NovoUsuario.senha = input('Qual será sua senha? Remonmendamos uma senha com mais de 8 dígitos numeros ')
        NovoUsuario.dataNasc = input('Digite sua data de nascimento')
        NovoUsuario.profissao = input('Digite sua profissão')
        NovoUsuario.genero=input("digite seu genero")
        NovoUsuario.cidade=input("digite sua cidade")
        NovoUsuario.estado=input("digite seu estado")
        NovoUsuario.pais=input("digite seu pais")
        UsuarioDAO.inserir(NovoUsuario)

def logIn():
    print('========================================================================================================================')
    cursor = conn.cursor()

    email = input("Digite seu email:\n ")
    senha = input("Digite sua senha:\n ")

    cursor.execute("""
        Select * From tb_Usuario where email = ? and senha = ?;
    """, (email, senha))
    usuario = cursor.fetchone()

    if (usuario == None):
        return (False, "NADA")
    else:
        userfeed=usuario
        return (True, usuario)

def Comentar():
    print('========================================================================================================================')
        Novocomentario = comentario()
        Novocomentario.mensagem = input('Digite sua mensagem')
        Novocomentario.Remetente = userfeed.nome
        Novocomentario.dataHora = datetime.datetime().now()
        ComentarioDAO.inserir(Novocomentario)

while True
    menu=input("o que deseja fazer agora?\n0-sair\n1-criar o banco de dados\n2-cadastrar um usuário\n3-realizar LogIn")
    criarTabelas()

    if menu==0:
        break
    elif menu==1:
        criatTabelas()
    elif menu==2:
        signUp
    elif menu==3:
        logIn()

