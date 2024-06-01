from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField('Name of student', [validators.DataRequired("Please enter you name.")])
    Gender = RadioField('Gender', choices=[('M','Male'),('F','Female')])
    Address = TextAreaField("Address")

    email = StringField('Email',[validators.DataRequired("Please enter your email address."),validators.Email('Please enter your mail')])

    Age = IntegerField("age")
    language = SelectField('Languages', choices=[('cpp','c++'),('py','python')])
    submit = SubmitField("Send")