
## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/brandgit/TP_API1.git
cd data-integration2
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # Sur macOS/Linux
# ou
env\Scripts\activate     # Sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Optionnel) Créer un superutilisateur

```bash
python manage.py createsuperuser
```

## ⚙️ Configuration

Le projet utilise une configuration Django standard avec :
- Base de données SQLite (fichier `db.sqlite3`)
- Debug activé en mode développement
- Django REST Framework pour les API

## 🚀 Démarrage

### Démarrage local

```bash
# Activer l'environnement virtuel
source env/bin/activate

# Démarrer le serveur de développement
python manage.py runserver
```

L'application sera accessible sur : `http://localhost:8000`

### Interface d'administration

Accédez à l'interface d'administration Django : `http://localhost:8000/admin`

## 📡 Endpoints API

### Base URL : `http://localhost:8000/api/`

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/api/test_json_view/` | Test simple retournant du JSON |
| `POST` | `/api/test_post_view/` | Test d'endpoint POST |
| `GET` | `/api/products/` | Liste paginée des produits (3 par page) |
| `GET` | `/api/products/expensive/` | Produit le plus cher |
| `POST` | `/api/products/create/` | Créer un nouveau produit |
| `PUT` | `/api/products/<id>/update/` | Mettre à jour un produit |

### Exemples d'utilisation

#### Créer un produit

```bash
curl -X POST http://localhost:8000/api/products/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15",
    "price": 999.99,
    "description": "Dernier iPhone d'Apple"
  }'
```

#### Récupérer la liste des produits

```bash
curl http://localhost:8000/api/products/
```

#### Mettre à jour un produit

```bash
curl -X PUT http://localhost:8000/api/products/1/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15 Pro",
    "price": 1199.99,
    "description": "iPhone 15 Pro avec fonctionnalités avancées"
  }'
```

## 🐳 Docker

### Démarrer avec Docker Compose

```bash
# Construire et démarrer les conteneurs
docker-compose up --build

# Démarrer en arrière-plan
docker-compose up -d
```
