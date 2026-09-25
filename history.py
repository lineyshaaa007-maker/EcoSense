# history.py

import csv


FILE_NAME = "data/waste_records.csv"


def save_record(waste_item):

    file = open(FILE_NAME, "a", newline="")

    writer = csv.writer(file)

    writer.writerow([
        waste_item.item_name,
        waste_item.material,
        waste_item.condition,
        waste_item.quantity,
        waste_item.category,
        waste_item.status,
        waste_item.recommendation
    ])

    file.close()


def read_records():

    file = open(FILE_NAME, "r", newline="")

    reader = csv.DictReader(file)

    records = list(reader)

    file.close()

    return records


def display_history():

    records = read_records()

    print("========== WASTE HISTORY ==========")

    if len(records) == 0:

        print("No records available.")

    else:

        for record in records:

            print("---------- WASTE RECORD ----------")
            print("Item:", record["item_name"])
            print("Material:", record["material"])
            print("Condition:", record["condition"])
            print("Quantity:", record["quantity"])
            print("Category:", record["category"])
            print("Status:", record["status"])
            print("Recommendation:", record["recommendation"])


def search_records():

    records = read_records()

    search = input(
        "Enter item name or material to search: "
    ).lower()

    found = False

    for record in records:

        if (
            search in record["item_name"].lower()
            or search in record["material"].lower()
        ):

            print("---------- MATCH FOUND ----------")
            print("Item:", record["item_name"])
            print("Material:", record["material"])
            print("Condition:", record["condition"])
            print("Quantity:", record["quantity"])
            print("Category:", record["category"])
            print("Status:", record["status"])
            print("Recommendation:", record["recommendation"])

            found = True

    if found == False:

        print("No matching record found.")