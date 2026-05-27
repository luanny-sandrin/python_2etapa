from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resultado, etapas = calcular()
        return render_template('calculadora.html', etapas=etapas, resultados=resultado)
    else:
        return render_template('calculadora.html', etapas="", resultados="")

if __name__ == '__main__':
    app.run(debug=True)