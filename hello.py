from flask import Flask, render_template

# create flask instance
app = Flask(__name__)

# create a route decorator
@app.route('/')

def index():
    return render_template("index.html")
