# Simulated knowledge base mapping categories to recommended conditions and baseline spoilage days.
recommended_conditions = {
    "dairy": {"temp": 4, "humidity": 50, "baseline": 14},
    "meat": {"temp": 2, "humidity": 60, "baseline": 7},
    "beverages": {"temp": 4, "humidity": 55, "baseline": 30},
    "fruit": {"temp": 5, "humidity": 80, "baseline": 10},
    "vegetables": {"temp": 4, "humidity": 85, "baseline": 8},
    "bakery": {"temp": 20, "humidity": 50, "baseline": 3},
    "unknown": {"temp": 5, "humidity": 60, "baseline": 10}
}


def compute_spoilage(category, actual_temp, actual_humidity):
    rec = recommended_conditions.get(
        category, recommended_conditions["unknown"])
    recommended_temp = rec["temp"]
    recommended_humidity = rec["humidity"]
    baseline_days = rec["baseline"]

    # Penalize deviations in temperature.
    temp_diff = actual_temp - recommended_temp
    if temp_diff > 0:
        baseline_days -= temp_diff
    else:
        baseline_days -= abs(temp_diff) * 0.5

    # Penalize deviations in humidity.
    hum_penalty = int(abs(actual_humidity - recommended_humidity) // 5)
    baseline_days -= hum_penalty

    predicted_spoilage_days = max(1, int(baseline_days))
    return {
        "recommended_temp": recommended_temp,
        "recommended_humidity": recommended_humidity,
        "predicted_spoilage_days": predicted_spoilage_days
    }
