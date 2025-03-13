from flask import Flask
from controllers.expiry_controller import expiry_bp
from utils.error_handler import error_handler
from utils.logger import logger
from config import PORT
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(expiry_bp, url_prefix="/api")
error_handler(app)

if __name__ == "__main__":
    logger.info(f"Starting app on port {PORT}")
    app.run(host="0.0.0.0", port=PORT)
