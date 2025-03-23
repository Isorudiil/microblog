from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Elijah'}
    posts = [
        {
            'author': {'username': 'Katie'},
            'body': 'So good to see you hubby'
         },
         {
             'author': {'username': 'Katie Joanna'},
             'body': "Don't you love Gilmore Girls?"
         }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)