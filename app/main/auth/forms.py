from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"Wypełnij pola!"), Length(1, 64), Email(message=u"Czy to prawidłowy email?")])
    password = PasswordField(u'Hasło', validators=[DataRequired(message=u"Pole nie może być puste"), Length(6, 32)])
    remember_me = BooleanField(u"Zapamiętaj mnie", default=True)
    submit = SubmitField(u'Zaloguj')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"Wypełnij pola!"), Length(1, 64), Email(message=u"Czy to prawidłowy email?")])
    name = StringField(u'Nazwa użytkownika', validators=[DataRequired(message=u"Pole nie może być puste"), Length(1, 64)])
    password = PasswordField(u'Hasło',
                             validators=[DataRequired(message=u"Pole nie może być puste"), EqualTo('password2', message=u'Hasła muszą się zgadzać'),
                                         Length(6, 32)])
    password2 = PasswordField(u'Potwierdź hasło ponownie', validators=[DataRequired(message=u"Pole nie może być puste")])
    submit = SubmitField(u'Zarejestruj się')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'Email jest już zarejestrowany')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'Obecne hasło', validators=[DataRequired(message=u"Pole nie może być puste")])
    new_password = PasswordField(u'Nowe hasło', validators=[DataRequired(message=u"Pole nie może być puste"),
                                                     EqualTo('confirm_password', message=u'Hasła muszą się zgadzać'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Potwierdź nowe hasło', validators=[DataRequired(message=u"Pole nie może być puste")])
    submit = SubmitField(u"Zapisz nowe hasło")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'Oryginalne hasło jest nieprawidłowe')
