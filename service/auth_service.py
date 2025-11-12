from flask import jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from entity.user import db
from entity.user import User

class AuthError(Exception):
    def __init__(self, message, status_code=401):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


def register(username: str, email: str, password: str):
    print(username, email, password)
    if User.query.filter_by(email=email).first():
        raise AuthError("Cet email existe déjà", 400)

    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return {"message": "Utilisateur créé avec succès !"}


def login(username_or_email: str,password: str):
    user = User.query.filter(
        (User.email == username_or_email) | (User.username == username_or_email)
    ).first()

    if not user:
        raise AuthError("Identifier ou mot de passe incorrect", 404)

    token = create_access_token(identity=user.id)
    return {"token": token, "username": user.username}