from flask import Flask

aula1 = Flask(__name__)

@aula1.route('/')
def home():
    return 'Acesse a rota <a href="/decorator">/decorator</a> para ver a explicação.'

@aula1.route('/decorator')
def explicar_decorator():
    return '''
    <h1>Entendendo Decorators em Python</h1>
    
    <h3>1. O que é um Decorator?</h3>
    <p>Um <b>decorator</b> (decorador) é uma função que recebe outra função como argumento, 
    estende o seu comportamento sem modificá-la explicitamente e retorna uma nova função. 
    Em Python, eles são identificados pelo símbolo <code>@</code> acima da definição de uma função.</p>

    <h3>2. Para que serve?</h3>
    <ul>
        <li><b>Reutilização de código:</b> Evita repetição (DRY - Don't Repeat Yourself).</li>
        <li><b>Separação de preocupações:</b> Permite adicionar lógica extra (como logs, controle de acesso ou cache) 
        sem "sujar" o código principal da função.</li>
        <li><b>Modificação dinâmica:</b> Altera como uma função se comporta em tempo de execução.</li>
    </ul>

    <h3>3. Como é utilizado no Flask?</h3>
    <p>O uso mais comum no Flask é o <code>@aula2.route('/')</code>. Aqui está o que acontece:</p>
    <ul>
        <li>O decorator <b>registra</b> a função que vem logo abaixo dele no sistema de roteamento do Flask.</li>
        <li>Ele associa um endereço URL (ex: /decorator) a uma função específica do Python.</li>
        <li>Quando o servidor recebe uma requisição para aquele caminho, o Flask sabe exatamente qual função deve "chamar" 
        graças ao registro feito pelo decorator no momento em que a aplicação foi iniciada.</li>
    </ul>
    
    <hr>
    <p><i>Exemplo técnico: @aula2.route('/caminho') "embrulha" sua função para que ela se torne uma resposta web.</i></p>
    '''

if __name__ == '__main__':
    aula1.run(debug=True)