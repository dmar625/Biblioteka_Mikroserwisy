from library_services import db
from library_services.models import User
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import LoginForm, RegistrationForm, ChangePasswordForm


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        the_user = User.query.filter(User.email.ilike(login_form.email.data)).first()
        if the_user is not None and the_user.verify_password(login_form.password.data):
            login_user(the_user, login_form.remember_me.data)
            flash(u'Udało Ci się zalogować, witaj %s!' % the_user.name, 'success')
            return redirect(request.args.get('next') or url_for('base.index'))
        flash(u'Niepoprawna nazwa użytkownika lub hasło.', 'danger')
    return render_template("login.html", form=login_form, title=u"Zaloguj się")


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash(u'Wylogowano.', 'info')
    return redirect(url_for('base.index'))


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        the_user = User(email=form.email.data,
                        name=form.name.data,
                        password=form.password.data)
        db.session.add(the_user)
        db.session.commit()
        flash(u'Zarejestrowałeś się, witaj %s!' % form.name.data, 'success')
        login_user(the_user)
        return redirect(request.args.get('next') or url_for('base.index'))
    return render_template('register.html', form=form, title=u"Zarejestrowano nowego użytkownika")


@auth.route('/change_password/', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.password = form.new_password.data
        db.session.add(current_user)
        db.session.commit()
        flash(u'Hasło zostało zaktualizowane.', 'info')
        return redirect(url_for('clients.detail', user_id=current_user.id))
    return render_template('user_edit.html', form=form, user=current_user, title=u"Zmiana hasła")
