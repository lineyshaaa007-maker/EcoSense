# classifier.py

MATERIALS = (
    "plastic",
    "paper",
    "glass",
    "metal",
    "organic",
    "e-waste"
)


def classify_waste(material):

    if material == "plastic":
        return "Plastic Waste"

    elif material == "paper":
        return "Paper Waste"

    elif material == "glass":
        return "Glass Waste"

    elif material == "metal":
        return "Metal Waste"

    elif material == "organic":
        return "Organic Waste"

    elif material == "e-waste":
        return "E-Waste"

    else:
        return "Unknown"


def is_valid_material(material):

    if material in MATERIALS:
        return True

    return False