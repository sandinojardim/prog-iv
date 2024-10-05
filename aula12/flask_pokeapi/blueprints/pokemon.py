from flask import Blueprint, jsonify
from models import Pokemon

pokemon = Blueprint('pokemon', __name__)

@pokemon.route('/pokemon', methods=['GET'])
def get_all_pokemons():
    pokemons = Pokemon.query.all()
    return jsonify([{
        'id': pokemon.id,
        'name': pokemon.name,
        'number': pokemon.number,
        'types': pokemon.types.split(','),
        'image_url': pokemon.image_url
    } for pokemon in pokemons])

@pokemon.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    pokemon = Pokemon.query.get_or_404(pokemon_id)
    return jsonify({
        'id': pokemon.id,
        'name': pokemon.name,
        'number': pokemon.number,
        'types': pokemon.types.split(','),
        'image_url': pokemon.image_url
    })

@pokemon.route('/pokemon/name/<string:pokemon_name>', methods=['GET'])
def get_pokemon_by_name(pokemon_name):
    pokemon = Pokemon.query.filter(Pokemon.name == pokemon_name).first()
    if pokemon:
        return jsonify({
            'id': pokemon.id,
            'name': pokemon.name,
            'number': pokemon.number,
            'types': pokemon.types.split(','),
            'image_url': pokemon.image_url
        })
    else:
        return jsonify({"error": "Pokémon não encontrado."}), 404
