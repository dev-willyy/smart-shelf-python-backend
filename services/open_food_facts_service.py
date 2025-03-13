import requests

OFF_URL = "https://world.openfoodfacts.org/api/v0/product"


def fetch_product_info(barcode):
    try:
        response = requests.get(f"{OFF_URL}/{barcode}.json")
        data = response.json()
        if data.get("status") == 1:
            product = data.get("product", {})
            category = "unknown"
            if product.get("categories_hierarchy"):
                category = product["categories_hierarchy"][-1].replace(
                    "en:", "")
            return {
                "barcode": product.get("code"),
                "name": product.get("product_name", "Unknown Product"),
                "category": category
            }
        return None
    except Exception as e:
        print(f"Error fetching product info: {e}")
        return None
