# statistics.py

import numpy as np

from history import read_records


def show_statistics():

    records = read_records()

    if len(records) == 0:

        print("No data available for statistics.")
        return

    quantities = []

    for record in records:

        quantities.append(
            int(record["quantity"])
        )

    data = np.array(quantities)

    print("========== WASTE STATISTICS ==========")

    print("Total records:", len(data))
    print("Total quantity:", np.sum(data))
    print("Average quantity:", np.mean(data))
    print("Minimum quantity:", np.min(data))
    print("Maximum quantity:", np.max(data))

    categories = set()

    for record in records:

        categories.add(record["category"])

    print("Different categories:", len(categories))

    print("Categories recorded:")

    for category in categories:

        print("-", category)