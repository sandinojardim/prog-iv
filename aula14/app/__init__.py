from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from config import config

csp = {
    'default-src': ['\'self\'', 'https://stackpath.bootstrapcdn.com', 'https://cdnjs.cloudflare.com', 'https://cdn.jsdelivr.net'],
    'style-src': ['\'self\'', 'https://stackpath.bootstrapcdn.com', 'https://cdn.jsdelivr.net'],
    'script-src': ['\'self\'', 'https://code.jquery.com', 'https://cdn.jsdelivr.net', 'https://cdnjs.cloudflare.com', '\'unsafe-inline\''],
    'img-src': ['\'self\'', 'https://secure.gravatar.com']  # Permite imagens do Gravatar
}

bootstrap = Bootstrap5()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)
#talisman = Talisman(content_security_policy=csp)


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    limiter.init_app(app)

    #talisman.init_app(app)  # Força HTTPS em todas as rotas



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) #permite instanciação de aplicações em tempo de execução

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')



    return app