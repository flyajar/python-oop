class Item:
    # constructor
    def __init__(self, name: str, price: float, quantity: int):
        # validate the arguments
        assert price >= 0, f"Price should be non-negative number"
        assert quantity >= 0, f"Quantity should be a non-negative number"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 2, 5)

print(item1.calculate_total_price())
