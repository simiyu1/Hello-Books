from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mgeni'}
    books = [
        {
            'author': {'username': 'Mc Maher'},
            'title': 'Once Upon a Friday.',
            'Publisher': 'MacMillan'
        },
        {
            'author': {'username': 'Phil Koel'},
            'title': 'Know it all.',
            'Publisher': 'MacMillan'
        },
        {
            'author': {'username': 'Maria Stella'},
            'title': 'Bitter Pills, sweetened drinks',
            'Publisher': 'MacMillan'
        },
        {
            'author': {'username': 'Camella Poe'},
            'title': 'The Weekender.',
            'Publisher': 'MacMillan'
        }
    ]
    return render_template('/UI/index.html', title='Home', user=user, books=books)

@app.route('/login')
def login():
    return render_template('UI/login.html')
