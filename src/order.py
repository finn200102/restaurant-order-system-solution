"""Order module"""
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, order_item):
        """Adds an order to the items list"""
        self.items.append(order_item)

    def remove_item(self, idx: int):
        """Removes an item of the order"""
        if idx >= 0 and idx < len(self.items):
            self.items.pop(idx)
            return True
        else:
            return False
        
    def add_special_requests_to_item(self, idx: int, special_requests):
        """Adds list of special requests to a specific orderitem of the order"""
        self.items[idx].special_request += special_requests

        
    def get_total_price(self):
        """Calculates and returns the total price of the order"""
        return sum([item.base_price+ len(item.special_request) for item in self.items])
