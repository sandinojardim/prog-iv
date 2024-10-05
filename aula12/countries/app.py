from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para buscar informações do país
@app.route('/country', methods=['POST'])
def get_country_info():
    country_name = request.form.get('country')
    if not country_name:
        return jsonify({'error': 'País não informado.'}), 400
    
    api_url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    response = requests.get(api_url)
    
    if response.status_code != 200:
        return jsonify({'error': 'País não encontrado.'}), 404
    
    country_data = response.json()[0]
    
    # Extraindo informações do país
    country_info = {
        'name': country_data.get('name', {}).get('common', 'N/A'),
        'capital': country_data.get('capital', ['N/A'])[0],
        'population': country_data.get('population', 'N/A'),
        'region': country_data.get('region', 'N/A'),
        'subregion': country_data.get('subregion', 'N/A'),
        'flag': country_data.get('flags', {}).get('png', '')
    }
    
    return jsonify(country_info)

if __name__ == '__main__':
    app.run(debug=True)
