from flask import Flask
from datetime import datetime
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'mysecret key'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <body>
    <h1>Hello heroku</h1>
    <p>This is the latest change</p>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    </body>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)