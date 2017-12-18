# from flask_wtf import Form
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, SelectField, FieldList, FormField, TextField
from wtforms.validators import DataRequired, Email

# 'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
# 'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
# 'SelectMultipleField', 'StringField',

# 'BooleanField', 'TextAreaField', 'PasswordField', 'FileField',
#     'HiddenField', 'SubmitField', 'TextField'

class UsernamePasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class EmailPasswordForm(Form):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeatpassword = PasswordField('Repeat Password', validators=[DataRequired()])

class ChangePasswordForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])
    repeatpassword = PasswordField('Repeat Password', validators=[DataRequired()])

class EmailForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])

class PasswordForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])


from models import asset, asset_value_domain_attributes, survey, park

class ParkForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])

class AssetForm(Form):
    assets = survey().asset_heads()
    practice_heads = survey().practice_heads()
    value_heads = survey().value_heads()

class SurveyForm(Form):
    survey=survey()
