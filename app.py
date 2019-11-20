from datetime import datetime
from logging.config import fileConfig

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
CORS(app)

### Logging config
fileConfig("config/logging.cfg")

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config["SECRET_KEY"] = "mysecret key"

toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    app.logger.info("Logging some stuff")

    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <body>
    <h1>Hello heroku</h1>
    <p>This is the latest change</p>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    </body>
    """.format(
        time=the_time
    )


@app.route("/somedata")
@cross_origin()
def send_simple_data():
    app.logger.info("Getting some data")
    text_response = "Hello from Flask"
    return jsonify(text_response)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
