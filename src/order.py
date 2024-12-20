"""Order module"""

from src.order_item import OrderItem

class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, order_item):
        """Adds an order to the items list
        
        Args:
            order_items(OrderItem): an instance of the OrderItem class
        """
        self.items.append(order_item)
        print(f"Das folgende Gericht wurde aufgenommen:{self.order_item_to_string(order_item)}")

    def list_items(self):
        """Returns all the items of the order"""
        items = [f"Orderitem {idx}: " + self.order_item_to_string(item) for idx, item in enumerate(self.items)]
        return "".join(items)
        
        
    def order_item_to_string(self, order_item):
        """Returns an OrderItem object as a string
        
        Args:
            order_item(OrderItem): an OrderItem object
        """
        return f"\nName: {order_item.name}\nSpecialrequests: {order_item.special_request}\nBaseprice: {order_item.base_price}\n"

    def remove_item(self, idx: int):
        """Removes an item of the order
        
        Args:
            idx(int): The index of the OrderItem in self.items
        """
        if idx >= 0 and idx < len(self.items):
            print(f"Das folgende Gericht wurde entfernt:{self.order_item_to_string(self.items[idx])}")
            self.items.pop(idx)
            return True
        else:
            return False
        
    def add_special_requests_to_item(self, idx: int, special_requests):
        """Adds list of special requests to a specific orderitem of the order
        
        Args:
            idx (int): The index of the OrderItem in self.items
            special_requests (list[str]): A list of the special_requests (can be empty)
        """
        print(f"Es wurde '{special_requests}' zu dem folgenden Gericht hinzugefügt: {self.order_item_to_string(self.items[idx])}")
        self.items[idx].special_request += special_requests
        

        
    def get_total_price(self):
        """Calculates and returns the total price of the order"""
        summ = sum([item.base_price + len(item.special_request) for item in self.items])
        print(f"Der Gesamtbetrag ist: {summ}")
        return summ