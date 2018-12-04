from flask import Flask, render_template

import requests as r

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<query>', methods=['GET'])
def pokemon_response(query=None):
    request = r.get('http://pokeapi.co/api/v2/pokemon/' + query)
    if request.status_code != 200:
        return render_template('index.html')

    if query.isdigit():
        pokemon_name = request.json()['name']
        return render_template('pokemon_id.html', pokemon_name=pokemon_name, pokemon_id=query)
    else:
        pokemon_id = request.json()['id']
        return render_template('pokemon_name.html', pokemon_name=query, pokemon_id=pokemon_id)


if __name__ == '__main__':
    app.run()
