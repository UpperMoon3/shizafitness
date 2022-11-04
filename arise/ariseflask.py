from flask import Flask, request, render_template, redirect, url_for
import psycopg2
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecretmyfriendo!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/madi/arise7.db'
Bootstrap(app)
bd = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(bd.Model, UserMixin):
    id = bd.Column(bd.Integer, primary_key=True)
    username = bd.Column(bd.String(15), unique=True)
    email = bd.Column(bd.String(50), unique=True)
    password = bd.Column(bd.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        bd.session.add(new_user)
        bd.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/id1')
@login_required
def id1():
    return render_template('id1.html')

@app.route('/id2')
@login_required
def id2():
    return render_template('id2.html')

@app.route('/id3')
@login_required
def id3():
    return render_template('id3.html')

@app.route('/id4')
@login_required
def id4():
    return render_template('id4.html')

@app.route('/id5')
@login_required
def id5():
    return render_template('id5.html')

@app.route('/id6')
@login_required
def id6():
    return render_template('id6.html')

@app.route('/id7')
@login_required
def id7():
    return render_template('id7.html')

@app.route('/id8')
@login_required
def id8():
    return render_template('id8.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)