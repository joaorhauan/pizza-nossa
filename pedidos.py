from flask import Blueprint
from flask import render_template, request, redirect
from models import Pedido
from database import db
from datetime import date

bp_pedidos = Blueprint("pedidos", __name__, template_folder="templates")

@bp_pedidos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=="GET":
        return render_template('pedidos_create.html')
    
    if request.method=='POST':
        usuario_id = request.form.get('usuario.id')
        pizza_id = request.form.get('pizza_id')
        data = date.today()

        p = Pedido(usuario_id, pizza_id, data)
        db.session.add(p)
        db.session.commit()
        return 'Dados cadastrados com sucesso'
    
@bp_pedidos.route('/recovery')
def recovery():
    pedidos = Pedido.query.all()
    return render_template('pedidos_recovery.html', pedidos=pedidos)