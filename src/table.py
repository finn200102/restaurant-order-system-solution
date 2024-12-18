from src.order import Order
class Table:
    def __init__(self, table_number: int):
        """Init the table class"""
        self.table_number = int
        self.orders = []
        
    def add_order(self, order):
        """Add order to orders"""
        self.orders.append(order)

    def get_bill(self):
        """Returns the total_price of all orders on the table"""
        return sum([order.get_total_price() for order in self.orders])
