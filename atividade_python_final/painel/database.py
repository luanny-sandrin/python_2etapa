import sqlite3

def conectar():
    conexao = sqlite3.connect('tarefas.db')
    conexao.row_factory = sqlite3.Row
    return conexao


def buscar_usuario_por_email(email):
    conexao = conectar()

    usuario = conexao.execute(
        'SELECT * FROM usuarios WHERE email = ?',
        (email,)
    ).fetchone()

    conexao.close()

    return usuario


def inserir_usuario(nome, email, senha):
    conexao = conectar()

    conexao.execute(
        'INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
        (nome, email, senha)
    )

    conexao.commit()

    conexao.close()