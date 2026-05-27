from flask import Flask, request, render_template

app = Flask(__name__)

meu_usuario = "luanny"  
minha_senha = "1234"  

@app.route('/')
def atividade_jinja():
    dados_usuario = {"nome": "Luanny", "email": "luanny@gmail.com"}
    lista_textos_alunos = ["Luanny", "Clarice", "Davi", "Janaina"]
    nota_exemplo = 8.5 

    return render_template(
        'jinja.html', 
        nome_simples="Luanny", 
        idade_simples=18, 
        usuario=dados_usuario, 
        alunos=lista_textos_alunos, 
        nota=nota_exemplo
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario == meu_usuario and senha == minha_senha:
            return f"<h1>Acesso Permitido! Bem-vindo, {usuario}!</h1>"
        else:
            return render_template('login.html', erro="Login inválido. Usuário ou senha incorretos.")
    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)