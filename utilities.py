# utilities.py


def display_header(title):

    print("=" * 55)
    print(title.center(55))
    print("=" * 55)


def get_condition():

    while True:

        condition = input(
            "Enter condition (clean/dirty/damaged): "
        ).strip().lower()

        if condition == "clean":
            return condition

        elif condition == "dirty":
            return condition

        elif condition == "damaged":
            return condition

        else:
            print("Please enter clean, dirty, or damaged.")


def get_status(material, condition):

    if material == "organic":

        return "Biodegradable"

    elif material == "e-waste":

        return "Special Disposal Required"

    elif condition == "clean":

        return "Recyclable"

    elif condition == "dirty":

        return "Needs Cleaning"

    elif condition == "damaged":

        return "Check Recycling Facility"

    else:

        return "Unknown"