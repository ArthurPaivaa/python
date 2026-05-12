from flask import Flask, render_template_string

app = Flask(__name__)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo Online</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; display: flex; justify-content: center; padding: 20px; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 500px; width: 100%; }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        h2 { font-size: 1.2em; color: #3498db; margin-top: 20px; }
        ul { padding-left: 20px; }
        li { margin-bottom: 8px; }
        .tag { background: #3498db; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.9em; display: inline-block; margin: 2px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>{{ nome }}</h1>
        <p><strong>Cargo:</strong> {{ cargo }}</p>
        
        <h2>Experiência Profissional</h2>
        <ul>
            {% for exp in experiencias %}
                <li>{{ exp }}</li>
            {% endfor %}
        </ul>

        <h2>Habilidades</h2>
        <div>
            {% for habilidade in habilidades %}
                <span class="tag">{{ habilidade }}</span>
            {% endfor %}
        </div>

        <p style="margin-top: 30px; font-size: 0.8em; color: #888;">Gerado dinamicamente via Flask</p>
    </div>
</body>
</html>
"""

@app.route('/curriculo')
def exibir_curriculo():
    # os dados que serão injetados no html
    dados = {
        "nome": "Seu Nome Aqui",
        "cargo": "Desenvolvedor Python Júnior",
        "experiencias": [
            "Desenvolvimento de APIs com Flask",
            "Automação de processos com Python",
            "Criação de Dashboards de dados"
        ],
        "habilidades": ["Python", "Flask", "SQL", "Git", "Docker"]
    }
    # vai renderizar a string html passando os dados como argumentos
    return render_template_string(HTML_TEMPLATE, **dados)

if __name__ == '__main__':
    app.run(debug=True)
