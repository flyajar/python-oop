import csv


class Item:
    # class attribute
    pay_rate = 0.8
    all = []

    # constructor
    def __init__(self, name: str, price: float, quantity: int):
        # validate the arguments
        assert price >= 0, f"Price should be non-negative number"
        assert quantity >= 0, f"Quantity should be a non-negative number"

        # assign to self object
        # these are instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('./../items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

