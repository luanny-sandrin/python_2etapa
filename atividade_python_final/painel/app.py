import requests
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import conectar
from flask import jsonify


app = Flask(__name__)
app.secret_key = "123456"

def buscar_frase():

    try:

        resposta = requests.get(
            "https://api.quotable.io/random",
            timeout=5
        )

        dados = resposta.json()

        return dados["content"]

    except:

        return "Cada amanhecer é um convite a ser melhor, uma nova chance para recomeçar e uma tela em branco para criar o seu melhor dia."


@app.route("/")
def inicio():

    if "usuario" not in session:
        return redirect("/login")

    status = request.args.get("status")

    conexao = conectar()
    cursor = conexao.cursor()

    if status:

        cursor.execute("""
            SELECT *
            FROM tarefas
            WHERE usuario_id = ?
            AND status = ?
        """, (session["usuario"], status))

    else:

        cursor.execute("""
            SELECT *
            FROM tarefas
            WHERE usuario_id = ?
        """, (session["usuario"],))

    tarefas = cursor.fetchall()

    conexao.close()

    frase = buscar_frase()

    return render_template(
        "dashboard.html",
        tarefas=tarefas,
        frase=frase
    )



@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = generate_password_hash(request.form["senha"])

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO usuarios(nome,email,senha)
            VALUES(?,?,?)
        """,(nome,email,senha))

        conexao.commit()
        conexao.close()

        return redirect(url_for("login"))

    return render_template("registro.html")



@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM usuarios
            WHERE email=?
        """,(email,))

        usuario = cursor.fetchone()

        conexao.close()

        if usuario:

            if check_password_hash(usuario["senha"], senha):

                session["usuario"] = usuario["id"]

                return redirect("/")

    return render_template("login.html")



@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")



@app.route("/nova_tarefa", methods=["GET", "POST"])
def nova_tarefa():

    if "usuario" not in session:
        return redirect("/login")

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO tarefas
            (titulo, descricao, status, usuario_id)
            VALUES (?, ?, ?, ?)
        """, (
            titulo,
            descricao,
            status,
            session["usuario"]
        ))

        conexao.commit()
        conexao.close()

        return redirect("/")

    return render_template("nova_tarefa.html")



@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    if "usuario" not in session:
        return redirect("/login")

    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]

        cursor.execute("""
            UPDATE tarefas
            SET titulo = ?,
                descricao = ?,
                status = ?
            WHERE id = ? AND usuario_id = ?
        """, (
            titulo,
            descricao,
            status,
            id,
            session["usuario"]
        ))

        conexao.commit()
        conexao.close()

        return redirect("/")

    cursor.execute("""
        SELECT * FROM tarefas
        WHERE id = ? AND usuario_id = ?
    """, (id, session["usuario"]))

    tarefa = cursor.fetchone()

    conexao.close()

    return render_template(
        "editar.html",
        tarefa=tarefa
    )



@app.route("/excluir/<int:id>")
def excluir(id):

    if "usuario" not in session:
        return redirect("/login")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ? AND usuario_id = ?
    """, (id, session["usuario"]))

    conexao.commit()
    conexao.close()

    return redirect("/")

@app.route("/api/tarefas")
def api_tarefas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM tarefas
    """)

    tarefas = cursor.fetchall()

    conexao.close()

    lista = []

    for tarefa in tarefas:

        lista.append({

            "id": tarefa["id"],

            "titulo": tarefa["titulo"],

            "descricao": tarefa["descricao"],

            "status": tarefa["status"]

        })

    return jsonify(lista)

if __name__ == '__main__':
    app.run(debug=True) 