from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from time import sleep
from flask_caching import Cache
import hashlib
from time import strftime

app = Flask(__name__)
CORS = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)


@app.route('/api/greeting', methods=['POST'])
def greeting():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify(greeting=f'Hello, {name}!')

def get_time():
    data = strftime("%Y-%m-%dT-%h-%m-%s")
    return data

@app.route('/api/time')
@app.cache.cached(timeout=10)
def index():
    return get_time()

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response


users = {
    "user1": "password1",
    "user2":"password2"
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    one_time_key = data.get('oneTimeKey')

    # Sprawdzamy, czy użytkownik istnieje
    if username in users:
        # Sprawdzamy, czy hasło jest poprawne
        expected_password = hashlib.sha256((users[username] + one_time_key).encode()).hexdigest()
        print(expected_password)
        if password == expected_password:
            return {"success": True}, 200
        else:
            return {"success": False, "message": "Nieprawidłowe hasło"}, 401
    else:
        return {"success": False, "message": "Nieznany użytkownik"}, 404


if __name__ == '__main__':
    app.run(debug=True)