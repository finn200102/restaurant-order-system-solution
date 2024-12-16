"""Order module"""
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, order_item):
        """Adds an order to the items list"""
        self.items.append(order_item)