from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField, StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import required, length


class UploadForm(FlaskForm):
    file = FileField('Image', validators=[required(), FileAllowed(['rar', 'zip'], 'Envie Arquivos no formato .zip e .rar')])
    descricao = TextAreaField('Descrição', validators=[required(), length(max=1000, message='Campo com mais de 1000 caracteres.')])
    servico = SelectField("Serviço", validators=[required()], choices=[("Dosimetria Clínica"), ("Dosimetria Pré-Clínica"), 
                                                                        ("Segmentação e Quantificação"), ("Modelagem Computacional"),
                                                                        ("Radiosinoviortese")])
    submit = SubmitField('Enviar')
