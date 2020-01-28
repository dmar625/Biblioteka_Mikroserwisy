# -*- coding: utf-8 -*-
from library_services.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    isbn = StringField(u"ISBN",
                       validators=[DataRequired(message=u"Pole nie może być puste"),
                                   Regexp('[0-9]{13,13}', message=u"ISBN musi składać się z 13 cyfr")])
    title = StringField(u"Tytuł książki",
                        validators=[DataRequired(message=u"Pole nie może być puste"), Length(1, 128, message=u"Długość znaków od 1 do 128")])
    origin_title = StringField(u"Oryginalny tytuł", validators=[Length(0, 128, message=u"Długość znaków od 0 do 128")])
    subtitle = StringField(u"Podtytuł", validators=[Length(0, 128, message=u"Długość znaków od 0 do 128")])
    author = StringField(u"Autor", validators=[Length(0, 128, message=u"Nazwa autora od 0 do 64 znaków")])
    translator = StringField(u"Tłumacz",
                             validators=[Length(0, 64, message=u"Nazwa tłumacza od 0 do 64 znaków")])
    publisher = StringField(u"Wydawca", validators=[Length(0, 64, message=u"Nazwa wydawcy od 0 do 64 znaków")])
    image = StringField(u"Okładka", validators=[Length(0, 128, message=u"Od 0 do 128 znaków")])
    pubdate = StringField(u"Data publikacji", validators=[Length(0, 32, message=u"Od 0 do 32 znaków")])
    tags = StringField(u"Tagi", validators=[Length(0, 128, message=u"Od 0 do 128 znaków")])
    pages = IntegerField(u"Strony")
    price = StringField(u"Cena", validators=[Length(0, 64, message=u"Od 0 do 32 znaków")])
    binding = StringField(u"Okładka", validators=[Length(0, 16, message=u"Od 0 do 16 znaków")])
    numbers = IntegerField(u"Ilość", validators=[DataRequired(message=u"Pole nie może być puste")])
    summary = PageDownField(u"Podsumowanie")
    catalog = PageDownField(u"Katalog")
    submit = SubmitField(u"Zatwierdzenie zmian")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(u'Ten sam numer ISBN już istnieje i nie można go wprowadzić, sprawdź dokładnie, czy książka jest w magazynie.')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"Szukaj")


