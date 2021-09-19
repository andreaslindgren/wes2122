from my_server import app, db
from my_server.models import User
from my_server.forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, flash

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        
        db.session.add(new_user)
        db.session.commit()

        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password == form.password.data:
            flash(f'User "{user.username}" successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful!', 'warning')

    return render_template('login.html', form=form)