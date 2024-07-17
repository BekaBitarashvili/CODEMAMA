from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class RegistrationForm(FlaskForm):
    username = StringField('მომხმარებელი', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('ელ.ფოსტა', validators=[DataRequired(), Email()])
    password = PasswordField('პაროლი', validators=[DataRequired()])
    confirm_password = PasswordField('გაიმეორე პაროლი', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("რეგისტრაცია")


class LoginForm(FlaskForm):
    email = StringField('ელ.ფოსტა', validators=[DataRequired(), Email()])
    password = PasswordField('პაროლი', validators=[DataRequired()])
    remember = BooleanField('დამიმახსოვრე')
    submit = SubmitField("ავტორიზაცია")