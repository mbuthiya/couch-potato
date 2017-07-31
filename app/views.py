from  flask import render_template
from app import app
# Index route
@app.route('/')
@app.route('/index')
def index():
    '''
    Index view function that handles request to the index route

    Returns:
        Returns the index html page
    '''
    return render_template('index.html')


# users route
@app.route('/users/@<name>')
def users(name):
    '''
    Users view function that handles request to the index route

    Args:
        name: This is a users name.
    Returns:
        Returns the users html page and passes in the dynamic name to it.
    '''
    return render_template('users.html', name = name)
