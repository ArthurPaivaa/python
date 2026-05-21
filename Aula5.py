from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dicionário de usuários: { 'usuario': 'senha' }
usuarios = {
    'arthur':  '22401644',
    'dolga':   'cotemig2026',
    'janaina': 'cotemig2026',
    'antonio': 'cotemig2026',
}

def show_the_login_form(erro=None):
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Login</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #1a1a2e;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .card {
                background: #16213e;
                border: 1px solid #0f3460;
                border-radius: 12px;
                padding: 40px 36px;
                width: 340px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            }
            h2 {
                color: #e94560;
                margin-bottom: 24px;
                font-size: 1.6rem;
                text-align: center;
                letter-spacing: 2px;
                text-transform: uppercase;
            }
            label {
                color: #a8b2c1;
                font-size: 0.8rem;
                letter-spacing: 1px;
                text-transform: uppercase;
                display: block;
                margin-bottom: 6px;
            }
            input {
                width: 100%;
                padding: 10px 14px;
                border: 1px solid #0f3460;
                border-radius: 6px;
                background: #0f3460;
                color: #fff;
                font-size: 0.95rem;
                margin-bottom: 18px;
                outline: none;
                transition: border .2s;
            }
            input:focus { border-color: #e94560; }
            button {
                width: 100%;
                padding: 12px;
                background: #e94560;
                color: #fff;
                border: none;
                border-radius: 6px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                letter-spacing: 1px;
                transition: background .2s;
            }
            button:hover { background: #c73652; }
            .erro {
                color: #e94560;
                font-size: 0.85rem;
                text-align: center;
                margin-bottom: 14px;
                background: rgba(233,69,96,.1);
                border-radius: 6px;
                padding: 8px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Login</h2>
            {% if erro %}
            <div class="erro">{{ erro }}</div>
            {% endif %}
            <form method="POST">
                <label>Usuário</label>
                <input type="text" name="usuario" placeholder="seu usuário" autofocus>
                <label>Senha</label>
                <input type="password" name="senha" placeholder="sua senha">
                <button type="submit">Entrar</button>
            </form>
        </div>
    </body>
    </html>
    """, erro=erro)


def do_the_login():
    usuario = request.form.get('usuario', '').strip().lower()
    senha   = request.form.get('senha', '').strip()

    # Percorre o dicionário para verificar as credenciais
    for user, pwd in usuarios.items():
        if usuario == user and senha == pwd:
            return render_template_string("""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <title>Bem-vindo</title>
                <style>
                    body {
                        font-family: 'Segoe UI', sans-serif;
                        background: #1a1a2e;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }
                    .card {
                        background: #16213e;
                        border: 1px solid #0f3460;
                        border-radius: 12px;
                        padding: 40px 36px;
                        text-align: center;
                        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
                    }
                    h1 { color: #4ecca3; font-size: 1.8rem; }
                    p  { color: #a8b2c1; margin-top: 10px; }
                    a  { color: #e94560; text-decoration: none; display: inline-block; margin-top: 20px; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>Bem-vindo, {{ nome }}! 🎉</h1>
                    <p>Login realizado com sucesso.</p>
                    <a href="/">← Voltar</a>
                </div>
            </body>
            </html>
            """, nome=user.capitalize())

    # Nenhum usuário bateu — login inválido
    return show_the_login_form(erro="Usuário ou senha inválidos.")


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping
