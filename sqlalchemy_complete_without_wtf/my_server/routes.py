from sqlalchemy.orm import undefer_group
from my_server import app, db
from my_server.models import User
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def start():
    return render_template('index.html')

# Add user
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')
    
    new_user = User(name=request.form['name'], email=request.form['email'])
    
    db.session.add(new_user)
    db.session.commit()

    flash('User added successfully!', 'success')

    return redirect(url_for('list_users'))


@app.route('/user/list', methods=['GET'])
@app.route('/user/list/<id>', methods=['GET'])
def list_users(id=None):
    if id is None:
        users_to_show = User.query.all()
    else:
        users_to_show = [User.query.get(id)]

    return render_template('list_users.html', users=users_to_show)

@app.route('/user/update/<id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get(id)

    if request.method == 'GET':
        return render_template('update_user.html', user=user)
    
    user.name = request.form['name']
    user.email = request.form['email']
    db.session.commit()

    flash('User updated successfully', 'success')

    return redirect(url_for('list_users'))


@app.route('/user/delete/<id>', methods=['GET'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    flash('User deleted successfully', 'success')
    return redirect(url_for('list_users'))
