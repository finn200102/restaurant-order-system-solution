"""This is the table module for the Table class."""
__author__ = "7157747, Gellien, 8425470, Heidusch"


class Table:
    """This is the Table class."""

    def __init__(self, table_number: int):
        """Init the table class."""
        self.table_number = table_number
        self.orders = []

    def add_order(self, order):
        """Add order to orders."""
        self.orders.append(order)

    def get_bill(self):
        """Return the total_price of all orders on the table."""
        return sum(
            order.get_total_price()
            for order in self.orders
        )

    def remove_order(self, idx):
        """Remove an order at the index idx."""
        if 0 <= idx < len(self.orders):
            self.orders.pop(idx)
            return True
        return False
