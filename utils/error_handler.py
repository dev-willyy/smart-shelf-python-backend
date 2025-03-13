from flask import jsonify


def error_handler(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({"error": "Internal Server Error"}), 500
