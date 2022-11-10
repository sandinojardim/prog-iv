from ensurepip import bootstrap
from wsgiref.validate import validator
from flask import Flask, render_template, redirect, url_for, session
from livereload import Server
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'chave secreta'
bootstrap = Bootstrap5(app)

class NameForm(FlaskForm):
	name = StringField("Nome: ",validators=[DataRequired()])
	gender = RadioField('Sexo: ',choices=[('M','Masculino'),('F','Feminino')])
	submit = SubmitField('Enviar')

@app.route('/',methods=['GET','POST'])
def index_db():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data#name = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html',form=form, name=session.get('name'))




server = Server(app.wsgi_app)
server.watch('templates/')
server.serve()