from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ClassifyForm(FlaskForm):
  textarea = TextAreaField('Enter text here:', validators=[DataRequired(), Length(min=30)])
  submit = SubmitField('Classify Text')