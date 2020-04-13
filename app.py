from flask import Flask, jsonify, request, redirect, g, render_template, session
from flask_cors import CORS
from spotify_requests import spotify


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'super secret key'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route("/auth")
def auth():
    if 'auth_header' in session:
        authed = True
    else:
        authed = False

    return jsonify({
        "url": spotify.AUTH_URL,
        "authed": authed
    })


@app.route("/callback/", methods=['POST'])
def callback():
    code = request.json.get('code')
    auth_token = code
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header

    return jsonify('OK')

@app.route("/albums/", methods=['GET'])
def albums():
    if 'auth_header' in session:
        albums = spotify.get_saved_albums(session['auth_header'])
        
        return jsonify(albums)
    else:
        return jsonify([])

@app.route("/top/", methods=['GET'])
def top():
    if 'auth_header' in session:
        top = spotify.get_top(session['auth_header'])
        
        return jsonify(top)
    else:
        return jsonify([])

@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

if __name__ == '__main__':
    app.run(host='192.168.1.142')