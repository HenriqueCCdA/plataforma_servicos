from datetime import datetime

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    
    empresa = db.Column(db.String(20), index=True)
    telefone = db.Column(db.String(40), index=True)
    endereco = db.Column(db.String(50), index=True)
    pais = db.Column(db.String(10), index=True)
    estado = db.Column(db.String(10), index=True)
    cep = db.Column(db.String(10), index=True)

    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    files = db.relationship('FileContents', backref='user', lazy='dynamic')
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class FileContents(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(1000), index=True)
    servico = db.Column(db.String(50), index=True)
    file_name = db.Column(db.String(60))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.String(15), default='Enviado')
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
