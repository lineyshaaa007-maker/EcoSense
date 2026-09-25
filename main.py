# main.py

import classifier
import validation
import recommendation
import models
import history
import statistics
import utilities


def classify_waste_feature():

    utilities.display_header("CLASSIFY WASTE")

    item_name = input("Enter waste item name: ").strip()

    if validation.validate_item_name(item_name) == False:

        print("Item name cannot be empty.")
        return

    material = input(
        "Enter material (plastic/paper/glass/metal/organic/e-waste): "
    ).strip().lower()

    if classifier.is_valid_material(material) == False:

        print("Invalid material.")
        print(
            "Choose from plastic, paper, glass, metal, organic, e-waste."
        )
        return

    condition = utilities.get_condition()

    quantity = validation.get_quantity()

    category = classifier.classify_waste(material)

    status = utilities.get_status(
        material,
        condition
    )

    recommendation_text = recommendation.get_recommendation(
        material
    )

    waste_item = models.WasteItem(
        item_name,
        material,
        condition,
        quantity,
        category,
        status,
        recommendation_text
    )

    history.save_record(waste_item)

    waste_item.display()

    print("Record saved successfully!")


def main_menu():

    while True:

        utilities.display_header(
            "ECOSENSE - SMART WASTE CLASSIFICATION SYSTEM"
        )

        print("1. Classify Waste")
        print("2. View Waste History")
        print("3. Search Waste Records")
        print("4. View Waste Statistics")
        print("5. View Recycling Recommendations")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            classify_waste_feature()

        elif choice == "2":

            history.display_history()

        elif choice == "3":

            history.search_records()

        elif choice == "4":

            statistics.show_statistics()

        elif choice == "5":

            recommendation.display_recommendations()

        elif choice == "6":

            print("Thank you for using EcoSense!")

            break

        else:

            print("Invalid choice.")
            print("Please select a number from 1 to 6.")


main_menu()