from database import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    types = db.Column(db.String(100), nullable=True)  
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Pokemon {self.name}>'
