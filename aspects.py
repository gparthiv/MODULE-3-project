ASPECTS = {
    "Vehicle": [
        "car", "vehicle", "automobile", "build", "design", "look"
    ],
    "Engine": [
        "engine", "motor", "power", "performance", "acceleration"
    ],
    "Battery": [
        "battery", "range", "charging", "charge"
    ],
    "Mileage": [
        "mileage", "fuel economy", "fuel consumption", "efficiency"
    ],
    "Safety": [
        "safety", "brakes", "airbags", "abs", "collision"
    ],
    "Comfort": [
        "comfort", "seat", "seats", "ride", "suspension", "space"
    ],
    "Service": [
        "service", "maintenance", "dealer", "repair"
    ],
    "Infotainment": [
        "infotainment", "screen", "display", "navigation", "audio",
        "speaker", "music", "bluetooth"
    ],
    "Price": [
        "price", "cost", "expensive", "cheap", "value", "money"
    ]
}


def extract_aspects(text):
    text = text.lower()
    found = []

    for aspect, keywords in ASPECTS.items():
        for keyword in keywords:
            if keyword in text:
                found.append(aspect)
                break

    return found