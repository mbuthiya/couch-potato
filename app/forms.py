from app import app
app.config['SECRET_KEY']="fruity"

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class SearchForm(Form):
    search_item = StringField('Search for movies tv shows or blog tags ',validators=[Required()])
    submit =SubmitField('Submit')
