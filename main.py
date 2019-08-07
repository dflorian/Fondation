from flask import Flask
from flask import render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
import re

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/sandbox/")
def sandbox():
    return render_template("sandbox.html")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)