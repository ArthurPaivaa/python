from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Acesse <a href="/decorator">/decorator</a> para ver a explicação.'

@app.route('/decorator')
def explicar_decorator():
    return """
    <h1>Conceito de Decorator em Python</h1>
    
    <h3>1. O que é?</h3>
    <p>Um <b>decorator</b> é uma função que recebe outra função como argumento, estende o seu comportamento sem modificá-la explicitamente e retorna uma nova função.</p>
    
    <h3>2. Para que serve?</h3>
    <p>Serve para separar preocupações e evitar repetição de código (DRY - Don't Repeat Yourself). É ideal para tarefas como:</p>
    <ul>
        <li>Logs e monitoramento;</li>
        <li>Controle de autenticação/permissões;</li>
        <li>Cache de dados;</li>
        <li>Validação de entradas.</li>
    </ul>

    <h3>3. Uso no Flask (@app.route)</h3>
    <p>No Flask, o decorator <code>@app.route('/')</code> é usado para "embrulhar" uma função Python comum e registrá-la como uma <b>rota</b> no servidor web. 
    Internamente, o Flask usa esse decorator para associar uma URL específica à lógica que deve ser executada quando alguém a acessa.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

