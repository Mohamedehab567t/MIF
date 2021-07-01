from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , RadioField, TextAreaField
from wtforms.validators import DataRequired, Email
from functions import validate_email

class EmailForm (FlaskForm):
    email = StringField('email', validators=[DataRequired(message="Please Enter Your Email"),
                                             Email(message="Not An Email") , validate_email])
    submit = SubmitField('Login')


class VoteForm(FlaskForm):
    disagree = RadioField('vote' , choices=[('agree' , 'موافق'),('disagree' , 'مش موافق')])


class Qform(FlaskForm):
    question = TextAreaField('Question' , render_kw={"rows" : 5 , "cols" : 11} , validators=[DataRequired()])
    submit = SubmitField('Send')