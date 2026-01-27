from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Transaction

app = Flask(__name__)
CORS(app)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change later

# Init extensions
db.init_app(app)
jwt = JWTManager(app)

# Home route
@app.route("/")
def home():
    return {"status": "Finance Tracker Backend Running"}

# Register route
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"access_token": token}), 200

# Add transaction (PROTECTED)
@app.route("/transaction", methods=["POST"])
@jwt_required()
def add_transaction():
    data = request.get_json()
    user_id = get_jwt_identity()

    if not data or not data.get("amount") or not data.get("category") or not data.get("type"):
        return jsonify({"error": "Amount, category, and type required"}), 400

    if data["type"] not in ["income", "expense"]:
        return jsonify({"error": "Type must be income or expense"}), 400

    transaction = Transaction(
        amount=data["amount"],
        category=data["category"],
        type=data["type"],
        user_id=user_id
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Transaction added successfully"}), 201

# Get transactions (PROTECTED)
@app.route("/transactions", methods=["GET"])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()

    transactions = Transaction.query.filter_by(user_id=user_id).all()

    return jsonify([
        {
            "id": t.id,
            "amount": t.amount,
            "category": t.category,
            "type": t.type,
            "date": t.date
        }
        for t in transactions
    ])

# Create DB tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created")

if __name__ == "__main__":
    app.run(debug=True)
