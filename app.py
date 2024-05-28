from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Usuário admin hardcoded
admin_username = "paciente"
admin_password = "p01223"

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para lidar com o login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verificar se as credenciais correspondem ao usuário admin
    if username == admin_username and password == admin_password:
        # Redirecionar para a página de boas-vindas
        return redirect(url_for('dados'))
    else:
        return "Invalid username or password"

# Página de boas-vindas após o login bem-sucedido
@app.route('/dados')
def welcome():
    return render_template('dados.html')

if __name__ == '__main__':
    app.run(debug=True)
