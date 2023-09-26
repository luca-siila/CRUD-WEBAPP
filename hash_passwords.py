from werkzeug.security import generate_password_hash
from models import User, db
from app import app

with app.app_context():  
    users = User.query.all()  # get all users

    for user in users:
        plaintext_password = user.password_hash
        hashed_password = generate_password_hash(plaintext_password)
        user.password_hash = hashed_password  # replace with hashed password
        db.session.commit()  # commit the changes
