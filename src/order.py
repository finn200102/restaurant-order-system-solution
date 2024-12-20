"""Order module"""
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, order_item):
        """Adds an order to the items list"""
        self.items.append(order_item)
        print(f"Das Gericht '{order_item}' wurde aufgenommen")

    def list_items(self):
        """Returns all the items of the order"""

    def remove_item(self, idx: int):
        """Removes an item of the order"""
        if idx >= 0 and idx < len(self.items):
            print(f"Das Gericht '{self.items[idx]}' wurde entfernt")
            self.items.pop(idx)
            return True
        else:
            return False
        
    def add_special_requests_to_item(self, idx: int, special_requests):
        """Adds list of special requests to a specific orderitem of the order"""
        print(f"Es wurde '{special_requests}' zu dem Gericht '{self.items[idx]}' hinzugefügt")
        self.items[idx] += special_requests

        
    def get_total_price(self):
        """Calculates and returns the total price of the order"""
        summ = sum([item.base_price + len(item.special_request) for item in self.items])
        print(f"Der Gesamtbetrag ist: {summ}")
        return summ