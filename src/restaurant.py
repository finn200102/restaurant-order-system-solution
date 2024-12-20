from src.order_item import OrderItem
from src.order import Order
class Restaurant:
    def __init__(self, menue):
        """Initializes the Restaurant class"""
        self.menue = menue
        self.tables = []

    def add_table(self, table):
        """Add a table to the restaurant"""
        self.tables.append(table)

    def get_table(self, idx):
        """Returns the table with the idx"""
        matches =  [t for t in self.tables if t.table_number == idx]
        return matches[0] if matches else None
    
    def add_order_to_table(self, idx, name, special_request, base_price):
        """Adds an order to a table"""
        order = Order()
        order.add_item(OrderItem(name, special_request, base_price))
        self.get_table(idx).add_order(order)

    def remove_order_from_table(self, idx, order_idx):
        """Remove the order_idx order from table idx"""
        self.get_table(idx).remove_order(order_idx)
    
    def save_bill(self, idx, filepath):
        """Saves the bill to a txt"""
        bill = self.get_table(idx).get_bill()
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"table number: {idx}, price: {bill}\n")