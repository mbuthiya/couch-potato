from  flask import render_template,redirect,url_for,session
from app import app
from .forms import SearchForm
# Index route
@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    '''
    Index view function that handles request to the index route

    Returns:
        Returns the index html page
    '''
    title = "The couch potato - Home"

    # Initializes  the search form
    form = SearchForm()

    # Checks if form is valid
    if form.validate_on_submit():
        search = form.search_item.data
        form.search_item.data = ''

        # Redirects to the search page
        return redirect(url_for('search',item = search))

    return render_template('index.html', title= title,form =form)


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
@app.route('/news')
def discover():
    '''
    News view  function  to display Random tv shows

    '''
    title = "The couch potato - News"
    return render_template('news.html',title = title)


@app.route('/search/<item>',methods =['GET','POST'])
def search(item):
    '''
    Search view  function  to display searched item tags

    '''
    form = SearchForm()

    if form.validate_on_submit():

        item = form.search_item.data

        session['item'] = form.search_item.data

        form.search_item.data =''

        return redirect(url_for('search',item =item))


    return render_template('search.html',item = item,form=form)
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
