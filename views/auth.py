from flask import render_template, request, redirect, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash

from . import app, db
from models.user import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}")
        print(f"Password: {password}")

        user = User.query.filter_by(username=username).first()
        print(f"User from DB: {user}")

        if user is None or not user.verify_password(password):
            # The user doesn't exist or the password is wrong
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')
