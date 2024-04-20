from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

#create a form class 
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# create a route decorator
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/link')

def link():
    return render_template("linkk.html")

#create name page
@app.route('/name', methods = ['GET','POST'])
def name():
    return render_template("user.html")