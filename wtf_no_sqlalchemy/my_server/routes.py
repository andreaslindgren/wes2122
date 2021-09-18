from sqlalchemy.orm import undefer_group
from my_server import app, db
from my_server.models import User
from my_server.forms import RegistrationForm, LoginForm
from flask import render_template, request, redirect, url_for, flash

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


# # Add user
# @app.route('/user/add', methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'GET':
#         return render_template('add_user.html')
    
#     new_user = User(name=request.form['name'], email=request.form['email'])
    
#     db.session.add(new_user)
#     db.session.commit()

#     flash('User added successfully!', 'success')

#     return redirect(url_for('list_users'))


# @app.route('/user/list', methods=['GET'])
# @app.route('/user/list/<id>', methods=['GET'])
# def list_users(id=None):
#     if id is None:
#         users_to_show = User.query.all()
#     else:
#         users_to_show = [User.query.get(id)]

#     return render_template('list_users.html', users=users_to_show)

# @app.route('/user/update/<id>', methods=['GET', 'POST'])
# def update_user(id):
#     user = User.query.get(id)

#     if request.method == 'GET':
#         return render_template('update_user.html', user=user)
    
#     user.name = request.form['name']
#     user.email = request.form['email']
#     db.session.commit()

#     flash('User updated successfully', 'success')

#     return redirect(url_for('list_users'))


# @app.route('/user/delete/<id>', methods=['GET'])
# def delete_user(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()

#     flash('User deleted successfully', 'success')
#     return redirect(url_for('list_users'))
