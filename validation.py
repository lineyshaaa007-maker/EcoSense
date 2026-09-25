# validation.py


def validate_item_name(item):

    if item.strip() == "":
        return False

    return True


def validate_quantity(quantity):

    if quantity > 0:
        return True

    return False


def get_quantity():

    while True:

        try:

            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0.")

        except ValueError:

            print("Please enter a valid whole number.")