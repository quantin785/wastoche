from flask import Blueprint, request, jsonify
from service.auth_service import login, AuthError, register

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login_route():
    try:
        data = request.get_json()
        username_or_email = data.get('username')
        password = data.get('password')

        if not username_or_email or not password:
            return jsonify({"error": "Champs manquants"}), 400

        result = login(username_or_email, password)
        return jsonify(result), 200

    except AuthError as e:
        return jsonify({"error": e.message}), e.status_code

    except Exception as e:
        # fallback en cas d’erreur non prévue
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/register', methods=['POST'])
def register_route():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"error": "Champs manquants"}), 400

        result = register(username, email,password)
        return jsonify(result), 200

    except AuthError as e:
        return jsonify({"error": e.message}), e.status_code

    except Exception as e:
        # fallback en cas d’erreur non prévue
        return jsonify({"error": str(e)}), 500
