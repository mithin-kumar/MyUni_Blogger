from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,SubmitField ,BooleanField
from wtforms.validators import DataRequired,length,Email ,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),length(min=2 ,max=20)])
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('confiram_Password', validators= [DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign-up')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember= BooleanField('Remember me')
    submit = SubmitField('Sign-in')