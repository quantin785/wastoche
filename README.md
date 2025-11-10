# Flask Hello World

Une application Flask simple qui affiche "Hello World".

## Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/projetgit
cd projet
```

### 2. Créer un environnement virtuel

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Sur macOS/Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Si vous n'avez pas de fichier `requirements.txt`, installez Flask directement :
```bash
pip install flask
```

## Lancement de l'application

### Mode développement

```bash
flask run
```

ou

```bash
python app.py
```

L'application sera accessible à l'adresse : `http://127.0.0.1:5000`

### Avec le mode debug activé

```bash
flask run --debug
```

## Structure du projet

```
flask-hello-world/
│
├── app.py              # Fichier principal de l'application
├── requirements.txt    # Liste des dépendances
└── README.md          # Ce fichier
```

## Exemple de code (app.py)

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

## requirements.txt

```
Flask==3.0.0
```

## Contribuer

## Ajout de l'entité User

```python
class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

```

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou soumettre une pull request.

## Licence

Ce projet est sous licence MIT.


