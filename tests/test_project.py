# test_project.py

from classifier import classify_waste, is_valid_material
from validation import validate_quantity
from recommendation import get_recommendation


def test_classification():

    assert classify_waste("plastic") == "Plastic Waste"
    assert classify_waste("paper") == "Paper Waste"
    assert classify_waste("glass") == "Glass Waste"


def test_material_validation():

    assert is_valid_material("plastic") == True
    assert is_valid_material("paper") == True
    assert is_valid_material("unknown") == False


def test_quantity_validation():

    assert validate_quantity(5) == True
    assert validate_quantity(0) == False
    assert validate_quantity(-2) == False


def test_recommendation():

    result = get_recommendation("plastic")

    assert "Recycle" in result


def run_tests():

    test_classification()
    test_material_validation()
    test_quantity_validation()
    test_recommendation()

    print("All tests passed successfully!")


if __name__ == "__main__":

    run_tests()