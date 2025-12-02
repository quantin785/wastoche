import re

from flask import jsonify

from service.auth_service import AuthError

EMAIL_REGEX = re.compile(
    r"^(?!\.)[\w.\-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

PASSWORD_REGEX = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.,;:_\-])[A-Za-z\d@$!%*?&.,;:_\-]{12,}$'
)

def check_credentials( username: str, password: str):
    if not username or not password:
        raise AuthError('username and password is required', 400)


def check_register_crendentials(email:str, username: str, password: str):
    if not username or not password:
        raise AuthError('username and password is required', 400)

    check_email_format(email)
    check_password_strength(password)

    if username.len() < 7:
        raise AuthError('username is too short', 400)


def check_password_strength(password: str):
    if not PASSWORD_REGEX.match(password):
        raise AuthError(
            "Le mot de passe doit contenir au moins 12 caractères, "
            "une majuscule, une minuscule, un chiffre et un caractère spécial."
        , 400)


def check_email_format(email: str):
    if not EMAIL_REGEX.match(email):
        raise ValueError("Adresse e-mail invalide.")
    return True

