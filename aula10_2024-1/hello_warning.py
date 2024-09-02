from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap5
from livereload import Server




app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'chave secreta'
bootstrap = Bootstrap5(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        flash('Nome registrado com sucesso.', 'success')
        return redirect(url_for('index'))
    elif len(session['name']) < 8:
        flash('O nome deve ter pelo menos 8 caracteres.', 'warning')
    return render_template('index_warning.html', form=form, name=session.get('name'))

server = Server(app.wsgi_app)
server.watch('templates/')
server.serve()