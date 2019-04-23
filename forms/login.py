from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

# form used to log in to the chatroom, this provide


class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=35)])
    submit = SubmitField('Log In')
