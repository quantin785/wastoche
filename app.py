from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy

from extension import db, jwt
from route.auth_route import auth_bp

app = Flask(__name__)

# Configuration de la base de données (exemple avec SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ma_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '2795d16c7e798c37d33d14c01802e692f4edb050d552870e9cbab97cdf78ffa9'

db.init_app(app)  # ⚙️ lier la base de données à l’app ici
jwt.init_app(app)


# Enregistrement du blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.get("/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f"Bienvenue {current_user}, tu es authentifié 🎉"), 200

if __name__ == '__main__':
    app.create_app(debug=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)