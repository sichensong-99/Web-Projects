from flask_wtf import FlaskForm
from wtforms import FileField



class UploadForm(FlaskForm):
    file_csv = FileField()