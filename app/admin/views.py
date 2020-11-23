from flask import abort, render_template, url_for, flash, jsonify
from werkzeug.utils import redirect

from app import db
from app.admin import bp
from flask_login import current_user, login_required

from app.auth.forms import RegistrationForm
from app.models import usuario_model
from app import s3_connection
import boto3
import botocore
import requests

def check_admin():
    if not current_user.is_admin:
        abort(403)


@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    check_admin()

    lista = usuario_model.User.query.all()

    form = RegistrationForm()
    if form.validate_on_submit():
        user = usuario_model.User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabéns, Cadastro com Sucesso!')
        return redirect(url_for('admin.dashboard'))
    

    return render_template('admin/admin_dashboard.html', lista=lista, form=form)


@bp.route('/requisicoes', methods=['GET', 'POST'])
@login_required
def requisicoes():

    check_admin()

    lista_req = usuario_model.FileContents.query.all()

    return render_template('admin/admin_requisicoes.html', lista=lista_req)


@bp.route("/download/<int:id_arq>")
def download(id_arq):

    file = usuario_model.FileContents.query.filter_by(id=id_arq).first()
    arquivo_name = file.file_name

    url = s3_connection.download_s3(arquivo_name)

    return redirect(url)
    


def deletar_usuario():
    return "usuario deletado"


def editar_usuario():
    return "usuario editado"