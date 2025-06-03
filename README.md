# 📦 TP API - Data Integration Project

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/brandgit/TP_API1.git
cd data-integration2

### 2. Create a virtual environment

python -m venv env

# On macOS/Linux:
source env/bin/activate

# On Windows:
env\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Initialize the database

python manage.py makemigrations
python manage.py migrate

5. (Optional) Create a superuser

python manage.py createsuperuser

⚙️ Configuration

Framework: Django + Django REST Framework
Database: SQLite (db.sqlite3)
Mode: Development (DEBUG = True)

🚀 Running the Application

Locally

# Activate the virtual environment
source env/bin/activate

# Start the development server
python manage.py runserver

Application available at: http://localhost:8000

Admin Interface
Available at: http://localhost:8000/admin

📡 API Endpoints

Base URL: http://localhost:8000/api/

Method	Endpoint	Description
GET	/api/test_json_view/	Simple test returning JSON
POST	/api/test_post_view/	Test a POST request
GET	/api/products/	Paginated list of products (3/page)
GET	/api/products/expensive/	Most expensive product
POST	/api/products/create/	Create a new product
PUT	/api/products/<id>/update/	Update an existing product

📥 Usage Examples

🔧 Create a product

curl -X POST http://localhost:8000/api/products/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15",
    "price": 999.99,
    "description": "Latest iPhone from Apple"
  }'

📃 List all products

curl http://localhost:8000/api/products/

✏️ Update a product

curl -X PUT http://localhost:8000/api/products/1/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15 Pro",
    "price": 1199.99,
    "description": "iPhone 15 Pro with advanced features"
  }'

🐳 Docker Support

Run with Docker Compose

# Build and start the containers
docker-compose up --build

# Or run in detached mode
docker-compose up -d

