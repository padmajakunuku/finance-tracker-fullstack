from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "Finance Tracker Backend Running"}

if __name__ == "__main__":
    app.run(debug=True)
