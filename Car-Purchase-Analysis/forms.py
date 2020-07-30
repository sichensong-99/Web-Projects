from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, SelectField, RadioField, FileField,DateField
from wtforms.validators import DataRequired, Email, Length, InputRequired

class RegisterForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=20)])
    age = RadioField('Select age',choices=[('10-30','10-30'),('30-50',' 30-50'), ('50-70',' 50-70')])
    feedback= FileField('Upload file')
    experience=TextAreaField("Shopping experience")
    gender = SelectField('Select gender', choices=[('female', 'female'), ('male', 'male'), ('No provide', 'No provide')])
    checkbox =BooleanField("Agree to terms and conditions")
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Login")


class UploadForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    dob = DateField()
    email = StringField()
    file_photo = FileField()
    file_csv = FileField()
    comments = TextAreaField()
    submit = SubmitField("Upload")

class ProfileForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    file_photo = StringField()
    
class TableForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    dob = StringField()

class EmployeeForm(FlaskForm):
    file_csv = FileField()

class SalesForm(FlaskForm):
    file_csv = FileField()
    