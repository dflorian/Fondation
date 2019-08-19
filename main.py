from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from config import Config
from contact_form import ContactForm

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

@app.route("/home/")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your email has been added to our client database'.format(
            form.full_name.data, form.email.data))
        return redirect(url_for('contact'))
    return render_template("contact.html", title='Contact', form=form)

@app.route("/faq/")
def faq():
    return render_template("faq.html")

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