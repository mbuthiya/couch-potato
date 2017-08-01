from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
    '''
    Returns a custom error page for any 400 server errors encountered
    '''

    title = "Sorry we couldnt find that"
    return render_template('404.html', title=title),404


@app.errorhandler(500)
def internal_server_error(e):

    '''
    Returns a custom error page for any 500 server errors encountered
    '''

    title = "Its not you its us"
    return render_template('500.html', title=title),500
