from flask import Flask

aula2 = Flask(__name__)

@aula2.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Currículo</h1>

        <h2>Informações Pessoais</h2>
        <ul>
            <li><strong>NOME:</strong> Luanny Sandrin</li>
            <li><strong>IDADE:</strong> 18</li>
            <li><strong>E-MAIL:</strong> luannysandrin@gmail.com</li>
            <li><strong>TELEFONE:</strong> (31) 99428-3138</li>
        </ul>

        <h2>Formação Acadêmica</h2>
        <ul>
            <li>Colégio COTEMIG</li>
            <li>Técnica em Informática</li>
            <li><strong>CURSANDO - Conclusão</strong> Dezembro de 2026</li>
        </ul>

        <h2>Sobre Mim</h2>
        <p>
            Olá, meu nome é Luanny Alves Ishida Sandrin, tenho 18 anos.
            <br>Atualmente estou cursando o ensino médio Técnico na escola COTEMIG e a conclusão do curso será em 2026.
            <br>Pretendo trabalhar na área de TI como Dev, minha paixão está em desenvolver sites com interfaces modernas e de alta qualidade.
            <br>Meu objetivo é evoluir constantemente como profissional de TI e contribuir em projetos que gerem impacto real para pessoas e empresas.
        </p>

        <h2>Skills</h2>
        <h4>Soft</h4>
        <ul>
            <li>Criatividade</li>
            <li>Proatividade</li>
            <li>Pensamento Crítico</li>
            <li>Trabalho em Equipe</li>
            <li>Empatia</li>
            <li>Adaptabilidade</li>
            <li>Organização</li>
            <li>Flexibilidade</li>
        </ul>
        <h4>Hard</h4>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
            <li>MySQL</li>
            <li>C#</li>
            <li>Redes e Arquitetura de Computadores</li>
            <li>Robótica</li>
        </ul>
    </body>
    </html>
    '''

if __name__ == '__main__':
    aula2.run(debug=True)