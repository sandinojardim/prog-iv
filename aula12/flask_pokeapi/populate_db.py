import requests
from database import db
from models import Pokemon
from app import create_app

app = create_app()

def populate_db():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Primeiros 151 Pokémon
    response = requests.get(url)
    data = response.json()

    with app.app_context():
        for item in data['results']:
            pokemon_response = requests.get(item['url']).json()
            pokemon = Pokemon(
                name=pokemon_response['name'],
                number=pokemon_response['id'],
                types=','.join([type_info['type']['name'] for type_info in pokemon_response['types']]),
                image_url=pokemon_response['sprites']['front_default']
            )
            db.session.add(pokemon)
        db.session.commit()
        print("Banco de dados preenchido com sucesso!")

if __name__ == '__main__':
    populate_db()
