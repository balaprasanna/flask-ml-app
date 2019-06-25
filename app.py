import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PORT = int(os.getenv("PORT", 5000))

@app.route("/")
def hello():
    return "Hello World!"


app.run(host='0.0.0.0', port=PORT)