from my_server import app
from my_server.forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, flash

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'me@me.me' and form.password.data == 'password':
            flash('User successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful!', 'warning')

    return render_template('login.html', form=form)