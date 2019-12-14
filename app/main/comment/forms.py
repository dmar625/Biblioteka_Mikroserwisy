from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField(u"Twoja recenzja książki",
                            validators=[DataRequired(message=u"Zawartość nie może być pusta"), Length(1, 1024, message=u"Recenzje książek są ograniczone do 1024 znaków")])
    submit = SubmitField(u"Zatwierdź")
