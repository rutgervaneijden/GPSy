import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def index():
    location = dict()
    location['latitude'] = flask.request.args.get('latitude')
    location['longitude'] = flask.request.args.get('longitude')
    location['timestamp'] = flask.request.args.get('timestamp')
    try:
        with open('locations.json', 'r') as file:
            locations = json.load(file)
    except FileNotFoundError:
        locations = list()
    finally:
        locations.append(location)
        with open('locations.json', 'w') as file:
            json.dump(locations, file)
    return flask.render_template('index.html', data=locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
