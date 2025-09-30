from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import routes
import os

# Define a pasta onde está o frontend
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="/")
CORS(app)

# Registra as rotas da API
app.register_blueprint(routes, url_prefix="/api")

# Rota para servir o index.html
@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_DIR, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
