# models.py


class WasteItem:

    def __init__(
        self,
        item_name,
        material,
        condition,
        quantity,
        category,
        status,
        recommendation
    ):

        self.item_name = item_name
        self.material = material
        self.condition = condition
        self.quantity = quantity
        self.category = category
        self.status = status
        self.recommendation = recommendation

    def display(self):

        print("---------- WASTE DETAILS ----------")
        print("Item:", self.item_name)
        print("Material:", self.material)
        print("Condition:", self.condition)
        print("Quantity:", self.quantity)
        print("Category:", self.category)
        print("Status:", self.status)
        print("Recommendation:", self.recommendation)