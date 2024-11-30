from app import app, db  
from models import User
from werkzeug.security import generate_password_hash

username = 'johnmacaraeg'
email = 'johnmacaraeg@gmail.com'
password = '123456'

with app.app_context():
    existing_admin = User.query.filter_by(username=username).first()
    if existing_admin:
        print("The administrator user already exists.")
    else:
        admin_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password),
            is_admin=True  
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Manager created successfully.")
