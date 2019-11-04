"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    user = {'nickname':'Chen'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Mary'},
            'body':'Avengers Assemble!'
        }
    ]
    """Renders a sample page."""
    return render_template('index.html',title='Home',user=user,posts=posts)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=True)
