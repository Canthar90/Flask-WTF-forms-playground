from flask import Flask, render_template, request
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, email_validator, InputRequired, ValidationError
from flask_bootstrap import Bootstrap


import os


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(),  Email()])
    password = PasswordField(label='Password', validators=[validators.Length(min=8, max=200), DataRequired()])
    submit = SubmitField(label='Log in')

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app
app = create_app()
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'] )
def login():
    form_login = LoginForm(request.form)
    # if form_login.validate():
    if form_login.validate_on_submit():
        print("succes")
        inputed_email = form_login.email.data
        inputed_password = form_login.password.data
        expected_email = "admin@email.com"
        expected_password = "12345678"
        print(f"Data aqured email: {inputed_email} password: {inputed_password}")
        if inputed_email == expected_email and inputed_password == expected_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form_login)




if __name__ == '__main__':
    app.run(debug=True)