import flask
from flask import Flask
from apiengine import ApiEngine

app = Flask(__name__)

@app.route('/home/news')
def api():
    apiengine = ApiEngine()
    data = apiengine.start('engadget')
    return flask.jsonify(data[0])
    
if __name__ == "__main__":
    app.run(debug=True)