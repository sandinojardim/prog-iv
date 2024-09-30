from flask import render_template
from . import main
from flask_login import login_required

#nesta estrutura, rotas são definidas em arquivo views.py

@main.route('/', methods=['GET', 'POST']) #main.route ao invés de app.route, pois é definida a partir do Blueprint 'main'
def index():
    #return redirect(url_for(main.index)) ## necessita informar o 'namespace' das rotas
    return render_template('index.html')

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'