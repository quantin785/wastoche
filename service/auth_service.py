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
    """
    Fonction pour crée un compte utilisateur et stocker les informations dans la bddd

    :param username:
    :param email:
    :param password:
    :return: "message": "Utilisateur créé avec succès !"
    """
    if User.query.filter_by(email=email).first(): # cherche si l'email existe déja si oui je retourn une exeption
        raise AuthError("Cet email existe déjà", 400)

    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password) # créer une instance de la classe User
    db.session.add(user) # Ajouter le user a la bdd
    db.session.commit()
    return {"message": "Utilisateur créé avec succès !"}


def login(username_or_email: str,password: str):
    """
    Fonction pour s'authentifier et récuperer le JWT

    :param username_or_email:
    :param password:
    :return: {"token": token, "username": user.username}
    """
    user = User.query.filter(
        (User.email == username_or_email) | (User.username == username_or_email)
    ).first() # cherche si l'email ou le username existe déja
    if not user:
        raise AuthError("Identifier ou mot de passe incorrect", 404) # Retourne une exeption si il n'a pas trouver dans la bdd

    token = create_access_token(identity=user.username) # Crée un JWT qui contient les info du user
    return {"token": token, "username": user.username}