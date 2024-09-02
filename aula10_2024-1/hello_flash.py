from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from livereload import Server




app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'chave secreta'
bootstrap = Bootstrap5(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Parece que você mudou o nome!")
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index_flash.html', form=form, name=session.get('name'))

server = Server(app.wsgi_app)
server.watch('templates/')
server.serve()