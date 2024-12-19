from src.order import Order
class Table:
    def __init__(self, table_number: int):
        """Init the table class"""
        self.table_number = table_number
        self.orders = []
        
    def add_order(self, order):
        """Add order to orders"""
        self.orders.append(order)

    def get_bill(self):
        """Returns the total_price of all orders on the table"""
        return sum([order.get_total_price() for order in self.orders])
    
    def remove_order(self, idx):
        """Remove an order at the index idx"""
        if idx >= 0 and idx < len(self.orders):
            self.orders.pop(idx)
            return True
        else:
            return False
