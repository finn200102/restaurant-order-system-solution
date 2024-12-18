"""Order module"""
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, order_item):
        """Adds an order to the items list"""
        self.items.append(order_item)

    def remove_item(self, idx):
        """Removes an item of the order"""
        if idx >= 0 and idx < len(self.items):
            self.items.pop(idx)
            return True
        else:
            return False
