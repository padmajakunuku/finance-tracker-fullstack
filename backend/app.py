from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db

app = Flask(__name__)
CORS(app)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change later

# Init extensions
db.init_app(app)
jwt = JWTManager(app)

@app.route("/")
def home():
    return {"status": "Finance Tracker Backend Running"}

# Create DB tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created")

if __name__ == "__main__":
    app.run(debug=True)




