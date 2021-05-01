import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_character():
    r = requests.get('https://www.breakingbadapi.com/api/character/random')
    characterjson = r.json()
    character = {
        'image': characterjson[0]['img'],
        'name': characterjson[0]['name'],
        'occupation': characterjson[0]['occupation'],
        'status': characterjson[0]['status'],
        'nickname': characterjson[0]['nickname']
    }

    # Display Character
    return(render_template('index.html', character=character))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)  # specify port=80
