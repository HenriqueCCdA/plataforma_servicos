from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import usuario_model


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Remember me')
    submit = SubmitField('LogIn')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField("Email", validators=[Email(), DataRequired()])
    #--adcionando ---
    empresa = StringField('Empresa', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    pais = StringField('País', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired()])
    # -- add ---
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')

    @staticmethod
    def validate_email(self, email):
        user = usuario_model.User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este Email já Existe!')

    