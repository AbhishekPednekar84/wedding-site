from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TestimonialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    message = TextAreaField('Your Message', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Post Message')
