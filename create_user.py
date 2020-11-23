from app import db
import os
from app.models import usuario_model
from app import create_app
from config import app_config

db.create_all()
app = create_app("development")





u = usuario_model.User(username='admin', email='admin@admin.com', is_admin=True)
u.set_password('@admin.admin')
with app.app_context():
    db.session.add(u)
    db.session.commit()
    print("ok... fim")