from app import app
app.config['SECRET_KEY']="fruity"

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class SearchForm(Form):
    search_item = StringField('',validators=[Required()],render_kw={'placeholder':'Search'})
    submit =SubmitField('Submit')
