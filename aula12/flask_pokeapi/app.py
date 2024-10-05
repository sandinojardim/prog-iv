from flask import Flask
from config import Config
from database import db
from blueprints.pokemon import pokemon as pokemon_bp
from blueprints.main import main as main_bp 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados

    app.register_blueprint(pokemon_bp, url_prefix='/api')  # Prefixo para as rotas da API
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
