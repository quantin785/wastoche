from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from extension import db, jwt
from route.auth_route import auth_bp

app = Flask(__name__)

# Configuration de la base de données (exemple avec SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ma_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ma_cle_super_secrete'

db.init_app(app)  # ⚙️ lier la base de données à l’app ici
jwt.init_app(app)


# Enregistrement du blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"



if __name__ == '__main__':
    app.create_app(debug=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)