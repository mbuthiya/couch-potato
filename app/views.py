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
    title = "The couch potato - Home"
    return render_template('index.html', title= title)


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
    title = f" The couch potato - profile {name}"
    return render_template('users.html', name = name,title=title)

# Movies routes
@app.route('/movies')
def movies():
    '''
    Movies Route function to render movies.
    Returns:
        Returns the movies html page and passes in the dynamic name to it.
    '''
    title = "The couch potato - Movies"
    return render_template('movies.html',title = title)


# Tv Shows
@app.route('/shows')
def shows():
    '''
    Shows view  function  to display tv shows
    Returns:
        Returns the Tv shows html page.
    '''
    title = "The couch potato - Tv-Shows"
    return render_template('shows.html',title = title)


# Discover
@app.route('/discover')
def discover():
    '''
    Discover view  function  to display Random tv shows

    '''
    title = "The couch potato - Discover"
    return render_template('discover.html',title = title)


# Login
@app.route('/login')
def login():

    title = "The couch potato - Log In"
    return render_template('login.html',title = title)


# sign up
@app.route('/signup')
def signup():

    title = "The couch potato - Sign Up"
    return render_template('signup.html',title = title)
