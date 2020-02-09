from flask import Flask, render_template, redirect, url_for

from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://pjbxgzvuxwsyax:bc9c5cc029566f85ed4de92f5ea04f91742acb5037485c9770206910785c55dd@ec2-184-72-236-57.compute-1.amazonaws.com:5432/d2sprdqh7as62s'
db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Updated database if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Add user to DB
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    # Allow user to login if no validation error
    if login_form.validate_on_submit():
        return "Logged in finally!"

    return render_template("login.html", form=login_form)

if __name__ == "__main__":

    app.run(debug=True)
