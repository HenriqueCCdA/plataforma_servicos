from flask import render_template, request, url_for, flash, send_file
from flask_login import login_required, current_user
from werkzeug.utils import redirect, secure_filename
from app.main import bp
from app.main.forms import UploadForm
from app import usuario_model, db
from app import s3_connection


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("index.html")


@bp.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            file = form.file.data
            if file != '':
                filename = secure_filename(file.filename)

                name = str(current_user.id) + '_' + '_' + filename

                #validar o nome do arquivo antes de enviar
                f_name = usuario_model.FileContents.query.filter_by(file_name=name).first()

                if f_name is None:
 
                    s3_connection.upload_s3(file, name)
                

                    new_file = usuario_model.FileContents(descricao=form.descricao.data, 
                                                        servico=form.servico.data,
                                                        file_name=name, 
                                                        user_id=current_user.id)
                    db.session.add(new_file)
                    db.session.commit()
                    flash("Arquivo Enviado com Sucesso!", "success")
                    return redirect(url_for('main.upload'))
                else:
                    flash("Já existe um arquivo com este nome. Renomei-o!", "danger")

                

    return render_template("upload.html", form=form)


@bp.route("/download/<int:id_arq>")
def download(id_arq):

    file = usuario_model.FileContents.query.filter_by(id=id_arq).first()
    arquivo_name = file.file_name

    url = s3_connection.download_s3(arquivo_name)

    return redirect(url) 


@bp.route("/lista", methods=["GET"])
def lista():

    # clientes = usuario_model.FileContents.query.all()
    cliente = usuario_model.FileContents.query.filter_by(user_id=current_user.id).all()
    return render_template("listar_arquivos.html", dados=cliente)


@bp.route("/principal", methods=["GET", "POST"])
def principal():

    return render_template("principal.html")

@bp.route("/upload_new", methods=["GET", "POST"])
def upload_new():

    return render_template("upload_new.html")