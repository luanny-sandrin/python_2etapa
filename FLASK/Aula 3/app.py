from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre/<nome>')
def sobre(nome):
    return f"Bem-vindo {nome} ao meu primeiro FLASK!"

if __name__ == '__main__':
    app.run(debug=True)