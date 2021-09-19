from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from my_server.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])

    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    confirm_password = PasswordField('Confirm password', validators=[
        DataRequired(),
        EqualTo('password')
    ])

    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The username already exists.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('The email already exists.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    remember = BooleanField('Remember me')

    submit = SubmitField('Login')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])

    content = StringField('Content', validators=[
        DataRequired()
    ])

    submit = SubmitField('Post')