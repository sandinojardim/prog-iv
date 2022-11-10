import os
from flask import Flask, render_template, redirect, url_for, session
from livereload import Server
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave ultra secreta'
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)


class NameForm(FlaskForm):
    name = StringField("Nome: ",validators=[DataRequired()])
    #mail = EmailField("E-mail: ",validators=[DataRequired()])
	#gender = RadioField('Sexo: ',choices=[('M','Masculino'),('F','Feminino')])
    submit = SubmitField('Enviar')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #email = db.Column(db.String(64),index=True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.route('/',methods=['GET','POST'])
def index():
    db.create_all()
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data,role_id=0)#user = User(username=form.name.data,role_id=0,email=form.mail.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            session['name'] = form.name.data
            #session['mail'] = form.mail.data
        else:
            session['known'] = True
            session['name'] = form.name.data
            session['mail'] = form.mail.data
            form.name.data = ''
            return redirect(url_for('index'))
    return render_template('index_db.html',form=form, name=session.get('name'),known=session.get('known',False))
    #return render_template('index_db.html',form=form, name=session.get('name'),email=session.get('mail'),known=session.get('known',False))


migrate = Migrate(app,db)

# server = Server(app.wsgi_app)
# server.watch('templates/')
# server.serve()