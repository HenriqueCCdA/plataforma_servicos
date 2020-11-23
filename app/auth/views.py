from app import db
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import usuario_model
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm


@bp.route("/login", methods=['GET', 'POST'])
def login():
    er=None
    form = LoginForm()
    if form.validate_on_submit():

        user = usuario_model.User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):

            login_user(user)#, remember=form.remember_me.data)

            if user.is_admin:
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('main.index'))
        else:
            er='email invalido'
            flash('Email ou Senha Invalido!')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html', form=form, er=er)


@bp.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@bp.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = usuario_model.User(username=form.username.data, email=form.email.data, empresa=form.empresa.data,
        telefone=form.telefone.data, endereco=form.endereco.data, pais=form.pais.data, estado=form.estado.data, cep=form.cep.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuário Cadastrado!')
        return redirect(url_for('auth.login'))
    return render_template('auth/registrar.html', form=form)
