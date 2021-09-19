from my_server import app, db
from my_server.models import User, Post
from my_server.forms import RegistrationForm, LoginForm, NewPostForm
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password == form.password.data:
            #note that remember is a boolean
            login_user(user, remember=form.remember.data)
            flash(f'User "{user.username}" successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful!', 'warning')

    return render_template('login.html', form=form)


# Note that the login_required needs to be below the path.
@app.route('/post/list')
@login_required
def list_posts():
    posts = current_user.posts
    return render_template('list_posts.html', posts=posts)


@app.route('/post/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Post added successfully', 'success')
        return redirect(url_for('list_posts'))
    
    return render_template('add_post.html', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))