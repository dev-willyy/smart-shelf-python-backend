import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "development")
PORT = int(os.getenv("PORT", 5000))
# Allowed food categories (comma-separated in .env)
ALLOWED_FOOD_CATEGORIES = os.getenv(
    "ALLOWED_FOOD_CATEGORIES", "dairy,meat,beverages,fruit,vegetables,bakery").split(',')
