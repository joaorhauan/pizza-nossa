from flask import Flask, render_template, flash, redirect, request
from database import db
from flask_migrate import Migrate
from models import Usuario
from pedidos import bp_pedidos

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'

conexao = "sqlite:///mydb"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_pedidos, url_prefix='/pedidos')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    user = request.form.get("user")
    password = request.form.get('password')
    if user != 'admin' or password != 'senha123':

        if (user == 'admin'):
            flash('O login está correto.', "warning")
        else:
            flash("O login está incorreto", "danger")
        
        if (password == 'senha123'):
            flash("A senha está correta", "warning")
        else:
            flash("A senha está incorreta.", "danger")

        return redirect('/login')
    else:
        return "Os dados recebidos foram: usuario = {} e senha {}".format(user,password)


if __name__ == '__main__':
    app.run(debug=True)