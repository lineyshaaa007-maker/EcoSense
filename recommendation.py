# recommendation.py

RECOMMENDATIONS = {
    "plastic": "Recycle the plastic through an appropriate recycling system.",
    "paper": "Recycle clean and dry paper.",
    "glass": "Place glass items in an appropriate glass recycling collection.",
    "metal": "Send suitable metal items for recycling.",
    "organic": "Consider composting suitable organic waste.",
    "e-waste": "Send electronic waste to an authorized e-waste collection facility."
}


def get_recommendation(material):

    return RECOMMENDATIONS.get(
        material,
        "No recommendation available."
    )


def display_recommendations():

    print("========== RECYCLING RECOMMENDATIONS ==========")

    for material, recommendation in RECOMMENDATIONS.items():

        print(material.title(), ":", recommendation)