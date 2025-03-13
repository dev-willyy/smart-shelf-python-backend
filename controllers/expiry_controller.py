from flask import Blueprint, request, jsonify
from services.open_food_facts_service import fetch_product_info
from services.advanced_ml_service import compute_spoilage
from config import ALLOWED_FOOD_CATEGORIES

expiry_bp = Blueprint("expiry", __name__)


@expiry_bp.route("/predict-expiry", methods=["POST"])
def predict_expiry():
    data = request.get_json()
    barcode = data.get("barcode")
    temperature = data.get("temperature")
    humidity = data.get("humidity")

    if not barcode or temperature is None or humidity is None:
        return jsonify({"error": "Missing barcode, temperature, or humidity."}), 400

    product_info = fetch_product_info(barcode)
    if not product_info:
        return jsonify({"error": "Product not found in Open Food Facts."}), 404

    if product_info.get("category", "").lower() not in [cat.lower() for cat in ALLOWED_FOOD_CATEGORIES]:
        return jsonify({"error": "The scanned product is not recognized as a food product."}), 400

    spoilage = compute_spoilage(
        product_info["category"].lower(), float(temperature), float(humidity)
    )

    result = {
        "barcode": product_info["barcode"],
        "productName": product_info["name"],
        "category": product_info["category"],
        "recommendedTemp": spoilage["recommended_temp"],
        "recommendedHumidity": spoilage["recommended_humidity"],
        "actualTemperature": temperature,
        "actualHumidity": humidity,
        "predictedSpoilageDays": spoilage["predicted_spoilage_days"]
    }
    return jsonify(result), 200
