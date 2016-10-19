from flask import Flask
from flask import redirect
import os


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_route(path):
    if 'REDIRECT_URL' in os.environ:
        return redirect(os.environ['REDIRECT_URL'], code=302)

    return 'Redirect not set!'
